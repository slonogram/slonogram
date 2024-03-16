from typing import (
    overload,
    Literal,
    Callable,
    TypeAlias,
    TypeVar,
)
from functools import wraps

from .base import Filter, ExtendedFilter
from ..dispatching.context import Context
from .predicate import Predicate

M = TypeVar("M")
Unlifted: TypeAlias = Callable[[M], bool]


@overload
def lift(f: Unlifted[M], extend: Literal[True]) -> ExtendedFilter[M]:
    ...


@overload
def lift(f: Unlifted[M], extend: Literal[False]) -> Filter[M]:
    ...


def lift(f: Unlifted[M], extend: bool = True) -> ExtendedFilter[M] | Filter[M]:
    @wraps(f)
    def lifted(ctx: Context[M]) -> bool:
        return f(ctx.model)

    if extend:
        return Predicate(lifted)
    return lifted


__all__ = ["lift"]
