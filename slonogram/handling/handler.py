from ..dispatching.context import Context
from ..filtering.types import FilterFn

from ._inspect import HandlerFn, AnyHandlerFn, into_handler_fn

from typing import (
    Generic,
    TypeVar,
    Optional,
)

T = TypeVar("T")
D = TypeVar("D")


class Handler(Generic[D, T]):
    def __init__(
        self,
        fn: AnyHandlerFn[D, T],
        filter_: Optional[FilterFn[D, T]] = None,
    ) -> None:
        self.filter_ = filter_
        self.fn: HandlerFn[D, T] = into_handler_fn(fn)

    def __repr__(self) -> str:
        return f"<Handler name={self.fn.__name__!r}>"

    async def try_invoke(self, ctx: Context[D, T]) -> bool:
        filter_ = self.filter_
        if filter_ is not None:
            if not await filter_(ctx):
                return False
        await self.fn(ctx)

        return True


__all__ = ["Handler", "HandlerFn"]
