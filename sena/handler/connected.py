import typing as t

from .base import HandlerFn, Next
from .reducing import (
    Reducer,
    Reducing,
)

from ..control_flow import ControlFlow, Break
from ..endpoint.base import EndpointFn

T = t.TypeVar("T")
B = t.TypeVar("B")
C = t.TypeVar("C")

class NextEndpoint(Next[B, C]):
    __slots__ = ('inner', )

    def __init__(self, inner: EndpointFn[B, C]) -> None:
        self.inner = inner

    def __repr__(self) -> str:
        return repr(self.inner)

    async def __call__(self, req: C) -> ControlFlow[B, C]:
        return Break(await self.inner(req))

class Connected(Next[B, C], Reducing[B, C]):
    __slots__ = ('handler', 'next')

    def __init__(self, handler: HandlerFn[B, C], next: Next[B, C]) -> None:
        self.handler = handler
        self.next = next

    def reduce(self, f: Reducer[B, C, T], initial: T) -> T:
        return f(initial, self.handler)

    @classmethod
    def from_endpoint(cls, handler: HandlerFn[B, C], endpoint: EndpointFn[B, C]) -> t.Self:
        return cls(handler, NextEndpoint(endpoint))

    def __repr__(self) -> str:
        return f"Connected(handler={self.handler!r}, next={self.next!r})"

    def __call__(self, req: C) -> t.Awaitable[ControlFlow[B, C]]:
        return self.handler(req, self.next)


__all__ = ["Connected", "NextEndpoint"]


