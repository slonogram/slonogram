from __future__ import annotations

from types import EllipsisType
from typing import TYPE_CHECKING
from io import IOBase
from typing import (
    TypeVar,
    Any,
    ParamSpec,
)

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context, CtxExcMiddleware


from slonogram.dispatching.activation import Activation
from slonogram.session import CanCollectAttachs

T = TypeVar("T")
P = ParamSpec("P")


async def run_after_exc(
    exc: Exception,
    ctx: Context[Any],
    after: CtxExcMiddleware[Any] | None,
) -> Activation[Any]:
    if after is None:
        raise exc
    await after(ctx, exc)

    return Activation.ignored()


async def run_after_strict(
    ctx: Context[Any],
    after: CtxExcMiddleware[Any] | None,
) -> None:
    if after is not None:
        await after(ctx, None)


def prefer(val: Any | EllipsisType, otherwise: Any) -> Any:
    if val is ...:
        return otherwise
    return val


def collect_attachs_from(
    obj: CanCollectAttachs | list[Any],
    dest: dict[str, IOBase],
) -> None:
    if isinstance(obj, list):
        for item in obj:
            collect_attachs_from(item, dest)
    else:
        obj.collect_attachs(dest)
