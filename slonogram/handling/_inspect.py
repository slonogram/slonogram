from typing import (
    TypeVar,
    Callable,
    TypeAlias,
    Awaitable,
    Any,
    Tuple,
    Type,
    Generic,
    Protocol,
)

from ..dispatching.context import Context
from ..bot import Bot

from inspect import signature

R = TypeVar("R")
T = TypeVar("T")


class HandlerFn(Protocol, Generic[T]):
    def __call__(self, context: Context[T], /) -> Awaitable[None]:
        ...


_Single: TypeAlias = Callable[[T], Awaitable[None]]
_Two: TypeAlias = Callable[[R, T], Awaitable[None]]

AnyHandlerFn: TypeAlias = (
    _Single[Bot]
    | _Single[T]
    | _Single[Context[T]]
    | _Two[Bot, T]
    | _Two[T, Bot]
)


def extract_origin_type(t) -> type:
    return getattr(t, "__origin__", t)


def annotate_with_handler_fn(
    c: Callable[[Any], Awaitable[None]]
) -> HandlerFn[Any]:
    """
    Annotate first argument of `c` with the `Context` hint.

    BE AWARE!! This function has side-effects: it modifies
    parameter `c`
    :param c: callable to annotate
    :return: same function
    """
    sig = signature(c)
    first_arg_k = next(iter(sig.parameters))
    c.__annotations__[first_arg_k] = Context[Any]
    return c  # type: ignore


def _fmt_tps_tuple(tps: Tuple[Type, Type]) -> str:
    return f"({tps[0].__qualname__}, {tps[1].__qualname__})"


def into_handler_fn(original: AnyHandlerFn[T]) -> HandlerFn[T]:
    if getattr(original, "__treat_as_context__", False):
        return original  # type: ignore
    sig = signature(original)
    params = sig.parameters
    items = list(params.items())

    match items:
        case [(_, spec)]:
            origin = extract_origin_type(spec.annotation)
            if origin == Bot:
                return lambda ctx: original(ctx.inter.bot)  # type: ignore
            elif origin == Context:
                return original  # type: ignore
            else:
                return lambda ctx: original(ctx.model)  # type: ignore

        case [(_, spec1), (_, spec2)]:
            origins = (
                extract_origin_type(spec1.annotation),
                extract_origin_type(spec2.annotation),
            )

            if origins[1] == Bot:
                return lambda ctx: original(
                    ctx.model, ctx.inter.bot
                )  # type: ignore
            elif origins[0] == Bot:
                return lambda ctx: original(
                    ctx.inter.bot, ctx.model
                )  # type: ignore
            else:
                raise TypeError(
                    f"Function `{_fmt_tps_tuple(origins)} -> Awaitable[None]` "
                    f"Can't be made into `(Context[T]) -> Awaitable[None]`"
                    f". Note: arguments should be either "
                    f"`(Bot, T)` or `(T, Bot)`, where `T` is the model."
                )

        case _:
            raise TypeError(
                f"callable `{original.__name__}` should take 2 or 1 arguments"
            )


__all__ = ["HandlerFn", "into_handler_fn", "annotate_with_handler_fn"]
