from typing import TypeVar

from ..handling.activation import Activation
from ..handling.handler import Handler
from ..dispatching.context import Context
from .base import Middlewared

M = TypeVar("M")

class NeverActivate(Middlewared[M]):
    __slots__ = ('handler', )

    def __init__(self, handler: Handler[M]) -> None:
        self.handler = handler
    
    def __repr__(self) -> str:
        return f"NeverActivate({self.handler})"
    
    async def __call__(self, ctx: Context[M], /) -> Activation:
        _ = await self.handler(ctx)

        return Activation.STALLED


__all__ = ["NeverActivate"]
