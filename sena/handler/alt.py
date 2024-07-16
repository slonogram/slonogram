import typing as t

from .base import HandlerFn, Next
from .simple import Simple

from ..control_flow import Continue, Break, ControlFlow

B = t.TypeVar("B")
C = t.TypeVar("C")

class AltFn(HandlerFn[B, C]):
    __slots__ = ('handlers', )

    def __init__(self, handlers: tuple[HandlerFn[B, C], ...]) -> None:
        self.handlers = handlers

    
    async def __call__(self, req: C, next: Next[B, C]) -> ControlFlow[B, C]:
        for handler in self.handlers:
            result = await handler(req, next)
            if isinstance(result, Break):
                return result
            req = result.value

        return Continue(req)

    def __repr__(self) -> str:
        return f"AltFn(handlers={self.handlers!r})"

def alt(head: HandlerFn[B, C], *tail: HandlerFn[B, C]) -> Simple[B, C]:
    return Simple(AltFn((head, *tail)))


__all__ = ["alt", "AltFn"]


