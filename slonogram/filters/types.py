from typing import Callable, TypeAlias, TypeVar, Awaitable
from ..dp.context import Context

T = TypeVar("T")
D = TypeVar("D")


class Unit:
    __slots__ = ()


FilterFn: TypeAlias = Callable[[Context[D, T]], Awaitable[bool]]
