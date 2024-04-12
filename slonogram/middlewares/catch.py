from typing import (
    TypeVar,
    Iterable,
    TypeVarTuple,
    Generic,
    TYPE_CHECKING,
)

from ..handling.follows import CurrentMiddleware
from ..handling.extended import ExtendedHandler
from ..handling.handler import Handler
from ..handling.activation import Activation
if TYPE_CHECKING:
    from ..dispatching.context import Context

from ..types.caught_exception import CaughtException

M = TypeVar("M")
E = TypeVar("E", bound=Exception)

class Catch(Generic[M, E], CurrentMiddleware[M]):
    __slots__ = ('exception', 'handler')

    def __init__(self, exc: type[E], handler: Handler[CaughtException]) -> None:
        self.exception = exc
        self.handler = handler

    def __repr__(self) -> str:
        return f'Catch(exc={self.exception!r}, handler={self.handler!r})'

    async def __call__(self, ctx: 'Context[M]', next: Handler[M]) -> Activation:
        try:
            return await next(ctx)
        except self.exception as exc:
            caught = CaughtException(ctx.model, exc)
            return await self.handler(ctx.with_model(caught))


__all__ = ["Catch"]

