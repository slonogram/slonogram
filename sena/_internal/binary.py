from __future__ import annotations

import typing as t

from .reducible import Reducer
from .base import Predicate
from .ext import HandlerExt

Acc = t.TypeVar("Acc")

L = t.TypeVar("L")
R = t.TypeVar("R")
Op = t.TypeVar("Op")

I = t.TypeVar("I")
O = t.TypeVar("O")


def and_(req: I, lhs: Predicate[I], rhs: Predicate[I]) -> bool:
    return lhs(req) and rhs(req)


def or_(req: I, lhs: Predicate[I], rhs: Predicate[I]) -> bool:
    return lhs(req) or rhs(req)


def xor(req: I, lhs: Predicate[I], rhs: Predicate[I]) -> bool:
    return bool(lhs(req) ^ rhs(req))


class Binary(HandlerExt, t.Generic[L, R, Op]):
    """Perform binary operation."""

    __slots__ = ("lhs", "rhs", "op")

    # Implemented that way because:
    # - it enables implementing short-circuit operators
    # - binary operations can share logic (reduce, for example)
    #   without duplication
    def __init__(
        self,
        lhs: L,
        rhs: R,
        op: Op,
    ) -> None:
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        # (initial @ lhs) @ rhs
        return f(f(initial, self.lhs), self.rhs)

    def __repr__(self) -> str:
        return f"Binary(lhs={self.lhs!r}, rhs={self.rhs!r}, op={self.op!r})"

    def __call__(
        self: Binary[L, R, t.Callable[[I, L, R], O]],
        req: I,
    ) -> O:
        return self.op(req, self.lhs, self.rhs)
