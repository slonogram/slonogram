from __future__ import annotations

import typing as t
import abc

from .reducible import Reducible
from .base import (
    EndpointFn,
    SeqEndpointFn,
)
from .after import After

B = t.TypeVar("B")
C = t.TypeVar("C")
S = t.TypeVar("S")

class Mapper(t.Protocol[B, C]):
    def __call__(self, endpoint: EndpointFn[B, C], /) -> EndpointFn[B, C]:
        ...

class Modifier(t.Protocol[S]):
    def __call__(self, value: S, /) -> S:
        ...


class Endpoint(EndpointFn[B, C], Reducible[B, C], t.Protocol[B, C]):
    __slots__ = ('fn', )

    @abc.abstractmethod
    def map(self, f: Mapper[B, C]) -> Endpoint[B, C]:
        raise NotImplementedError

    @abc.abstractmethod
    def __call__(self, req: C, /) -> t.Awaitable[B]:
        raise NotImplementedError

    def after(self, current: SeqEndpointFn[B, C]) -> Endpoint[B, C]:
        return self.map(After.factory(current))

    def modify(self, f: Modifier[t.Self]) -> t.Self:
        return f(self)


__all__ = ["Endpoint"]


