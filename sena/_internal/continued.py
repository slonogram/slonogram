from __future__ import annotations

import typing as t

from .reducible import Reducer
from .base import Handler, AsyncHandler
from .modify import Modify

H = t.TypeVar("H")

Acc = t.TypeVar("Acc")

I = t.TypeVar("I")
O = t.TypeVar("O")
NR = t.TypeVar("NR")

class AsyncContinued(Modify, t.Generic[H]):
    """Same as [`Continued`], but additionally awaits handler
    and next function. 
    """

    __slots__ = ('handler', )

    def __init__(self, handler: H) -> None:
        self.handler = handler

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        return f(initial, self.handler)

    def __repr__(self) -> str:
        return f"AsyncContinued(handler={self.handler!r})"

    async def __call__(
        self: AsyncContinued[AsyncHandler[I, O]],
        req: I,
        next: t.Callable[[O], t.Awaitable[NR]],
    ) -> NR:
        return await next(await self.handler(req))

class Continued(Modify, t.Generic[H]):
    """Converts plain handler into sequential handler, by simply
    feeding `next` function with output of the handler.
    """

    __slots__ = ('handler', )

    def __init__(self, handler: H) -> None:
        self.handler = handler

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        return f(initial, self.handler)

    def __repr__(self) -> str:
        return f"Continued(handler={self.handler!r})"

    def __call__(
        self: Continued[Handler[I, O]],
        req: I,
        next: t.Callable[[O], NR],
    ) -> NR:
        return next(self.handler(req))


