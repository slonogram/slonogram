from typing import Callable, TypeAlias, TypeVar, Awaitable
from ..dp.context import Context

T = TypeVar("T")

FilterFn: TypeAlias = Callable[[Context[T]], Awaitable[bool]]
