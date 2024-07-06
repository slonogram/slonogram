from __future__ import annotations
import typing as t

from .handler import HandlerFn, Endpoint
from .control_flow import ControlFlow

from .then import Then
from .predicate import Predicate, PredicateFn

C = t.TypeVar("C")
B = t.TypeVar("B")

Cn = t.TypeVar("Cn")
Bn = t.TypeVar("Bn")

class Handler(HandlerFn[B, C]):
    __slots__ = ('f', )

    def __init__(self, f: HandlerFn[B, C]) -> None:
        self.f = f

    def apply(self, f: t.Callable[[Handler[B, C]], Handler[Bn, Cn]]) -> Handler[Bn, Cn]:
        return f(self)

    def predicate(self, pred: PredicateFn[C]) -> Handler[B, C]:
        return self.apply(lambda h: Handler(Predicate(pred, h.f)))

    def then(self, handler: HandlerFn[B, C]) -> Handler[B, C]:
        return self.apply(lambda h: Handler(Then(h.f, handler)))

    def __repr__(self) -> str:
        return repr(self.f)

    def __call__(self, req: C, next: Endpoint[B, C]) -> t.Awaitable[ControlFlow[B, C]]:
        return self.f(req, next)


__all__ = ["Handler"]

