from .context import Context
from ..bot import Bot
from ..filters.types import FilterFn

from functools import partial
from inspect import signature
from typing import Generic, TypeVar, TypeAlias, Callable, Awaitable

T = TypeVar("T")

HandlerFnWithCtx: TypeAlias = Callable[[Context[T]], Awaitable[None]]
HandlerFnOnlyBot: TypeAlias = Callable[[Bot], Awaitable[None]]
HandlerFnModelBot: TypeAlias = Callable[[T, Bot], Awaitable[None]]

HandlerFn: TypeAlias = (
    HandlerFnWithCtx[T] | HandlerFnOnlyBot | HandlerFnModelBot[T]
)


def _create_fn(
    fn: HandlerFn[T], prefer_bot: bool
) -> Callable[[Context[T]], Awaitable[None]]:
    sig = signature(fn)
    params_no = len(sig.parameters)

    match params_no:
        case 1 if prefer_bot:
            return partial(_call_only_bot, fn)
        case 1:
            return partial(_call_with_ctx, fn)
        case 2:
            return partial(_call_model_bot, fn)
    raise ValueError("> 2 arguments in the handler function")


def _call_with_ctx(
    fn: HandlerFnWithCtx[T], ctx: Context[T]
) -> Awaitable[None]:
    return fn(ctx)


def _call_only_bot(
    fn: HandlerFnOnlyBot, ctx: Context[T]
) -> Awaitable[None]:
    return fn(ctx.bot)


def _call_model_bot(
    fn: HandlerFnModelBot[T], ctx: Context[T]
) -> Awaitable[None]:
    return fn(ctx.model, ctx.bot)


class Handler(Generic[T]):
    def __init__(
        self, prefer_bot: bool, fn: HandlerFn[T], filter_: FilterFn[T]
    ) -> None:
        self.filter_ = filter_
        self.fn = _create_fn(fn, prefer_bot)

    async def try_invoke(self, ctx: Context[T]) -> bool:
        filter_result = await self.filter_(ctx)
        if filter_result is None:
            return False
        await self.fn(ctx)

        return True


__all__ = ["Handler"]
