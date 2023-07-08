from __future__ import annotations

from ..dispatching.context import Context
from ..filtering.types import FilterFn

from .middleware import MiddlewareFn
from ._inspect import HandlerFn, AnyHandlerFn
from ._inspect import into_handler_fn

from typing import Generic, TypeVar, Optional, Callable, TypeAlias

T = TypeVar("T")
D = TypeVar("D")


class Handler(Generic[D, T]):
    def __init__(
        self,
        fn: AnyHandlerFn[D, T],
        observer: bool,
        filter_: Optional[FilterFn[D, T]],
        middleware: Optional[MiddlewareFn[D, T]],
    ) -> None:
        self.filter_ = filter_
        self.middleware = middleware

        self._fn_name = fn.__name__
        self.observer = observer
        self.fn: HandlerFn[D, T] = into_handler_fn(fn)

    def __repr__(self) -> str:
        obs_flag = ":observer" if self.observer else ""
        return f"<Handler{obs_flag} name={self._fn_name!r}>"

    async def try_invoke(self, ctx: Context[D, T]) -> bool:
        filter_ = self.filter_
        prev_pad = ctx.pad
        ctx.pad = prev_pad.create_child()

        try:
            if filter_ is not None:
                if not await filter_(ctx):
                    return False
            mw = self.middleware
            if mw is not None:
                await mw(ctx)

            await self.fn(ctx)
        finally:
            ctx.pad = prev_pad

        return not self.observer


HandlerInplaceTransformer: TypeAlias = Callable[[Handler[D, T]], None]

__all__ = [
    "Handler",
    "HandlerFn",
    "AnyHandlerFn",
    "HandlerInplaceTransformer",
    "into_handler_fn",
]
