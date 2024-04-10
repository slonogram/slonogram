from typing import TypeVar, Awaitable, TYPE_CHECKING

from .._internal.utils import stalled
from .extended import ExtendedHandler
from .handler import Handler
from .activation import Activation
from .utils import unwrap

if TYPE_CHECKING:
    from ..dispatching.context import Context
    from ..filtering.base import Filter

M = TypeVar("M")

class Filtered(ExtendedHandler[M]):
    __slots__ = ('filter', 'handler')

    def __init__(self, handler: Handler[M], filter: 'Filter[M]') -> None:
        self.filter = filter
        self.handler = unwrap(handler)

    def __repr__(self) -> str:
        return f"Filtered({self.handler!r}, filter={self.filter!r})"

    def __call__(self, ctx: 'Context[M]') -> Awaitable[Activation]:
        if self.filter(ctx):
            return self.handler(ctx)
        return stalled()


__all__ = ["Filtered"]


