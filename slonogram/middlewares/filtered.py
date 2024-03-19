from typing import TypeVar

from ..filtering.base import Filter
from ..dispatching.context import Context
from ..handling.activation import Activation
from ..handling.handler import Handler

from .utils import unwrap
from .base import Middlewared


M = TypeVar("M")


class Filtered(Middlewared[M]):
    __slots__ = ("filter", "handler")

    def __init__(self, handler: Handler[M], filter: Filter[M]) -> None:
        self.filter = filter
        self.handler = unwrap(handler)

    def __repr__(self) -> str:
        return f"Filtered({self.handler}, filter={self.filter})"

    async def __call__(self, ctx: Context[M], /) -> Activation:
        if self.filter(ctx):
            return await self.handler(ctx)
        return Activation.stalled()


__all__ = ["Filtered"]
