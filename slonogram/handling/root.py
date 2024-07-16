from __future__ import annotations

import dataclasses as dtc
import typing as t

from sena.control_flow import Break as _Break

from ..types.ctx import Ctx
from ..types.slots import Slots

from ..utils.altering import alter1, Alterer1
from ..utils.omit import Omittable, OMIT
from ..utils.stash import ward_stash

from ..schemas.update import Update
from ..schemas.message import Message
from ..schemas.callback_query import CallbackQuery

from .handler import (
    AbstractHandler,
    HandlerFn,
    Handler,
    Next,
    Mapper,
)
from .control_flow import (
    ControlFlow,
    Continue,
    Break,
)

D = t.TypeVar("D")

class RootHandler(HandlerFn[Update], t.Protocol):
    slots: Slots

    def alter(
        self,
        *,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> t.Self:
        ...

class RootHandlerFactory(t.Protocol):
    def __call__(self, slots: Slots, /) -> RootHandler:
        ...

async def _continue(ctx: Ctx[Update]) -> Continue[Update]:
    return Continue(ctx)

# TODO: This logic is quite a mess. We need to convert `Ctx[D]` to `Ctx[Update]` and
# `ControlFlow[D]` to `Ctx[Update]` some more civilized way.
async def _dispatch(
    orig: Ctx[Update],
    handlers: tuple[HandlerFn[D], ...],
    ctx: Ctx[D],
    next: Next[Update],
) -> ControlFlow[Update]:
    async def _next(req: Ctx[D]) -> ControlFlow[D]:
        # Assuming that `ctx` was not changed
        result = await next(orig)
        if isinstance(result, _Break):
            return Break(result.value)
        return Continue(orig)

    for handler in handlers:
        result = await ward_stash(handler, ctx, _next)

        if isinstance(result, _Break):
            return Break(result.value)

    return Continue(orig)

class DefaultRootHandler(RootHandler):
    __slots__ = ('slots', )

    slots: Slots

    def __init__(self, slots: Slots) -> None:
        self.slots = slots

    def alter(
        self,
        *,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> t.Self:
        return type(self)(
            slots=alter1(slots, self.slots),
        )

    def __repr__(self) -> str:
        return f"DefaultRootHandler(slots={self.slots!r})"

    def __call__(self, ctx: Ctx[Update], next: Next[Update]) -> t.Awaitable[ControlFlow[Update]]:
        upd = ctx.data
        slots = self.slots

        if upd.callback_query is not None:
            return _dispatch(
                ctx,
                slots.callback_query,
                ctx.with_data(upd.callback_query),
                next,
            )
        elif upd.message is not None:
            return _dispatch(
                ctx,
                slots.message,
                ctx.with_data(upd.message),
                next,
            )

        return _continue(ctx)

def slots_lens(alterer: Alterer1[Slots]) -> Alterer1[RootHandler]:
    return lambda h: h.alter(slots=alterer)

class Root(AbstractHandler[Update]):
    __slots__ = ('handler', 'factory')

    handler: RootHandler
    factory: RootHandlerFactory

    def __init__(self, handler: RootHandler, factory: RootHandlerFactory) -> None:
        self.handler = handler
        self.factory = factory

    @classmethod
    def from_slots(
        cls,
        slots: Omittable[Slots] = OMIT,
        root_handler_factory: Omittable[RootHandlerFactory] = OMIT,
    ) -> t.Self:
        _slots: Slots = Slots() if slots is OMIT else t.cast(Slots, slots)
        _root_handler_factory = (
            DefaultRootHandler
            if root_handler_factory is OMIT
            else t.cast(RootHandlerFactory, root_handler_factory)
        )

        return cls(_root_handler_factory(_slots), _root_handler_factory)

    def alter(
        self,
        *,
        handler: Omittable[Alterer1[RootHandler]] = OMIT,
        factory: Omittable[Alterer1[RootHandlerFactory]] = OMIT,
    ) -> t.Self:
        return type(self)(
            handler=alter1(handler, self.handler),
            factory=alter1(factory, self.factory),
        )

    def on_message(self, *hs: HandlerFn[Message]) -> t.Self:
        return self.alter(handler=slots_lens(
            lambda s: dtc.replace(s, message=(*s.message, *hs)),
        ))

    def on_callback_query(self, *hs: HandlerFn[CallbackQuery]) -> t.Self:
        return self.alter(handler=slots_lens(
            lambda s: dtc.replace(s, callback_query=(*s.callback_query, *hs)),
        ))

    def map(self, f: Mapper[Update]) -> AbstractHandler[Update]:
        return Handler(f(self.handler))

    def __repr__(self) -> str:
        return f"Root(handler={self.handler!r}, factory={self.factory!r})"

    def __call__(self, req: Ctx[Update], next: Next[Update]) -> t.Awaitable[ControlFlow[Update]]:
        return self.handler(req, next)


__all__ = [
    "Root",
    "RootHandler",
    "RootHandlerFactory",
    "DefaultRootHandler",
]

