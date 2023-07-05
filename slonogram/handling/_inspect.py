from ..dispatching.context import Context
from ..bot import Bot

from functools import partial
from typing import (
    TypeVar,
    Callable,
    TypeAlias,
    Awaitable,
    Any,
    Tuple,
    Type,
)
from inspect import signature

D = TypeVar("D")
T = TypeVar("T")

HandlerFn: TypeAlias = Callable[[Context[D, T]], Awaitable[None]]
_Single: TypeAlias = Callable[[T], Awaitable[None]]
_Two: TypeAlias = Callable[[D, T], Awaitable[None]]

AnyHandlerFn: TypeAlias = (
    _Single[Bot]
    | _Single[Context[D, T]]
    | _Two[Bot, Context[D, T]]
    | _Two[Context[D, T], Bot]
)


def extract_origin_type(t) -> type:
    return getattr(t, "__origin__", t)


def annotate_with_handler_fn(
    c: Callable[[Any], Awaitable[None]]
) -> HandlerFn[Any, Any]:
    """
    Annotate first argument of `c` with the `Context` hint.

    BE AWARE!! This function has side-effects: it modifies
    parameter `c`
    :param c: callable to annotate
    :return: same function
    """
    sig = signature(c)
    first_arg_k = next(iter(sig.parameters))
    c.__annotations__[first_arg_k] = Context[Any, Any]
    return c  # type: ignore


def _fmt_tps_tuple(tps: Tuple[Type, Type]) -> str:
    return f"({tps[0].__qualname__}, {tps[1].__qualname__})"


def _named(name: str, f: HandlerFn[D, T]) -> HandlerFn[D, T]:
    f.__name__ = name
    return f


def into_handler_fn(original: AnyHandlerFn[D, T]) -> HandlerFn[D, T]:
    sig = signature(original)
    name_it = partial(_named, original.__name__)
    params = sig.parameters
    items = list(params.items())

    match items:
        case [(_, spec)]:
            origin = extract_origin_type(spec.annotation)
            if origin == Bot:
                return name_it(
                    lambda ctx: original(ctx.inter.bot)  # type: ignore
                )
            elif origin == Context:
                return original  # type: ignore
            else:
                raise TypeError(
                    "Not sure about type of the first argument,"
                    " please provide type hint to disambiguate it "
                    "(`Bot` or `Context[...]`)"
                )

        case [(_, spec1), (_, spec2)]:
            origins = (
                extract_origin_type(spec1.annotation),
                extract_origin_type(spec2.annotation),
            )

            if origins == (Bot, Context):
                return name_it(
                    lambda ctx: original(ctx.inter.bot, ctx)  # type: ignore
                )
            elif origins == (Context, Bot):
                return name_it(
                    lambda ctx: original(ctx, ctx.inter.bot)  # type: ignore
                )
            else:
                raise TypeError(
                    f"Function `{_fmt_tps_tuple(origins)} -> Awaitable[None]` "
                    f"Can't be made into `(Context[D, T]) -> Awaitable[None]`"
                    f". Note: arguments should be either "
                    f"`(Bot, Context)` or `(Context, Bot)`."
                )

        case _:
            raise TypeError(
                f"callable `{original.__name__}` should take 2 or 1 arguments"
            )


__all__ = ["HandlerFn", "into_handler_fn", "annotate_with_handler_fn"]
