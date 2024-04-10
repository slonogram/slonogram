from typing import TypeVar, Awaitable, Iterable, Protocol, TYPE_CHECKING
from functools import reduce

from .activation import Activation
from .handler import Handler
from .extended import ExtendedHandler
from .utils import unwrap

if TYPE_CHECKING:
    from ..dispatching.context import Context

from .wrap import Wrap

M = TypeVar("M")

class CurrentMiddleware(Protocol[M]):
    def __call__(self, ctx: 'Context[M]', next: 'Handler[M]') -> Awaitable[Activation]:
        ...

class Follows(ExtendedHandler[M]):
    __slots__ = ("next", "current")

    def __init__(self, next: Handler[M], current: CurrentMiddleware[M]) -> None:
        self.next = unwrap(next)
        self.current = current

    def __call__(self, ctx: 'Context[M]', /) -> Awaitable[Activation]:
        return self.current(ctx, self.next)

    def __repr__(self) -> str:
        return f"Follows({self.current!r}, next={self.next!r})"


def from_iterable(
    handler: Handler[M],
    it: Iterable[CurrentMiddleware[M]],
) -> ExtendedHandler[M]:
    """Constructs :ref:`ExtendedHandler` handler from the iterable, as opposed to sequential construction like

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


__all__ = ["Follows", "CurrentMiddleware", "from_iterable"]

