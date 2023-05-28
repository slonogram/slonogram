from . import FilterFn
from typing import TypeVar

from .extended_filter import InvertedFilter

T = TypeVar("T")


def identity(value: T) -> T:
    """
    identity function(`a -> a`). Useful, for example,
    when every update should be handled
    """
    return value


def not_(f: FilterFn[T]) -> FilterFn[T]:
    return InvertedFilter(f)
