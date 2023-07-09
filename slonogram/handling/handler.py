from __future__ import annotations

from ..types.context import Context
from ..types.filter import FilterFn
from ..types.middleware import MiddlewareFn
from ..types.handler_fn import HandlerFn, AnyHandlerFn, into_handler_fn

from typing import Generic, TypeVar, Optional, Callable, TypeAlias

T = TypeVar("T")


class Handler(Generic[T]):
    def __init__(
        self,
        fn: AnyHandlerFn[T],
        observer: bool,
        filter_: Optional[FilterFn[T]],
        middleware: Optional[MiddlewareFn[T]],
    ) -> None:
        self.filter_ = filter_
        self.middleware = middleware

        self._fn_name = getattr(fn, "__name__", repr(fn))
        self.observer = observer
        self.fn: HandlerFn[T] = into_handler_fn(fn)

    def __repr__(self) -> str:
        obs_flag = ":observer" if self.observer else ""
        return f"<Handler{obs_flag} name={self._fn_name!r}>"

    async def try_invoke(self, ctx: Context[T]) -> bool:
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


HandlerInplaceTransformer: TypeAlias = Callable[[Handler[T]], None]

__all__ = [
    "Handler",
    "HandlerFn",
    "AnyHandlerFn",
    "HandlerInplaceTransformer",
    "into_handler_fn",
]
