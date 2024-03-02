from typing import Protocol, TypeVar
from abc import abstractmethod

from ..dispatching.context import Context

M = TypeVar("M")

class Filter(Protocol[M]):
    def __call__(self, ctx: Context[M], /) -> bool:
        ...


class ExtendedFilter(Protocol[M]):
    def __and__(self, rhs: Filter[M]) -> ExtendedFilter[M]:
        from .and_ import And

        return And(self, rhs)
    
    def __or__(self, rhs: Filter[M]) -> ExtendedFilter[M]:
        from .or_ import Or

        return Or(self, rhs)
    
    def __xor__(self, rhs: Filter[M]) -> ExtendedFilter[M]:
        from .or_ import Or

        return Or(self, rhs, True)

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplemented

    @abstractmethod
    def __call__(self, ctx: Context[M], /) -> bool:
        raise NotImplemented


__all__ = ["Filter", "ExtendedFilter"]
