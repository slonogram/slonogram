import typing as t

from ..reduction import (
    Reducer as _Reducer,
    Reducible as _Reducible,
)
from .base import HandlerFn

B = t.TypeVar("B")
C = t.TypeVar("C")
T = t.TypeVar("T")

class Reducer(_Reducer[T, HandlerFn[B, C]], t.Protocol[B, C, T]):
    def __call__(self, accum: T, handler: HandlerFn[B, C], /) -> T:
        ...

@t.runtime_checkable
class Reducible(_Reducible[HandlerFn[B, C]], t.Protocol[B, C]):
    ...


__all__ = [
    "Reducible",
    "Reducer",
]


