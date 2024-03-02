from typing import TypeVar

from ..dispatching.context import Context
from .base import ExtendedFilter, Filter

M = TypeVar("M")


class Not(ExtendedFilter[M]):
    __slots__ = ('filter', )

    def __init__(self, filter: Filter[M]) -> None:
        self.filter = filter
    
    def __repr__(self) -> str:
        return f"Not({self.filter})"
    
    def __call__(self, ctx: Context[M], /) -> bool:
        return not self.filter(ctx)


__all__ = ["Not"]
