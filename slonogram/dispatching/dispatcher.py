from typing import (
    Generic,
    TypeVar,
    List,
    NoReturn,
    Optional,
    TypeAlias,
)
from anyio import create_task_group

from ..schemas import Message, UpdateType, Update
from ..bot import Bot
from .context import InterContextData, Context
from .local_set import LocalSet


D = TypeVar("D")
MsgCtx: TypeAlias = Context[D, Message]


class Dispatcher(Generic[D]):
    """
    ### skip_pending:

    skips updates sent before the current time
    (time is retrieved through the `time.time`)
    """

    def __init__(
        self, data: D, bot: Bot, skip_pending: bool = False
    ) -> None:
        self.set: LocalSet = LocalSet("__dispatcher__")
        self.skip_pending = skip_pending
        self._bot = bot
        self._data = data

    async def feed_update(
        self, inter: InterContextData[D], update: Update
    ) -> bool:
        if update.message is not None:
            raise NotImplementedError
        if update.edited_message is not None:
            raise NotImplementedError
        if update.callback_query is not None:
            raise NotImplementedError
        if update.inline_query is not None:
            raise NotImplementedError

        if update.channel_post is not None:
            raise NotImplementedError
        if update.chat_join_request is not None:
            raise NotImplementedError
        if update.chat_member is not None:
            raise NotImplementedError
        if update.chosen_inline_result is not None:
            raise NotImplementedError
        if update.edited_channel_post is not None:
            raise NotImplementedError
        if update.my_chat_member is not None:
            raise NotImplementedError
        if update.poll is not None:
            raise NotImplementedError
        if update.poll_answer is not None:
            raise NotImplementedError
        if update.pre_checkout_query is not None:
            raise NotImplementedError
        if update.shipping_query is not None:
            raise NotImplementedError
        return False

    async def create_intercontext_data(self) -> InterContextData[D]:
        me = await self._bot.user.get_me()
        return InterContextData(
            me, self._data, self._bot, create_task_group()
        )

    async def run_polling(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> NoReturn:
        inter = await self.create_intercontext_data()
        get_updates = self._bot.updates.get
        feed = self.feed_update

        async with inter.task_group as tg:
            while True:
                updates = await get_updates(
                    offset, limit, timeout, allowed_updates
                )

                if updates:
                    offset = updates[-1].id + 1

                for update in updates:
                    tg.start_soon(feed, inter, update)
