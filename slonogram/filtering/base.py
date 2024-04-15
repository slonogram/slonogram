from typing import Protocol, TypeVar

from ..types.context import Context

M = TypeVar("M")


class Filter(Protocol[M]):
    def __call__(self, ctx: Context[M], /) -> bool:
        ...

__all__ = ["Filter"]
