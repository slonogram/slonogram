from __future__ import annotations

import typing as t

from .base import SeqHandler
from .apply import Apply

from .ext import SeqHandlerExt
from .reducible import Reducer

C = t.TypeVar("C")
N = t.TypeVar("N")
Acc = t.TypeVar("Acc")
Next = t.TypeVar("Next")

I = t.TypeVar("I")
O = t.TypeVar("O")


class Then(SeqHandlerExt, t.Generic[C, Next]):
    __slots__ = ("current", "next")

    def __init__(self, current: C, next: Next) -> None:
        self.current = current
        self.next = next

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        # (initial @ current) @ next
        return f(f(initial, self.current), self.next)

    def __repr__(self) -> str:
        return f"Then(current={self.current!r}, next={self.next!r})"

    def __call__(
        self: Then[SeqHandler[I, O, Apply[Next, N]], Next],
        req: I,
        next: N,
    ) -> O:
        return self.current(req, Apply(self.next, next))
