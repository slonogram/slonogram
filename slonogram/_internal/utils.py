from types import EllipsisType
from typing import TYPE_CHECKING
from io import IOBase
from typing import TypeVar, TypeAlias, Callable, Any

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context
    from slonogram.dispatching.handler import Activation
    from slonogram.middleware import ExcMiddleware

from ..session import CanCollectAttachs

T = TypeVar("T")

AlterFn: TypeAlias = Callable[[T], T | EllipsisType]


def call_alter_nullable(c: Callable[[T], T] | None, value: T) -> T:
    if c is None:
        return value
    return c(value)


def const(v: T) -> Callable[[Any], T]:
    return lambda _: v


async def run_after_exc(
    exc: Exception,
    ctx: Context[Any],
    after: ExcMiddleware[Any] | None,
) -> Activation[Any]:
    if after is None:
        raise exc
    await after(ctx, exc)

    return Activation.ignored()


async def run_after_strict(
    ctx: Context[Any],
    after: ExcMiddleware[Any] | None,
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
