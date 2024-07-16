from __future__ import annotations

import typing as t

from .base import EndpointFn, SeqEndpointFn, EndpointFnFactory
from .after import After

B_co = t.TypeVar("B_co", covariant=True)
C_contra = t.TypeVar("C_contra", contravariant=True)

Bn = t.TypeVar("Bn")
Cn = t.TypeVar("Cn")

class Endpoint(EndpointFn[B_co, C_contra]):
    __slots__ = ('fn', )

    def __init__(self, fn: EndpointFn[B_co, C_contra]) -> None:
        self.fn = fn

    def after(self, current: SeqEndpointFn[B_co, C_contra]) -> Endpoint[B_co, C_contra]:
        return self.map(lambda e: After(current, self))

    def map(self, f: EndpointFnFactory[B_co, C_contra, Bn, Cn]) -> Endpoint[Bn, Cn]:
        return Endpoint(f(self.fn))

    def modify(self, f: t.Callable[[Endpoint[B_co, C_contra]], Endpoint[Bn, Cn]]) -> Endpoint[Bn, Cn]:
        return f(self)

    def __call__(self, req: C_contra, /) -> t.Awaitable[B_co]:
        return self.fn(req)

    def __repr__(self) -> str:
        return repr(self.fn)


__all__ = ["Endpoint"]


