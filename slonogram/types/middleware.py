from __future__ import annotations

from .context import Context

from typing import TypeVar, TypeAlias, Callable, Awaitable, List, Generic
from functools import partial

T = TypeVar("T")

MiddlewareFn: TypeAlias = Callable[[Context[T]], Awaitable[None]]
AnyMiddlewareFn: TypeAlias = Callable[
    [MiddlewareFn[T], Context[T]], Awaitable[None]
]


class Chain(Generic[T]):
    def __init__(self, *middlewares: AnyMiddlewareFn[T]) -> None:
        tail: MiddlewareFn[T] = do_nothing
        path: List[str] = []
        for middleware in reversed(middlewares):
            tail = partial(middleware, tail)
            path.append(middleware.__name__)

        self._fn = tail
        self._path = path

    def __call__(self, context: Context[T]) -> Awaitable[None]:
        return self._fn(context)

    def __matmul__(self, rhs: MiddlewareFn[T]) -> Group[T]:
        return Group(self, rhs)

    def __repr__(self) -> str:
        return " <| ".join(self._path)


class Group(Generic[T]):
    def __init__(self, *chains: MiddlewareFn[T]) -> None:
        self._chains = chains

    async def __call__(self, context: Context[T]) -> None:
        for chain in self._chains:
            await chain(context)

    def __matmul__(self, rhs: MiddlewareFn[T]) -> Group[T]:
        return Group(*self._chains, rhs)

    def __repr__(self) -> str:
        wrapped = map(lambda chain: f"({chain!r})", self._chains)

        return " -> ".join(wrapped)


async def do_nothing(_: Context[T]) -> None:
    pass
