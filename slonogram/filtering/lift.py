from typing import (
    overload,
    Literal,
    Callable,
    TypeAlias,
    TypeVar,
)

from .base import Filter, ExtendedFilter
from .predicate import Predicate
from ..dispatching.context import Context

M = TypeVar("M")
Unlifted: TypeAlias = Callable[[M], bool]

@overload
def lift(f: Callable[[M], bool], extend: Literal[True]) -> ExtendedFilter[M]:
    ...

@overload
def lift(f: Callable[[M], bool], extend: Literal[False]) -> Filter[M]:
    ...

def lift(f: Callable[[M], bool], extend: bool = True) -> ExtendedFilter[M] | Filter[M]:
    new_f: Filter[M] = lambda ctx: f(ctx.model)

    if extend:
        return Predicate(new_f)
    return new_f

__all__ = ["lift"]
