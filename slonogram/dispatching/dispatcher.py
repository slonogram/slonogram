from __future__ import annotations
from dataclasses import dataclass
from typing import (
    Any,
    overload,
    TypeVar,
    Iterable,
    Callable,
    TypeAlias,
)
from enum import IntEnum, auto


from .context import Context
from .layers import Layers
from .handler import RawHandler, Handler, Activation
from .stash import Stash

from .._internal.utils import call_alter_nullable, const
from ..exceptions.stash import CantReplaceStash
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


class StashRelation(IntEnum):
    PARENT = auto()
    CHILD = auto()


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


async def _run_after_exc(
    exc: Exception,
    ctx: Context[Any],
    after: ExcMiddleware[Any] | None,
) -> Activation[Any]:
    if after is None:
        raise exc
    await after(ctx, exc)

    return Activation.ignored()


async def _run_after_strict(
    ctx: Context[Any],
    after: ExcMiddleware[Any] | None,
) -> None:
    if after is not None:
        await after(ctx, None)


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
        stash: Stash | None = None,
    ) -> None:
        self.name = name
        self.children = children

        self.stash = stash or Stash()
        self.handlers = handlers or DispatcherHandlers()
        self.layers = layers or Layers()

    def alter(
        self,
        layers: AlterFn[Layers[[], Any]] | None = None,
        handlers: AlterFn[DispatcherHandlers] | None = None,
        children: AlterFn[tuple[Dispatcher, ...]] | None = None,
        stash: AlterFn[Stash] | None = None,
    ) -> Dispatcher:
        return Dispatcher(
            self.name,
            children=call_alter_nullable(children, self.children),
            handlers=call_alter_nullable(handlers, self.handlers),
            layers=call_alter_nullable(layers, self.layers),
            stash=call_alter_nullable(stash, self.stash),
        )

    def with_stash(
        self,
        stash: Stash,
        *,
        relation: StashRelation | None = StashRelation.CHILD,
    ) -> Dispatcher:
        """Creates dispatcher with a new stash.

        :param stash: stash to replace
        :param relation: controls how new stash relates with the dispatcher's one, there's three variants:
                         - No relation - specify None
                         - `StashRelation.PARENT` - specified stash would be parent of the dispatcher's
                         - `StashRelation.CHILD` - specified stash would be child of the disptacher's
        :raises slonogram.exceptions.stash.CantReplaceStash: if `Dispatcher` have any children

        """
        if self.children:
            raise CantReplaceStash()

        match relation:
            case StashRelation.CHILD:
                stash = Stash(stash.types, parent=self.stash)
            case StashRelation.PARENT:
                stash = Stash(self.stash.types, parent=stash)

        return self.alter(stash=const(stash))

    def child(
        self,
        dp: Dispatcher,
        *,
        relation: StashRelation | None = StashRelation.PARENT,
    ) -> Dispatcher:
        match relation:
            case None:
                f = lambda head: (*head, dp)
            case StashRelation.PARENT | StashRelation.CHILD:
                f = lambda head: (
                    *head,
                    dp.with_stash(self.stash, relation=relation),
                )

        return self.alter(children=f)

    def prepare(self, prepare: BareMiddleware[Any, []]) -> Dispatcher:
        return self.alter(layers=lambda layers: layers.copy_with(prepare=prepare))

    def before(self, before: BareMiddleware[Any, []]) -> Dispatcher:
        return self.alter(layers=lambda layers: layers.copy_with(before=before))

    def after(
        self,
        after: BareMiddleware[Any, [Exception | None]],
    ) -> Dispatcher:
        return self.alter(layers=lambda layers: layers.copy_with(after=after))

    def filter(self, filter: BareFilter[Any]) -> Dispatcher:
        return self.alter(layers=lambda layers: layers.copy_with(filter=filter))

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

        return self.alter(
            handlers=lambda handlers: handlers.extended_from(
                message=interests.yield_if(Interest.MESSAGE, h),
                edited_message=interests.yield_if(Interest.EDITED_MESSAGE, h),
                callback_query=interests.yield_if(Interest.CALLBACK_QUERY, h),
                inline_query=interests.yield_if(Interest.INLINE_QUERY, h),
            )
        )

    # Dispatching

    async def dispatch_to_children(
        self,
        ctx: Context[Any],
        update: Update,
        bot: Bot,
    ) -> Activation[Any]:
        after = self.layers.after
        activation: Activation[Any] = Activation.ignored()

        for child in self.children:
            try:
                activation = await child.feed_single(update, bot)
            except Exception as exc:
                return await _run_after_exc(exc, ctx, after)

            if activation.is_activated:
                break

        await _run_after_strict(ctx, after)
        return activation

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
        after = layers.after

        try:
            if layers.prepare is not None:
                await layers.prepare(context)

            if layers.filter is not None and not layers.filter(context):
                return Activation.ignored()

            if layers.before is not None:
                await layers.before(context)
        except Exception as exc:
            return await _run_after_exc(exc, context, after)

        for handler in handlers:
            try:
                activation = await handler(context)
            except Exception as exc:
                return await _run_after_exc(exc, context, after)
            else:
                await _run_after_strict(context, after)

            if activation.is_activated:
                return activation

        return await self.dispatch_to_children(
            context,
            update,
            bot,
        )

    def collect_interests(self) -> set[Interest]:
        interests = set[Interest]()
        h = self.handlers

        for interest, arr in (
            (Interest.EDITED_MESSAGE, h.edited_message),
            (Interest.MESSAGE, h.message),
            (Interest.CALLBACK_QUERY, h.callback_query),
            (Interest.INLINE_QUERY, h.inline_query),
        ):
            if arr:
                interests.add(interest)

        for child in self.children:
            interests.update(child.collect_interests())
        return interests


__all__ = [
    "Dispatcher",
]
