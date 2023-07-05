from typing import Callable, TypeAlias, TypeVar, Awaitable
from ..dispatching.context import Context

T = TypeVar("T")
D = TypeVar("D")

FilterFn: TypeAlias = Callable[[Context[D, T]], Awaitable[bool]]
