from types import EllipsisType
from typing import TypeVar, TypeAlias, Callable

T = TypeVar("T")

AlterFn: TypeAlias = Callable[[T], T | EllipsisType]


def prefer(val: T | EllipsisType, otherwise: T) -> T:
    if val is ...:
        return otherwise
    return val
