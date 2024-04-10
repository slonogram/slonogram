from typing import (
    TypeVar,
    TYPE_CHECKING,
    Protocol,
)

from .handler import Handler
if TYPE_CHECKING:
    from ..filtering.base import Filter

    from .follows import CurrentMiddleware

M = TypeVar("M")

class ExtendedHandler(Handler[M], Protocol[M]):
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



