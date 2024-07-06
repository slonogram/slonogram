import typing as t

from .filter import FilterFn
from ..types.ctx import Ctx

D = t.TypeVar("D")

class Or(FilterFn[D]):
    __slots__ = ('lhs', 'rhs', 'exclusive')

    def __init__(self, lhs: FilterFn[D], rhs: FilterFn[D], exclusive: bool = False) -> None:
        self.lhs = lhs
        self.rhs = rhs
        self.exclusive = exclusive

    def __call__(self, ctx: Ctx[D]) -> bool:
        if self.exclusive:
            return bool(self.lhs(ctx) ^ self.rhs(ctx))
        return self.lhs(ctx) or self.rhs(ctx)


__all__ = ["Or"]
