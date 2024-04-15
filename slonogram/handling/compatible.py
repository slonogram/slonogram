from typing import (
    TypeVar,
    Awaitable,
    Protocol,
)
from functools import wraps

from .activation import Activation
from .extended import ExtendedHandler
from .utils import is_extended_handler

from ..types.context import Context

M = TypeVar("M")
Ret = TypeVar("Ret", bool, None, Activation, covariant=True)


class CompatibleHandler(Protocol[M, Ret]):
    def __call__(self, ctx: 'Context[M]', /) -> Awaitable[Ret]:
        ...

def handler_from_compatible(
    compat: CompatibleHandler[M, Ret],
    activated: Activation | None = None,
) -> 'ExtendedHandler[M]':
    from ..handling.wrap import Wrap

    if is_extended_handler(compat):  # type: ignore
        return compat

    @wraps(compat)
    async def inner(ctx: 'Context[M]') -> Activation:
        # mypy is stupid as fuck
        # fuck you, mypy
        result = await compat(ctx)  # type: ignore
        if result is None:
            return activated  # type: ignore
        elif isinstance(result, bool):
            return activated if result else Activation.stalled()  # type: ignore

        return result
    if activated is None:
        activated = Activation(inner)

    return Wrap(inner)

__all__ = [
    "CompatibleHandler",
    "handler_from_compatible",
]

