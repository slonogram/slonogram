from __future__ import annotations
from ..dp.context import Context
from typing import Protocol, Generic, TypeVar

T = TypeVar("T")
D = TypeVar("D")


class Middleware(Generic[D, T], Protocol):
    async def __call__(self, /, context: Context[D, T]) -> None:
        ...
