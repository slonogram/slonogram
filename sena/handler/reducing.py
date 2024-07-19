import typing as t

from .base import HandlerFn

B = t.TypeVar("B")
C = t.TypeVar("C")
T = t.TypeVar("T")

class Reducer(t.Protocol[B, C, T]):
    def __call__(self, accum: T, handler: HandlerFn[B, C], /) -> T:
        ...

@t.runtime_checkable
class Reducing(t.Protocol[B, C]):
    def reduce(self, f: Reducer[B, C, T], initial: T, /) -> T:
        ...

def try_reduce(val: HandlerFn[B, C], f: Reducer[B, C, T], initial: T) -> T:
    if isinstance(val, Reducing):
        return val.reduce(f, initial)
    return f(initial, val)


__all__ = [
    "Reducing",
    "Reducer",
    "try_reduce",
]


