from typing import (
    TypeVar,
)

from .auto_collect import auto_collect
from .extended import ExtendedHandler
from .handler import Handler
from .activation import Activation
from .utils import unwrap_handler

from ..types.context import Context

M = TypeVar("M")

class Const(ExtendedHandler[M]):
    __slots__ = ('activation', 'handler')

    def __init__(self, activate: bool, handler: Handler[M]) -> None:
        handler = unwrap_handler(handler)
        self.handler = handler

        if activate:
            self.activation = Activation(handler)
        else:
            self.activation = Activation.stalled()

    @auto_collect
    def collect_interests(self):
        return (self.handler,)

    def __repr__(self) -> str:
        status = 'stalled' if self.activation.handler is None else 'activated'
        return f"Const({status}, of={self.handler!r})"

    async def __call__(self, ctx: Context[M]) -> Activation:
        await self.handler(ctx)
        return self.activation

__all__ = ["Const"]

