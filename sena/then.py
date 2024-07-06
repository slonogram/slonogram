import typing as t

from .handler import HandlerFn, Endpoint
from .control_flow import ControlFlow

C = t.TypeVar("C")
B = t.TypeVar("B")


class Then(HandlerFn[B, C]):
    __slots__ = ('current', 'next')

    def __init__(self, current: HandlerFn[B, C], next: HandlerFn[B, C]) -> None:
        self.current = current
        self.next = next

    def __call__(self, req: C, next: Endpoint[B, C]) -> t.Awaitable[ControlFlow[B, C]]:
        return self.current(req, lambda r: self.next(r, next))

    def __repr__(self) -> str:
        return f"{self.current!r}.then({self.next!r})"

__all__ = ["Then"]

