from typing import TypeVar, Awaitable, Callable, TypeAlias
from functools import wraps

from ..dispatching.context import Context
from ..handling.handler import Handler
from ..handling.activation import Activation
from .base import Middlewared

M = TypeVar("M")
HandlerCompatible: TypeAlias = Callable[[Context[M]], Awaitable[None]]

class Wrap(Middlewared[M]):
    __slots__ = ('function', )

    def __init__(self, function: Handler[M]) -> None:
        self.function = function
    
    def __repr__(self) -> str:
        return f"Wrap({self.function!r})"
    
    def __call__(self, ctx: Context[M]) -> Awaitable[Activation]:
        return self.function(ctx)


def activate(compatible: HandlerCompatible[M]) -> Wrap:
    @wraps(compatible)
    async def wrapper(ctx: Context[M]) -> Activation:
        return Activation.ACTIVATED

    return Wrap(wrapper)


__all__ = [
    "Wrap",
    "activate",
    "HandlerCompatible",
]
