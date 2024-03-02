from typing import TypeVar, Awaitable

from ..dispatching.context import Context
from ..handling.handler import Handler
from ..handling.activation import Activation
from .base import Middlewared

M = TypeVar("M")

class Wrap(Middlewared[M]):
    __slots__ = ('function', )

    def __init__(self, function: Handler[M]) -> None:
        self.function = function
    
    def __repr__(self) -> str:
        return f"Wrap({self.function!r})"
    
    def __call__(self, ctx: Context[M]) -> Awaitable[Activation]:
        return self.function(ctx)


__all__ = ["Wrap"]
