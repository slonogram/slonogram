from __future__ import annotations

import typing as t

from ..types.ctx import Ctx
from ..types.slots import Slots

from ..utils.altering import alter1, Alterer1
from ..utils.omit import Omittable, OMIT

from ..schemas.update import Update

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

class RootHandler(t.Protocol, HandlerFn[Update]):
    slots: Slots

    def alter(
        self,
        *,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> t.Self:
        ...


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

    async def __call__(self, ctx: Ctx[Update], next: Next[Update]) -> ControlFlow[Update]:
        raise NotImplementedError


class Root(AbstractHandler[Update]):
    __slots__ = ('inner', )

    inner: RootHandler

    def __init__(
        self,
        slots: Omittable[Slots] = OMIT,
        root_handler_factory: Omittable[t.Callable[[Slots], RootHandler]] = OMIT,
    ) -> None:
        _slots: Slots = Slots() if slots is OMIT else t.cast(Slots, slots)
        if root_handler_factory is OMIT:
            self.inner = DefaultRootHandler(_slots)
        else:
            factory = t.cast(t.Callable[[Slots], RootHandler], root_handler_factory)
            self.inner = factory(_slots)

    def map(self, f: Mapper[Update]) -> AbstractHandler[Update]:
        return Handler(f(self.inner))

    def __call__(self, req: Ctx[Update], next: Next[Update]) -> t.Awaitable[ControlFlow[Update]]:
        return self.inner(req, next)


__all__ = [
    "Root",
    "RootHandler",
    "DefaultRootHandler",
]

