from typing import (
    TypeVar,
    List,
    NoReturn,
    Optional,
    TypeAlias,
)
from anyio import create_task_group

from ..types.event_flags import MessageFlags, EmptyFlags
from ..types.context import InterContextData, Context

from ..exceptions.control_flow import DoNotHandle, SkipLocalSet
from ..exceptions.api_error import ApiError

from ..handling.handler import Handler
from ..schemas import Message, UpdateType, Update
from ..bot import Bot

from .local_set import LocalSet


T = TypeVar("T")
MsgCtx: TypeAlias = Context[Message]


class Dispatcher:
    """
    ### drop_pending:

    calls `deleteWebhook` with `drop_pending_updates` before the run
    """

    def __init__(self, bot: Bot, drop_pending: bool = False) -> None:
        self.set: LocalSet = LocalSet("__dispatcher__")
        self.drop_pending = drop_pending
        self._bot = bot
        self.data = None

    async def _handle_set(
        self, attr: str, set_: LocalSet, ctx: Context[T]
    ) -> bool:
        filter_ = set_.filter_
        parent_pad = ctx.pad
        ctx.pad = parent_pad.create_child()

        try:
            if filter_ is not None and not await filter_(ctx):
                return False

            mw = set_._middleware # noqa
            if mw is not None:
                await mw(ctx)
            h_list: List[Handler[T]] = getattr(set_, attr)

            for handler in h_list:
                if await handler.try_invoke(ctx):
                    return True

            for child in set_._children:  # noqa
                if await self._handle_set(attr, child, ctx):
                    return True
        except SkipLocalSet:
            return False
        finally:
            ctx.pad = parent_pad

        return False

    async def feed_update(
        self, inter: InterContextData, update: Update
    ) -> bool:
        try:
            if update.message is not None:
                return await self._handle_set(
                    "sent_message_handlers",
                    self.set,
                    Context(inter, MessageFlags.SENT, update.message),
                )
            elif update.edited_message is not None:
                return await self._handle_set(
                    "edited_message_handlers",
                    self.set,
                    Context(
                        inter, MessageFlags.EDITED, update.edited_message
                    ),
                )
            elif update.callback_query is not None:
                return await self._handle_set(
                    "callback_handlers",
                    self.set,
                    Context(inter, EmptyFlags.EMPTY, update.callback_query)
                )
            elif update.inline_query is not None:
                raise NotImplementedError

            elif update.channel_post is not None:
                raise NotImplementedError
            elif update.chat_join_request is not None:
                raise NotImplementedError
            elif update.chat_member is not None:
                raise NotImplementedError
            elif update.chosen_inline_result is not None:
                raise NotImplementedError
            elif update.edited_channel_post is not None:
                raise NotImplementedError
            elif update.my_chat_member is not None:
                raise NotImplementedError
            elif update.poll is not None:
                raise NotImplementedError
            elif update.poll_answer is not None:
                raise NotImplementedError
            elif update.pre_checkout_query is not None:
                raise NotImplementedError
            elif update.shipping_query is not None:
                raise NotImplementedError
        except DoNotHandle:
            pass

        return False

    async def create_intercontext_data(self) -> InterContextData:
        me = await self._bot.user.get_me()
        return InterContextData(
            me, self.data, self._bot, create_task_group()
        )

    async def _drop_pending_updates(self) -> None:
        try:
            await self._bot.update.delete_webhook(True)
        except ApiError:
            pass

    async def run_polling(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> NoReturn:
        if self.drop_pending:
            await self._drop_pending_updates()

        inter = await self.create_intercontext_data()
        get_updates = self._bot.update.poll
        feed = self.feed_update

        if allowed_updates is None:
            allowed_updates = list(self.set.collect_update_types())

        async with inter.task_group as tg:
            while True:
                updates = await get_updates(
                    offset, limit, timeout, allowed_updates  # type: ignore
                )

                if updates:
                    offset = updates[-1].id + 1

                for update in updates:
                    tg.start_soon(feed, inter, update)  # type: ignore
