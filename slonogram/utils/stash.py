import typing as t

from ..types.stash import Stash
from ..types.ctx import Ctx

if t.TYPE_CHECKING:
    from ..handling.handler import HandlerFn, Next
    from ..handling.control_flow import ControlFlow

D = t.TypeVar("D")


async def ward_stash(handler: 'HandlerFn[D]', ctx: 'Ctx[D]', next: 'Next[D]') -> 'ControlFlow[D]':
    old = ctx.stash
    ctx.stash = Stash(old)

    try:
        return await handler(ctx, next)
    finally:
        ctx.stash = old


__all__ = ["ward_stash"]


