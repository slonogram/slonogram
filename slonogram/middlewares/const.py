from typing import TypeVar, Callable, TypeAlias, Awaitable

from ..handling.activation import Activation
from ..handling.handler import Handler
from ..dispatching.context import Context
from .base import Middlewared

M = TypeVar("M")

class Const(Middlewared[M]):
    __slots__ = ('handler', 'activation')

    def __init__(self, handler: Handler[M], activation: Activation) -> None:
        self.handler = handler
        self.activation = activation
    
    def __repr__(self) -> str:
        return f"Const({self.handler}, activation={self.activation})"
    
    async def __call__(self, ctx: Context[M], /) -> Activation:
        _ = await self.handler(ctx)
        return self.activation


__all__ = ["Const"]
