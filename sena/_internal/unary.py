from __future__ import annotations

from .base import Predicate
from .ext import HandlerExt
from .reducible import Reducer

import typing as t

Acc = t.TypeVar("Acc")
I = t.TypeVar("I")
O = t.TypeVar("O")

Rhs = t.TypeVar("Rhs")
Op = t.TypeVar("Op")


def not_(arg: I, rhs: Predicate[I]) -> bool:
    return not rhs(arg)


class Unary(HandlerExt, t.Generic[Rhs, Op]):
    __slots__ = ("rhs", "op")

    def __init__(
        self,
        rhs: Rhs,
        op: Op,
    ) -> None:
        self.rhs = rhs
        self.op = op

    def __repr__(self) -> str:
        return f"Unary(rhs={self.rhs!r}, op={self.op!r})"

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        return f(initial, self.rhs)

    def __call__(
        self: Unary[Rhs, t.Callable[[I, Rhs], O]],
        req: I,
    ) -> O:
        return self.op(req, self.rhs)
