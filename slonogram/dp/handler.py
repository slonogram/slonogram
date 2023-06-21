from .context import Context
from ..bot import Bot
from ..filters.types import FilterFn

from functools import partial
from inspect import signature
from typing import Generic, TypeVar, TypeAlias, Callable, Awaitable

T = TypeVar("T")
D = TypeVar("D")

HandlerFnWithCtx: TypeAlias = Callable[[Context[D, T]], Awaitable[None]]
HandlerFnOnlyBot: TypeAlias = Callable[[Bot], Awaitable[None]]
HandlerFnBotModel: TypeAlias = Callable[[Bot, T], Awaitable[None]]

HandlerFn: TypeAlias = (
    HandlerFnWithCtx[D, T] | HandlerFnOnlyBot | HandlerFnBotModel[T]
)


def _create_fn(
    fn: HandlerFn[D, T], prefer_bot: bool
) -> Callable[[Context[D, T]], Awaitable[None]]:
    sig = signature(fn)
    params_no = len(sig.parameters)

    match params_no:
        case 1 if prefer_bot:
            return partial(_call_only_bot, fn)
        case 1:
            return partial(_call_with_ctx, fn)
        case 2:
            return partial(_call_bot_model, fn)
    raise ValueError("> 2 arguments in the handler function")


def _call_with_ctx(
    fn: HandlerFnWithCtx[D, T], ctx: Context[D, T]
) -> Awaitable[None]:
    return fn(ctx)


def _call_only_bot(
    fn: HandlerFnOnlyBot, ctx: Context[D, T]
) -> Awaitable[None]:
    return fn(ctx.inter.bot)


def _call_bot_model(
    fn: HandlerFnBotModel[T], ctx: Context[D, T]
) -> Awaitable[None]:
    return fn(ctx.inter.bot, ctx.model)


class Handler(Generic[D, T]):
    def __init__(
        self,
        prefer_bot: bool,
        fn: HandlerFn[D, T],
        filter_: FilterFn[D, T],
    ) -> None:
        self.filter_ = filter_
        self.fn = _create_fn(fn, prefer_bot)

    async def try_invoke(self, ctx: Context[D, T]) -> bool:
        filter_result = await self.filter_(ctx)
        if filter_result is None:
            return False
        await self.fn(ctx)

        return True


__all__ = ["Handler"]
