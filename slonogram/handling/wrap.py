from typing import (
    Awaitable,
    TypeVar,
)

from .handler import Handler
from .extended import ExtendedHandler
from .activation import Activation
from .utils import unwrap_handler

from ..reflect.named import get_name
from ..types.context import Context

from .auto_collect import auto_collect

M = TypeVar("M")

class Wrap(ExtendedHandler[M]):
    __slots__ = ('inner', )

    def __init__(self, handler: Handler[M]) -> None:
        self.inner = unwrap_handler(handler)
        self.__name__ = get_name(handler, '')

    def __repr__(self) -> str:
        return f'Wrap({self.inner!r})'

    def __call__(self, ctx: 'Context[M]') -> Awaitable[Activation]:
        return self.inner(ctx)

    @auto_collect
    def collect_interests(self):
        return (self.inner,)

__all__ = [
    "Wrap",
]

