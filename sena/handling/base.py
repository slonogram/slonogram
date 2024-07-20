import typing as t

from ..control_flow import ControlFlow

C = t.TypeVar("C")
B = t.TypeVar("B")
Bn = t.TypeVar("Bn")
Cn = t.TypeVar("Cn")

class Next(t.Protocol[B, C]):
    def __call__(self, req: C, /) -> t.Awaitable[ControlFlow[B, C]]:
        ...

class HandlerFn(t.Protocol[B, C]):
    def __call__(self, req: C, next: Next[B, C], /) -> t.Awaitable[ControlFlow[B, C]]:
        ...

class HandlerFnFactory(t.Protocol[B, C, Bn, Cn]):
    def __call__(self, previous: HandlerFn[B, C]) -> HandlerFn[Bn, Cn]:
        ...

__all__ = ["Next", "HandlerFn", "HandlerFnFactory"]

