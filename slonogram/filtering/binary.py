import typing as t
from functools import partial

from sena import Modify
import sena.plain as plain
from sena.reduce import Reducer


Acc = t.TypeVar("Acc")
I = t.TypeVar("I")

def and_(req: I, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> bool:
    return lhs(req) and rhs(req)

def or_(req: I, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> bool:
    return lhs(req) or rhs(req)

def xor(req: I, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> bool:
    return bool(lhs(req) ^ rhs(req))


class Binary(Modify, plain.Predicate[I]):
    """Perform binary operation.
    """
    __slots__ = ('lhs', 'rhs', 'op')

    # Implemented that way because:
    # - it allows implementing short-circuit operators
    # - binary operations can share logic (reduce, for example)
    #   without duplication
    def __init__(
        self,
        lhs: plain.Predicate[I],
        rhs: plain.Predicate[I],
        op: t.Callable[[I, plain.Predicate[I], plain.Predicate[I]], bool],
    ) -> None:
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    @classmethod
    def and_(cls, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> t.Self:
        return cls(lhs, rhs, and_)

    @classmethod
    def or_(cls, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> t.Self:
        return cls(lhs, rhs, or_)

    @classmethod
    def xor(cls, lhs: plain.Predicate[I], rhs: plain.Predicate[I]) -> t.Self:
        return cls(lhs, rhs, xor)

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        # (initial @ lhs) @ rhs
        return f(f(initial, self.lhs), self.rhs)

    def __repr__(self) -> str:
        return f"Binary(lhs={self.lhs!r}, rhs={self.rhs!r}, op={self.op!r})"

    def __call__(self, req: I) -> bool:
        return self.op(req, self.lhs, self.rhs)

__all__ = [
    "Binary",
    "and_",
    "or_",
    "xor",
]


