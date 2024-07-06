import typing as t

from .control_flow import ControlFlow

C = t.TypeVar("C")
B = t.TypeVar("B")

class Endpoint(t.Protocol[B, C]):
    def __call__(self, req: C, /) -> t.Awaitable[ControlFlow[B, C]]:
        ...

class HandlerFn(t.Protocol[B, C]):
    def __call__(self, req: C, next: Endpoint[B, C], /) -> t.Awaitable[ControlFlow[B, C]]:
        ...

__all__ = ["Endpoint", "HandlerFn"]

