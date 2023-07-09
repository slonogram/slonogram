from typing import (
    Awaitable,
    Protocol,
    TypeAlias,
    Generic,
    TypeVar,
    Callable,
    cast,
    get_origin,
)
from inspect import signature, Signature
from .context import Context
from ..bot import Bot

T = TypeVar("T")
R = TypeVar("R")

_Single: TypeAlias = Callable[[T], Awaitable[None]]
_Two: TypeAlias = Callable[[T, R], Awaitable[None]]

AnyHandlerFn: TypeAlias = (
    _Single[Bot]
    | _Single[T]
    | _Single[Context[T]]
    | _Two[Bot, T]
    | _Two[T, Bot]
)


class HandlerFn(Protocol, Generic[T]):
    def __call__(self, context: Context[T], /) -> Awaitable[None]:
        ...


class _WrappedFn(Generic[T]):
    __slots__ = "fn", "__name__", "__call__"

    def __init__(self, anyfn: AnyHandlerFn[T], call_method: str) -> None:
        self.fn = anyfn
        self.__call__ = getattr(self, call_method)
        self.__name__ = getattr(anyfn, "__name__", "<unnamed>")

    def only_bot(self, ctx: Context[T]) -> Awaitable[None]:
        return self.fn(ctx.inter.bot)  # type: ignore

    def only_model(self, ctx: Context[T]) -> Awaitable[None]:
        return self.fn(ctx.model)  # type: ignore

    def bot_model(self, ctx: Context[T]) -> Awaitable[None]:
        return self.fn(ctx.inter.bot, ctx.model)  # type: ignore

    def model_bot(self, ctx: Context[T]) -> Awaitable[None]:
        return self.fn(ctx.model, ctx.inter.bot)  # type: ignore


def into_handler_fn(anyfn: AnyHandlerFn[T]) -> HandlerFn[T]:
    if getattr(anyfn, "__cast_ctxed__", False):
        return cast(HandlerFn[T], anyfn)

    fn_name = getattr(anyfn, "__name__", "<unnamed>")
    sig = signature(anyfn)
    params = sig.parameters

    if len(params) == 1:
        first = next(iter(params.values()))
        annot = first.annotation
        if annot is Signature.empty:
            raise TypeError(
                f"Provide annotation for the function {fn_name} parameter"
            )
        elif annot is Bot:
            return _WrappedFn(anyfn, "only_bot")
        elif get_origin(annot) is Context:
            return cast(HandlerFn[T], anyfn)
        else:
            raise TypeError(f"Unknown type {annot!r}")
    elif len(params) == 2:
        it = iter(params.values())
        first = next(it)
        second = next(it)

        f_annot = first.annotation
        s_annot = second.annotation

        f_ty = get_origin(f_annot) or f_annot
        s_ty = get_origin(s_annot) or s_annot
        tps = (f_ty, s_ty)

        if tps[0] is Bot:
            return _WrappedFn(anyfn, "bot_model")
        elif tps[1] is Bot:
            return _WrappedFn(anyfn, "model_bot")
        else:
            raise TypeError("Unknown `AnyHandlerFn[T]` signature pattern")

    raise TypeError(
        "`AnyHandlerFn[T]` should take exactly 2 or 1 arguments"
    )


__all__ = ["AnyHandlerFn", "HandlerFn", "into_handler_fn"]
