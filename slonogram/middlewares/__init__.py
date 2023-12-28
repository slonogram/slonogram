from typing import TypeVar, Protocol, Awaitable, ParamSpec

M = TypeVar("M")
R = TypeVar("R", covariant=True)
P = ParamSpec("P")


class Middleware(Protocol[P, R]):
    def __call__(
        self,
        *args: P.args,
        **kwds: P.kwargs,
    ) -> Awaitable[R]:
        ...


__all__ = ["Middleware"]
