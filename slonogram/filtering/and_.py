from typing import TypeVar

from ..types.context import Context

from .base import Filter
from .extended import ExtendedFilter
from .utils import unwrap_predicate

M = TypeVar("M")


class And(ExtendedFilter[M]):
    __slots__ = ("lhs", "rhs")

    def __init__(self, lhs: Filter[M], rhs: Filter[M]) -> None:
        self.lhs = unwrap_predicate(lhs)
        self.rhs = unwrap_predicate(rhs)

    def __repr__(self) -> str:
        return f"And({self.lhs!r}, {self.rhs!r})"

    def __call__(self, ctx: Context[M]) -> bool:
        if self.lhs(ctx):
            return self.rhs(ctx)
        return False


__all__ = ["And"]
