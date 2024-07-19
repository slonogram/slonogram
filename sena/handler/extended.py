from __future__ import annotations
import typing as t

from abc import abstractmethod

from .base import HandlerFn, Next
from .reducing import Reducing

from ..endpoint.base import EndpointFn
from ..control_flow import ControlFlow

from .then import Then
from .catch import Catch, ExceptionHandler
from .filtered import Filtered, Predicate
from .connected import Connected

B = t.TypeVar("B")
C = t.TypeVar("C")

Bn = t.TypeVar("Bn")
Cn = t.TypeVar("Cn")

H = t.TypeVar("H")


# TODO: see `Handler.modify`
class Mapper(t.Protocol[B, C]):
    def __call__(self, input: HandlerFn[B, C], /) -> HandlerFn[B, C]:
        ...

class Modifier(t.Protocol[H]):
    def __call__(self, input: H) -> H:
        ...

@t.runtime_checkable
class Handler(HandlerFn[B, C], Reducing[B, C], t.Protocol[B, C]):
    # TODO: see `modify`, but now there's a type erasure
    @abstractmethod
    def map(self, f: Mapper[B, C]) -> Handler[B, C]:
        raise NotImplementedError

    @abstractmethod
    def __call__(self, req: C, next: Next[B, C], /) -> t.Awaitable[ControlFlow[B, C]]:
        raise NotImplementedError

    # Default sugar

    # TODO: this is quite constrained, since `modify` cannot change type of the `Handler`.
    # To be more flexible, python should support HKT.
    def modify(self, fn: Modifier[t.Self]) -> t.Self:
        return fn(self)

    def endpoint(self, endpoint: EndpointFn[B, C]) -> Next[B, C]:
        return Connected.from_endpoint(self, endpoint)

    def connect(self, next: Next[B, C]) -> Next[B, C]:
        return Connected(self, next)

    def filter(self, pred: Predicate[C]) -> Handler[B, C]:
        return self.map(Filtered.factory(pred))

    def catch(self, handler: ExceptionHandler[B, C]) -> Handler[B, C]:
        return self.map(Catch.factory(handler))

    def then(self, next: HandlerFn[B, C]) -> Handler[B, C]:
        return self.map(Then.factory(next))

__all__ = ["Handler"]

