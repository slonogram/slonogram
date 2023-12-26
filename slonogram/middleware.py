from __future__ import annotations
from typing import (
    Any,
    overload,
    Awaitable,
    TypeVar,
    ParamSpec,
    Generic,
    TypeAlias,
    Protocol,
    Concatenate,
    Iterable,
)
from functools import wraps

from .dispatching.context import Context

M = TypeVar("M")
P = ParamSpec("P")


class Middleware(Protocol[P]):
    def __call__(
        self,
        *args: P.args,
        **kwds: P.kwargs,
    ) -> Awaitable[None]:
        ...


CtxMiddleware: TypeAlias = Middleware[Concatenate[Context[M], P]]
SimpleMiddleware: TypeAlias = CtxMiddleware[M, []]
ExcMiddleware: TypeAlias = CtxMiddleware[M, [Exception | None]]


class Group(Generic[M, P]):
    __slots__ = ("middlewares",)

    middlewares: tuple[CtxMiddleware[M, P], ...]

    def __init__(self, *middlewares: CtxMiddleware[M, P]) -> None:
        self.middlewares = middlewares

    @overload
    def __and__(self, rhs: Group[M, P]) -> Group[M, P]:
        ...

    @overload
    def __and__(self, rhs: CtxMiddleware[M, P]) -> Group[M, P]:
        ...

    @overload
    def __and__(self, rhs: Iterable[CtxMiddleware[M, P]]) -> Group[M, P]:
        ...

    def __and__(
        self,
        rhs: Any,
    ) -> Group[M, P]:
        if isinstance(rhs, Iterable):
            return Group(*self.middlewares, *rhs)
        elif isinstance(rhs, Group):
            return Group(*self.middlewares, *rhs.middlewares)

        return Group(*self.middlewares, rhs)

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
    "CtxMiddleware",
    "SimpleMiddleware",
    "ExcMiddleware",
    "Group",
    "take_exc",
    "discard_exc",
]
