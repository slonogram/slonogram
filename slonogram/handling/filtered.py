from typing import TypeVar, Awaitable

from .._internal.utils import stalled
from .auto_collect import auto_collect
from .extended import ExtendedHandler
from .handler import Handler
from .activation import Activation
from .utils import unwrap_handler

from ..reflect.named import get_name
from ..types.context import Context
from ..filtering.base import Filter


M = TypeVar("M")

class Filtered(ExtendedHandler[M]):
    __slots__ = ('filter', 'handler')

    def __init__(self, handler: Handler[M], filter: Filter[M]) -> None:
        self.filter = filter
        self.handler = unwrap_handler(handler)
        self.__name__ = get_name(handler, '')

    def __repr__(self) -> str:
        return f"Filtered({self.handler!r}, filter={self.filter!r})"

    @auto_collect
    def collect_interests(self):
        return (self.handler,)

    def __call__(self, ctx: 'Context[M]') -> Awaitable[Activation]:
        if self.filter(ctx):
            return self.handler(ctx)
        return stalled()


__all__ = ["Filtered"]


