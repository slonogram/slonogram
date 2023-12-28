from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import (
    Generic,
    TypeVar,
    ParamSpec,
    Awaitable,
    Iterable,
)

from . import Middleware

P = ParamSpec("P")
R = TypeVar("R")


class ExtendedMiddleware(Generic[P, R], metaclass=ABCMeta):
    def __and__(self, rhs: Middleware[P, R]) -> Group[P, R]:
        return Group(self, rhs)

    @abstractmethod
    def __call__(
        self,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> Awaitable[R]:
        raise NotImplementedError


def flatten_middlewares(
    middlewares: Iterable[Middleware[P, R]]
) -> tuple[Middleware[P, R], ...]:
    mws: list[Middleware[P, R]] = []
    for mw in middlewares:
        if isinstance(mw, Group):
            mws.extend(mw.middlewares)
        else:
            mws.append(mw)

    return tuple(mws)


class Group(ExtendedMiddleware[P, R]):
    __slots__ = ("middlewares",)

    def __init__(self, *middlewares: Middleware[P, R]) -> None:
        if not middlewares:
            raise TypeError("Can't create empty group")
        self.middlewares = flatten_middlewares(middlewares)

    async def __call__(
        self,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> R:
        for middleware in self.middlewares:
            result = await middleware(*args, **kwargs)
        return result


__all__ = [
    "ExtendedMiddleware",
    "Group",
]
