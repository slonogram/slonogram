from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, overload, TypeAlias, Literal, TypeVar, Iterable

from .context import Context
from .layers import Layers
from .handler import RawHandler, Handler, HandlerActivation
from .stash import Stash

from ..filtering.base import BareFilter
from ..middleware import SimpleMiddleware, ExcMiddleware

from ..types.interest import Interest
from ..schemas import Update, Message
from ..bot import Bot

from .interests import InterestedHandler

T = TypeVar("T")


# This is needed since [] is considered falsy and
# `message or self.message` in that case will be `self.message`, not `[]` as intended
def _prefer(val: T | None, fallback: T) -> T:
    if val is None:
        return fallback
    return val


@dataclass(slots=True, frozen=True)
class DispatcherHandlers:
    message: list[Handler[Message]] = field(default_factory=list)
    edited_message: list[Handler[Message]] = field(default_factory=list)

    def extended_from(
        self,
        message: Iterable[Handler[Message]],
        edited_message: Iterable[Handler[Message]],
    ) -> DispatcherHandlers:
        return DispatcherHandlers(
            message=[*self.message, *message],
            edited_message=[*self.edited_message, *edited_message],
        )


M = TypeVar("M")
MessageInterest: TypeAlias = (
    Literal[Interest.MESSAGE] | Literal[Interest.EDITED_MESSAGE]
)


class Dispatcher:
    __slots__ = (
        "name",
        "children",
        "stash",
        "handlers",
    )

    def __init__(
        self,
        name: str | None = None,
        children: list[Dispatcher] | None = None,
        handlers: DispatcherHandlers | None = None,
    ) -> None:
        self.name = name

        if children is None:
            self.children = []
        else:
            self.children = children

        self.stash = Stash()
        self.handlers = handlers or DispatcherHandlers()

    @overload
    def register(
        self,
        handler: InterestedHandler[RawHandler[M]],
        filter: BareFilter[M] | None = None,
        *,
        prepare: SimpleMiddleware[M] | None = None,
        before: SimpleMiddleware[M] | None = None,
        after: ExcMiddleware[M] | None = None,
    ) -> Dispatcher:
        ...

    @overload
    def register(self, handler: InterestedHandler[Handler[M]]) -> Dispatcher:
        ...

    def register(
        self,
        handler: InterestedHandler[RawHandler[M]] | InterestedHandler[Handler[M]],
        filter: BareFilter[M] | None = None,
        *,
        prepare: SimpleMiddleware[M] | None = None,
        before: SimpleMiddleware[M] | None = None,
        after: ExcMiddleware[M] | None = None,
    ) -> Dispatcher:
        h: InterestedHandler[Handler[Any]]

        if isinstance(handler.handler, Handler):
            h = handler
        else:
            h = handler.map(
                lambda raw: Handler(
                    raw,
                    layers=Layers(
                        prepare=prepare,
                        before=before,
                        after=after,
                        filter=filter,
                    ),
                )
            )

        return Dispatcher(
            self.name,
            self.children,
            self.handlers.extended_from(
                message=h.message(),
                edited_message=h.edited_message(),
            ),
        )

    # Dispatching

    async def dispatch_to_children(self, update: Update, bot: Bot) -> HandlerActivation:
        for child in self.children:
            if await child.dispatch(update, bot) == HandlerActivation.activated:
                return HandlerActivation.activated

        return HandlerActivation.ignored

    async def dispatch(self, update: Update, bot: Bot) -> HandlerActivation:
        ref = self.handlers
        handlers: list[Handler[Any]]
        context = Context[Any](self.stash, None, bot)

        if update.message is not None:
            handlers = ref.message
            context.model = update.message
        elif update.edited_message is not None:
            handlers = ref.edited_message
            context.model = update.edited_message
        elif update.channel_post is not None:
            raise NotImplementedError
        elif update.edited_channel_post is not None:
            raise NotImplementedError
        elif update.inline_query is not None:
            raise NotImplementedError
        elif update.chosen_inline_result is not None:
            raise NotImplementedError
        elif update.callback_query is not None:
            raise NotImplementedError
        elif update.shipping_query is not None:
            raise NotImplementedError
        elif update.pre_checkout_query is not None:
            raise NotImplementedError
        elif update.poll is not None:
            raise NotImplementedError
        elif update.poll_answer is not None:
            raise NotImplementedError
        elif update.my_chat_member is not None:
            raise NotImplementedError
        elif update.chat_member is not None:
            raise NotImplementedError
        elif update.chat_join_request is not None:
            raise NotImplementedError
        else:
            return await self.dispatch_to_children(update, bot)

        for handler in handlers:
            if await handler(context) == HandlerActivation.activated:
                return HandlerActivation.activated

        return await self.dispatch_to_children(update, bot)

    def collect_interests(self) -> set[Interest]:
        interests = set[Interest]()
        h = self.handlers

        if h.edited_message:
            interests.add(Interest.EDITED_MESSAGE)
        if h.message:
            interests.add(Interest.MESSAGE)

        for child in self.children:
            interests.update(child.collect_interests())
        return interests
