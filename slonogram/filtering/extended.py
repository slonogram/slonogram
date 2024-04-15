from typing import TypeVar, Protocol

from .base import Filter
from ..types.context import Context

M = TypeVar("M")

class ExtendedFilter(Filter[M], Protocol[M]):
    __extended_filter__: bool = True

    def __invert__(self) -> "ExtendedFilter[M]":
        from .not_ import Not

        return Not(self)

    def __and__(self, rhs: Filter[M]) -> "ExtendedFilter[M]":
        from .and_ import And

        return And(self, rhs)

    def __or__(self, rhs: Filter[M]) -> "ExtendedFilter[M]":
        from .or_ import Or

        return Or(self, rhs)

    def __xor__(self, rhs: Filter[M]) -> "ExtendedFilter[M]":
        from .or_ import Or

        return Or(self, rhs, True)

    def __repr__(self) -> str:
        ...

    def __call__(self, ctx: 'Context[M]', /) -> bool:
        ...

__all__ = ["ExtendedFilter"]


