import typing as t

from .base import SeqHandler
from .modify import Modify
from .reducible import Reducer

I = t.TypeVar("I")
O = t.TypeVar("O")

Acc = t.TypeVar("Acc")

C = t.TypeVar("C")
N = t.TypeVar("N")
Next = t.TypeVar("Next")


class Apply(t.Generic[C, N], Modify):
    __slots__ = ('current', 'next')

    def __init__(self, current: C, next: N) -> None:
        self.current = current
        self.next = next

    def __repr__(self) -> str:
        return f"Apply(current={self.current!r}, next={self.next!r})"

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        # (initial @ current) @ next
        return f(f(initial, self.current), self.next)

    def __call__(
        self: Apply[SeqHandler[I, O, N], N],
        req: I,
    ) -> O:
        return self.current(req, self.next)


