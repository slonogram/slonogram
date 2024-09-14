from sena import Modify
from sena.reduce import Reducer
import sena.plain as plain

import typing as t

Acc = t.TypeVar("Acc")
I = t.TypeVar("I")

def not_(req: I, rhs: plain.Predicate[I]) -> bool:
    return not rhs(req)

def identity(req: I, rhs: plain.Predicate[I]) -> bool:
    return rhs(req)


class Unary(Modify, plain.Predicate[I]):
    __slots__ = ('filter', 'op')

    def __init__(
        self,
        filter: plain.Predicate[I],
        op: t.Callable[[I, plain.Predicate[I]], bool],
    ) -> None:
        self.filter = filter
        self.op = op

    @classmethod
    def id(cls, filter: plain.Predicate[I]) -> t.Self:
        return cls(filter, identity)

    @classmethod
    def not_(cls, filter: plain.Predicate[I]) -> t.Self:
        return cls(filter, not_)

    def __repr__(self) -> str:
        return f"Unary(filter={self.filter!r}, op={self.op!r})"

    def reduce(self, f: Reducer[Acc], initial: Acc) -> Acc:
        return f(initial, self.filter)

    def __call__(self, req: I) -> bool:
        return self.op(req, self.filter)


__all__ = ["Unary"]

