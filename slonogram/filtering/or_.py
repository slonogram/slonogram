from typing import TypeVar

from ..dispatching.context import Context
from .base import ExtendedFilter, Filter

M = TypeVar("M")


class Or(ExtendedFilter[M]):
    __slots__ = ('exclusive', 'lhs', 'rhs')

    def __init__(
        self,
        lhs: Filter[M],
        rhs: Filter[M],
        exclusive: bool = False,
    ) -> None:
        self.lhs = lhs
        self.rhs = rhs

        self.exclusive = exclusive
    
    def __repr__(self) -> str:
        return f"Or(exclusive={self.exclusive!r}, lhs={self.lhs!r}, rhs={self.rhs!r})"
    
    def __call__(self, ctx: Context[M]) -> bool:
        if self.exclusive:
            return self.lhs(ctx) ^ self.rhs(ctx)

        if self.lhs(ctx):
            return True
        return self.rhs(ctx)

__all__ = ["Or"]
