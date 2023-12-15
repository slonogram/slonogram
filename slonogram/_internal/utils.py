from types import EllipsisType
from typing import TypeVar, TypeAlias, Callable, Any

T = TypeVar("T")

AlterFn: TypeAlias = Callable[[T], T | EllipsisType]


def prefer(val: Any | EllipsisType, otherwise: Any) -> Any:
    if val is ...:
        return otherwise
    return val
