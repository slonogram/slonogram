from typing import (
    TypeVar,
    TYPE_CHECKING,
    Protocol,
    TypeAlias,
    Callable,
)

from .handler import Handler
from ..abstract.interested import Interested
if TYPE_CHECKING:
    from ..filtering.base import Filter
    
    from .follows import CurrentMiddleware

from ..reflect.named import Named
from ..types.stash import Stash
from ..types.caught_exception import CaughtException


M = TypeVar("M")
E = TypeVar("E", bound=Exception)
ReduceF: TypeAlias = Callable[['Filter[M]', 'Filter[M]'], 'Filter[M]']

class ExtendedHandler(Handler[M], Interested, Named, Protocol[M]):
    __name__: str = ''
    __extended_handler__: bool = True

    def with_stash(self, stash: Stash) -> 'ExtendedHandler[M]':
        from ..middlewares.inject_stash import InjectStash

        return self << InjectStash(stash)

    def catch(self, exc: type[E], handler: Handler[CaughtException[M, E]]) -> 'ExtendedHandler[M]':
        from ..middlewares.catch import Catch

        return self << Catch(exc, handler)

    def filtered(self, filter: 'Filter[M]') -> 'ExtendedHandler[M]':
        from .filtered import Filtered

        return Filtered(self, filter)

    def after(self, *middlewares: 'CurrentMiddleware[M]') -> 'ExtendedHandler[M]':
        from .follows import from_iterable

        return from_iterable(self, middlewares)

    def middlewares(self, *middlewares: 'CurrentMiddleware[M]') -> 'ExtendedHandler[M]':
        from .follows import from_iterable

        return from_iterable(self, reversed(middlewares))

    def __lshift__(self, middleware: 'CurrentMiddleware[M]') -> 'ExtendedHandler[M]':
        from .follows import Follows

        return Follows(self, middleware)

    def __repr__(self) -> str:
        ...

__all__ = ["ExtendedHandler"]



