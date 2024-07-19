import typing as t

from .base import HandlerFn, Next
from .simple import Simple
from .reducing import (
    Reducing,
    Reducer,
)

from ..control_flow import Continue, Break, ControlFlow

B = t.TypeVar("B")
C = t.TypeVar("C")
T = t.TypeVar("T")

class OneOfFn(HandlerFn[B, C], Reducing[B, C]):
    __slots__ = ('handlers', )

    def __init__(self, handlers: tuple[HandlerFn[B, C], ...]) -> None:
        self.handlers = handlers

    def reduce(self, f: Reducer[B, C, T], initial: T) -> T:
        for handler in self.handlers:
            initial = f(initial, handler)
        return initial
    
    async def __call__(self, req: C, next: Next[B, C]) -> ControlFlow[B, C]:
        for handler in self.handlers:
            result = await handler(req, next)
            if isinstance(result, Break):
                return result
            req = result.value

        return Continue(req)

    def __repr__(self) -> str:
        return f"AltFn(handlers={self.handlers!r})"

def one_of(head: HandlerFn[B, C], *tail: HandlerFn[B, C]) -> Simple[B, C]:
    return Simple(OneOfFn((head, *tail)))


__all__ = ["one_of", "OneOfFn"]


