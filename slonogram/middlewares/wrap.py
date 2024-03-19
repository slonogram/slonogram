from typing import TypeVar, Awaitable, TYPE_CHECKING, Protocol
from functools import wraps

if TYPE_CHECKING:
    from ..dispatching.context import Context
    from ..handling.handler import Handler
    from ..handling.activation import Activation

from .base import Middlewared
from .utils import unwrap

M = TypeVar("M")
class HandlerCompatible(Protocol[M]):
    def __call__(self, ctx: 'Context[M]') -> Awaitable[None]:
        ...



class Wrap(Middlewared[M]):
    __slots__ = ("function",)

    def __init__(self, function: 'Handler[M]') -> None:
        self.function = unwrap(function)

    def __repr__(self) -> str:
        return f"Wrap({self.function!r})"

    def __call__(self, ctx: 'Context[M]') -> Awaitable['Activation']:
        return self.function(ctx)


def activate(compatible: HandlerCompatible[M]) -> Wrap[M]:
    from ..handling.activation import Activation

    @wraps(compatible)
    async def wrapper(ctx: "Context[M]") -> "Activation":
        await compatible(ctx)
        return Activation(wrapper)

    return Wrap(wrapper)

__all__ = [
    "Wrap",
    "activate",
    "HandlerCompatible",
]
