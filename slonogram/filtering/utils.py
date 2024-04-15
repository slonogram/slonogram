from typing import TypeVar, TypeGuard

from .base import Filter
from .extended import ExtendedFilter

M = TypeVar("M")

def is_extended_filter(filter: Filter[M]) -> TypeGuard[ExtendedFilter[M]]:
    return getattr(filter, '__extended_filter__', False)

def unwrap_predicate(filter: Filter[M]) -> Filter[M]:
    from .predicate import Predicate
    while isinstance(filter, Predicate):
        filter = filter.function

    return filter

__all__ = ["unwrap_predicate", "is_extended_filter"]

