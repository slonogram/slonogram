from typing import TypeVar

from ..handling.handler import Handler
from ..handling.activation import Activation
from ..handling.follows import CurrentMiddleware

from ..types.stash import Stash
from ..types.context import Context

M = TypeVar("M")

class InjectStash(CurrentMiddleware[M]):
    __slots__ = ('stash', )

    def __init__(self, stash: Stash) -> None:
        self.stash = stash

    async def __call__(self, ctx: Context[M], next: Handler[M]) -> Activation:
        old = ctx.stash
        ctx.stash = self.stash.append(old)
        try:
            return await next(ctx)
        finally:
            ctx.stash = old


__all__ = ["InjectStash"]

