from __future__ import annotations

import typing as t

from .extended import Endpoint, Mapper
from .base import EndpointFn

from .reducible import Reducer

B = t.TypeVar("B")
C = t.TypeVar("C")
T = t.TypeVar("T")

P = t.ParamSpec("P")

class Simple(Endpoint[B, C]):
    __slots__ = ('inner', )

    def __init__(self, inner: EndpointFn[B, C]) -> None:
        self.inner = inner

    def map(self, f: Mapper[B, C]) -> Simple[B, C]:
        return Simple(f(self.inner))

    def reduce(self, f: Reducer[B, C, T], initial: T) -> T:
        return f(initial, self.inner)

    def __repr__(self) -> str:
        return repr(self.inner)

    def __call__(self, req: C) -> t.Awaitable[B]:
        return self.inner(req)

__all__ = ["Simple"]

