from __future__ import annotations

from ..dispatching.context import Context
from ..filtering.types import FilterFn

from ._inspect import HandlerFn, AnyHandlerFn
from ._inspect import into_handler_fn

from typing import Generic, TypeVar, Optional, Callable, TypeAlias

T = TypeVar("T")
D = TypeVar("D")


class Handler(Generic[D, T]):
    def __init__(
        self,
        fn: AnyHandlerFn[D, T],
        filter_: Optional[FilterFn[D, T]] = None,
    ) -> None:
        self.filter_ = filter_
        self._fn_name = fn.__name__
        self.fn: HandlerFn[D, T] = into_handler_fn(fn)

    def __repr__(self) -> str:
        return f"<Handler name={self._fn_name!r}>"

    def transform_inplace(
        self, f: HandlerInplaceTransformer[D, T]
    ) -> None:
        f(self)

    async def try_invoke(self, ctx: Context[D, T]) -> bool:
        filter_ = self.filter_
        if filter_ is not None:
            if not await filter_(ctx):
                return False
        await self.fn(ctx)

        return True


HandlerInplaceTransformer: TypeAlias = Callable[[Handler[D, T]], None]

__all__ = [
    "Handler",
    "HandlerFn",
    "AnyHandlerFn",
    "HandlerInplaceTransformer",
]
