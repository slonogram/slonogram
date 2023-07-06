from .context import Context

from typing import TypeVar, TypeAlias, Callable, Awaitable, List
from functools import partial

D = TypeVar("D")
T = TypeVar("T")

MiddlewareFn: TypeAlias = Callable[[Context[D, T]], Awaitable[None]]
AnyMiddlewareFn: TypeAlias = Callable[
    [MiddlewareFn[D, T], Context[D, T]], Awaitable[None]
]


class Chain:
    def __init__(self, *middlewares: AnyMiddlewareFn[D, T]) -> None:
        tail: MiddlewareFn[D, T] = do_nothing
        path: List[str] = []
        for middleware in reversed(middlewares):
            tail = partial(middleware, tail)
            path.append(middleware.__name__)

        self._fn = tail
        self._path = path

    def __call__(self, context: Context[D, T]) -> Awaitable[None]:
        return self._fn(context)

    def __repr__(self) -> str:
        return " <| ".join(self._path)


class Group:
    def __init__(self, *chains: MiddlewareFn[D, T]) -> None:
        self._chains = chains

    async def __call__(self, context: Context[D, T]) -> None:
        for chain in self._chains:
            await chain(context)

    def __repr__(self) -> str:
        wrapped = map(lambda chain: f"({chain!r})", self._chains)

        return " -> ".join(wrapped)


async def do_nothing(_: Context[D, T]) -> None:
    pass
