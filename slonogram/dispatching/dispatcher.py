from __future__ import annotations
from dataclasses import dataclass
from typing import Any, overload, TypeVar, Iterable, Callable, TypeAlias

from .context import Context
from .layers import Layers
from .handler import RawHandler, Handler, Activation
from .stash import Stash

from ..filtering.base import BareFilter
from ..middleware import (
    SimpleMiddleware,
    BareMiddleware,
    ExcMiddleware,
)

from ..types.interest import Interest
from ..schemas import (
    Message,
    Update,
    CallbackQuery,
    InlineQuery,
)
from ..bot import Bot

from .interests import InterestCombinator

T = TypeVar("T")
C1 = TypeVar("C1")
M = TypeVar("M")

AlterFn: TypeAlias = Callable[[T], T]


@dataclass(slots=True, frozen=True)
class DispatcherHandlers:
    message: tuple[Handler[Message], ...] = ()
    edited_message: tuple[Handler[Message], ...] = ()

    callback_query: tuple[Handler[CallbackQuery], ...] = ()
    inline_query: tuple[Handler[InlineQuery], ...] = ()

    def extended_from(
        self,
        message: Iterable[Handler[Message]],
        edited_message: Iterable[Handler[Message]],
        callback_query: Iterable[Handler[CallbackQuery]],
        inline_query: Iterable[Handler[InlineQuery]],
    ) -> DispatcherHandlers:
        return DispatcherHandlers(
            message=(*self.message, *message),
            edited_message=(*self.edited_message, *edited_message),
            callback_query=(*self.callback_query, *callback_query),
            inline_query=(*self.inline_query, *inline_query),
        )


class Dispatcher:
    __slots__ = (
        "name",
        "children",
        "stash",
        "handlers",
        "layers",
    )

    def __init__(
        self,
        name: str | None = None,
        children: tuple[Dispatcher, ...] = (),
        handlers: DispatcherHandlers | None = None,
        layers: Layers[[], Any] | None = None,
    ) -> None:
        self.name = name
        self.children = children

        self.stash = Stash()
        self.handlers = handlers or DispatcherHandlers()
        self.layers = layers or Layers()

    def alter_layers(
        self,
        f: AlterFn[Layers[[], Any]],
    ) -> Dispatcher:
        return Dispatcher(
            self.name,
            children=self.children,
            handlers=self.handlers,
            layers=f(self.layers),
        )

    def alter_handlers(self, f: AlterFn[DispatcherHandlers]) -> Dispatcher:
        return Dispatcher(
            self.name,
            children=self.children,
            handlers=f(self.handlers),
            layers=self.layers,
        )

    def alter_children(self, f: AlterFn[tuple[Dispatcher, ...]]) -> Dispatcher:
        return Dispatcher(
            self.name,
            children=f(self.children),
            handlers=self.handlers,
            layers=self.layers,
        )

    def child(self, dp: Dispatcher) -> Dispatcher:
        return self.alter_children(lambda head: (*head, dp))

    def prepare(self, prepare: BareMiddleware[Any, []]) -> Dispatcher:
        return self.alter_layers(lambda layers: layers.copy_with(prepare=prepare))

    def before(self, before: BareMiddleware[Any, []]) -> Dispatcher:
        return self.alter_layers(lambda layers: layers.copy_with(before=before))

    def after(
        self,
        after: BareMiddleware[Any, [Exception | None]],
    ) -> Dispatcher:
        return self.alter_layers(lambda layers: layers.copy_with(after=after))

    def filter(self, filter: BareFilter[Any]) -> Dispatcher:
        return self.alter_layers(lambda layers: layers.copy_with(filter=filter))

    @overload
    def on(
        self,
        interests: InterestCombinator[C1, M],
        handler: RawHandler[M],
        filter: BareFilter[M] | None = None,
        *,
        prepare: SimpleMiddleware[M] | None = None,
        before: SimpleMiddleware[M] | None = None,
        after: ExcMiddleware[M] | None = None,
    ) -> Dispatcher:
        ...

    @overload
    def on(
        self,
        interests: InterestCombinator[C1, M],
        handler: Handler[M],
    ) -> Dispatcher:
        ...

    def on(
        self,
        interests: InterestCombinator[C1, M],
        handler: Handler[M] | RawHandler[M],
        filter: BareFilter[M] | None = None,
        *,
        observer: bool = False,
        prepare: SimpleMiddleware[M] | None = None,
        before: SimpleMiddleware[M] | None = None,
        after: ExcMiddleware[M] | None = None,
    ) -> Dispatcher:
        h: Handler[Any] = (
            handler
            if isinstance(handler, Handler)
            else Handler(
                handler,
                layers=Layers(
                    prepare=prepare,
                    before=before,
                    after=after,
                    filter=filter,
                ),
                observer=observer,
            )
        )

        return self.alter_handlers(
            lambda handlers: handlers.extended_from(
                message=interests.yield_if(Interest.MESSAGE, h),
                edited_message=interests.yield_if(Interest.EDITED_MESSAGE, h),
                callback_query=interests.yield_if(Interest.CALLBACK_QUERY, h),
                inline_query=interests.yield_if(Interest.INLINE_QUERY, h),
            )
        )

    # Dispatching

    async def dispatch_to_children(self, update: Update, bot: Bot) -> Activation[Any]:
        for child in self.children:
            activation = await child.feed_single(update, bot)

            if activation.is_activated:
                return activation

        return Activation.ignored()

    async def feed_single(self, update: Update, bot: Bot) -> Activation[Any]:
        ref = self.handlers
        handlers: tuple[Handler[Any], ...]
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
            handlers = ref.inline_query
            context.model = update.inline_query
        elif update.chosen_inline_result is not None:
            raise NotImplementedError
        elif update.callback_query is not None:
            handlers = ref.callback_query
            context.model = update.callback_query
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
            return Activation.ignored()
        layers = self.layers

        try:
            if layers.prepare is not None:
                await layers.prepare(context)

            if layers.filter is not None and not layers.filter(context):
                return Activation.ignored()

            if layers.before is not None:
                await layers.before(context)

            for handler in handlers:
                if (activation := await handler(context)).is_activated:
                    return activation
        except Exception as exc:
            if layers.after is None:
                # TODO: Maybe handling?
                raise exc
            await layers.after(context, exc)
        else:
            if layers.after is not None:
                await layers.after(context, None)

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


__all__ = [
    "Dispatcher",
]
