from typing import TypeVar

from ..dispatching.context import Context
from .base import ExtendedFilter, Filter

M = TypeVar("M")


class Predicate(ExtendedFilter[M]):
    __slots__ = ("function",)

    def __init__(self, function: Filter[M]) -> None:
        self.function = function

    def __call__(self, ctx: Context[M]) -> bool:
        return self.function(ctx)

    def __repr__(self) -> str:
        return f"Predicate({self.function})"


__all__ = ["Predicate"]
