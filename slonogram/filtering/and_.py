from typing import TypeVar

from ..dispatching.context import Context
from .base import ExtendedFilter, Filter

M = TypeVar("M")


class And(ExtendedFilter[M]):
    __slots__ = ("lhs", "rhs")

    def __init__(self, lhs: Filter[M], rhs: Filter[M]) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self) -> str:
        return f"And({self.lhs!r}, {self.rhs!r})"

    def __call__(self, ctx: Context[M]) -> bool:
        if self.lhs(ctx):
            return self.rhs(ctx)
        return False


__all__ = ["And"]
