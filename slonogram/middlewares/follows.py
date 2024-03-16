from typing import TypeVar, Awaitable, Iterable
from functools import reduce

from ..handling.activation import Activation
from ..handling.handler import Handler
from ..dispatching.context import Context
from .base import FollowedMiddleware, Middlewared

from .wrap import Wrap

M = TypeVar("M")


class Follows(Middlewared[M]):
    __slots__ = ("follower", "after")

    def __init__(self, follower: Handler[M], after: FollowedMiddleware[M]) -> None:
        self.follower = follower
        self.after = after

    def __call__(self, ctx: Context[M], /) -> Awaitable[Activation]:
        return self.after(ctx, self.follower)

    def __repr__(self) -> str:
        return f"Follows({self.follower!r}, after={self.after!r})"


def from_iterable(
    handler: Handler[M],
    it: Iterable[FollowedMiddleware[M]],
) -> Middlewared[M]:
    """Constructs :ref:`Middlewared` handler from the iterable, as opposed to sequential construction like

    ```python
    f = (
        Wrap(f)
        << middleware1
        << middleware2
        << middleware3
    )
    ```

    """
    return reduce(lambda lhs, rhs: lhs << rhs, it, Wrap(handler))


__all__ = ["Follows", "from_iterable"]
