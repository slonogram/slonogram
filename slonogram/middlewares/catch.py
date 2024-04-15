from typing import (
    TypeVar,
    Generic,
)

from ..handling.follows import CurrentMiddleware
from ..handling.handler import Handler
from ..handling.activation import Activation

from ..types.context import Context
from ..types.caught_exception import CaughtException

M = TypeVar("M")
E = TypeVar("E", bound=Exception)

class Catch(Generic[M, E], CurrentMiddleware[M]):
    __slots__ = ('exception', 'handler')

    def __init__(self, exc: type[E], handler: Handler[CaughtException[M, E]]) -> None:
        self.exception = exc
        self.handler = handler

    def __repr__(self) -> str:
        return f'Catch(exc={self.exception!r}, handler={self.handler!r})'

    async def __call__(self, ctx: 'Context[M]', next: Handler[M]) -> Activation:
        try:
            return await next(ctx)
        except self.exception as exc:
            caught = CaughtException(ctx.model, exc, next)
            return await self.handler(ctx.with_model(caught))


__all__ = ["Catch"]

