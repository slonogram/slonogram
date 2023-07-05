from __future__ import annotations
from ..dispatching.context import Context
from typing import (
    Protocol,
    Generic,
    TypeVar,
    TypeAlias,
    Callable,
    Awaitable,
)

T = TypeVar("T")
D = TypeVar("D")

NextMiddleware: TypeAlias = Callable[[Context[D, T]], Awaitable[None]]


class Middleware(Generic[D, T], Protocol):
    async def __call__(
        self, /, call_next: NextMiddleware[D, T], context: Context[D, T]
    ) -> None:
        ...
