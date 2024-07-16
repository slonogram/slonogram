import typing as t

from .base import HandlerFn, Next, HandlerFnFactory

from ..control_flow import ControlFlow
from ..utils import extract_handler

C = t.TypeVar("C")
B = t.TypeVar("B")


class Then(HandlerFn[B, C]):
    __slots__ = ('current', 'next')

    def __init__(self, current: HandlerFn[B, C], next: HandlerFn[B, C]) -> None:
        self.current = extract_handler(current)
        self.next = extract_handler(next)

    @classmethod
    def factory(cls, current: HandlerFn[B, C]) -> HandlerFnFactory[B, C, B, C]:
        return lambda next: cls(current, next)

    def __call__(self, req: C, next: Next[B, C]) -> t.Awaitable[ControlFlow[B, C]]:
        return self.current(req, lambda r: self.next(r, next))

    def __repr__(self) -> str:
        return f"{self.current!r}.then({self.next!r})"

__all__ = ["Then"]

