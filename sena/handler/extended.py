from __future__ import annotations
import typing as t

from .base import HandlerFn, Next

from ..control_flow import ControlFlow

from .then import Then
from .filtered import Filtered, Predicate

B = t.TypeVar("B")
C = t.TypeVar("C")

Bn = t.TypeVar("Bn")
Cn = t.TypeVar("Cn")

class Handler(HandlerFn[B, C]):
    def __init__(self, fn: HandlerFn[B, C]) -> None:
        self.fn = fn

    def filter(self, pred: Predicate[C]) -> Handler[B, C]:
        return self.map(lambda f: Filtered(pred, self))

    def then(self, next: HandlerFn[B, C]) -> Handler[B, C]:
        return self.map(lambda f: Then(self, next))

    def map(self, f: t.Callable[[HandlerFn[B, C]], HandlerFn[Bn, Cn]]) -> Handler[Bn, Cn]:
        return self.modify(lambda h: Handler(f(h.fn)))

    def modify(self, fn: t.Callable[[Handler[B, C]], Handler[Bn, Cn]]) -> Handler[Bn, Cn]:
        return fn(self)

    def __call__(self, req: C, next: Next[B, C], /) -> t.Awaitable[ControlFlow[B, C]]:
        return self.fn(req, next)

__all__ = ["Handler"]

