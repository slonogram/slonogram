from typing import (
    Awaitable,
    TypeVar,
    TYPE_CHECKING,
)

from .handler import Handler
from .extended import ExtendedHandler
from .activation import Activation
from .utils import unwrap

if TYPE_CHECKING:
    from ..dispatching.context import Context

M = TypeVar("M")

class Wrap(ExtendedHandler[M]):
    __slots__ = ('inner', )

    def __init__(self, handler: Handler[M]) -> None:
        self.inner = unwrap(handler)

    def __repr__(self) -> str:
        return f'Wrap({self.inner!r})'

    def __call__(self, ctx: 'Context[M]') -> Awaitable[Activation]:
        return self.inner(ctx)

__all__ = [
    "Wrap",
]

