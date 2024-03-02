from typing import Protocol, TypeVar, Awaitable

from .activation import Activation
from ..dispatching.context import Context

M = TypeVar("M")


class Handler(Protocol[M]):
    def __call__(self, ctx: Context[M], /) -> Awaitable[Activation]:
        ...

__all__ = ["Handler"]
