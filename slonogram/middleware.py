from typing import (
    Awaitable,
    TypeVar,
    ParamSpec,
    Generic,
    TypeAlias,
    Callable,
    Concatenate,
)
from functools import wraps

from .dispatching.context import Context

M = TypeVar("M")
P = ParamSpec("P")

BareMiddleware: TypeAlias = Callable[Concatenate[Context[M], P], Awaitable[None]]
SimpleMiddleware: TypeAlias = BareMiddleware[M, []]
ExcMiddleware: TypeAlias = BareMiddleware[M, [Exception | None]]


class Group(Generic[P]):
    __slots__ = ("middlewares",)

    def __init__(self, *middlewares: BareMiddleware[M, P]) -> None:
        self.middlewares = middlewares

    async def __call__(
        self,
        context: Context[M],
        *args: P.args,
        **kwds: P.kwargs,
    ) -> None:
        for middleware in self.middlewares:
            await middleware(context, *args, **kwds)


def take_exc(simple: SimpleMiddleware[M]) -> ExcMiddleware[M]:
    @wraps(simple)
    def wrapper(ctx: Context[M], _: Exception | None) -> Awaitable[None]:
        return simple(ctx)

    return wrapper


def discard_exc(exc_handler: ExcMiddleware[M]) -> SimpleMiddleware[M]:
    @wraps(exc_handler)
    def wrapper(ctx: Context[M]) -> Awaitable[None]:
        return exc_handler(ctx, None)

    return wrapper


__all__ = [
    "BareMiddleware",
    "SimpleMiddleware",
    "ExcMiddleware",
    "Group",
    "take_exc",
    "discard_exc",
]
