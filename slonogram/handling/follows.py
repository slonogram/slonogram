from typing import TypeVar, Awaitable, Iterable, Protocol
from functools import reduce

from .auto_collect import auto_collect
from .activation import Activation
from .handler import Handler
from .extended import ExtendedHandler
from .utils import unwrap_handler

from ..types.context import Context
from ..reflect.named import get_name

M = TypeVar("M")

class CurrentMiddleware(Protocol[M]):
    def __call__(self, ctx: 'Context[M]', next: 'Handler[M]') -> Awaitable[Activation]:
        ...

class Follows(ExtendedHandler[M]):
    __slots__ = ("next", "current")

    def __init__(self, next: Handler[M], current: CurrentMiddleware[M]) -> None:
        self.next = unwrap_handler(next)
        self.current = current
        self.__name__ = get_name(next, '')

    @auto_collect
    def collect_interests(self):
        return (self.next, )

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
    from .wrap import Wrap

    return reduce(lambda lhs, rhs: lhs << rhs, it, Wrap(handler))


__all__ = ["Follows", "CurrentMiddleware", "from_iterable"]

