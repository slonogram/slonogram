import typing as t

from .base import HandlerFn, Next
from .extended import Handler, Mapper
from .reducible import Reducer

from .simple import Simple

from ..control_flow import Continue, Break, ControlFlow

B = t.TypeVar("B")
C = t.TypeVar("C")
T = t.TypeVar("T")

class OneOf(Handler[B, C]):
    __slots__ = ('handlers', )

    def __init__(self, *handlers: HandlerFn[B, C]) -> None:
        self.handlers = handlers

    def reduce(self, f: Reducer[B, C, T], initial: T) -> T:
        for handler in self.handlers:
            initial = f(initial, handler)
        return initial

    def map(self, f: Mapper[B, C]) -> Handler[B, C]:
        return Simple(f(self))
    
    async def __call__(self, req: C, next: Next[B, C]) -> ControlFlow[B, C]:
        for handler in self.handlers:
            result = await handler(req, next)
            if isinstance(result, Break):
                return result
            req = result.value

        return Continue(req)

    def __repr__(self) -> str:
        return f"OneOf(handlers={self.handlers!r})"

__all__ = ["OneOf"]


