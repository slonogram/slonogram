from typing import (
    TypeVar,
    Awaitable,
    Protocol,
    TYPE_CHECKING,
)
from functools import wraps
from .activation import Activation
if TYPE_CHECKING:
    from ..dispatching.context import Context
    from ..handling.handler import Handler

M = TypeVar("M")
Ret = TypeVar("Ret", bool, None, Activation, covariant=True)


class CompatibleHandler(Protocol[M, Ret]):
    def __call__(self, ctx: 'Context[M]', /) -> Awaitable[Ret]:
        ...

def handler_from_compatible(
    compat: CompatibleHandler[M, Ret],
    activated: Activation | None = None,
) -> Handler[M]:
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

    return inner

__all__ = [
    "CompatibleHandler",
    "handler_from_compatible",
]

