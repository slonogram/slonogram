from typing import (
    TypeVar,
    TYPE_CHECKING,
    Protocol,
    Iterable,
    TypeAlias,
    Callable,
)

from ..schemas.maybe_inaccessible_message import Message

from .handler import Handler
from ..abstract.interested import Interested
if TYPE_CHECKING:
    from .follows import CurrentMiddleware

from ..filtering.base import Filter

from ..omittable import Omittable, Omit, OMIT
from ..reflect.named import Named, get_name
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

    def command(
        self: 'ExtendedHandler[Message]',
        variations: Omittable[Iterable[str] | str] = OMIT,
        filter: Omittable[Filter[Message]] = OMIT,
        reduce: Omittable[ReduceF[Message]] = OMIT,
    ) -> 'ExtendedHandler[Message]':
        from ..filtering.command import Command

        if isinstance(variations, Omit):
            name = get_name(self)
            if not name:
                raise TypeError(
                    f'Handler {self!r} has no name, '
                    f'you need to assign command variations by yourself'
                )
            variations = (name, )

        if isinstance(reduce, Omit):
            from ..filtering.and_ import And
            reduce = And

        u_filter: Filter[Message] = Command(variations)
        if not isinstance(filter, Omit):
            u_filter = reduce(u_filter, filter)

        return self.filtered(u_filter)

    def __repr__(self) -> str:
        ...

__all__ = ["ExtendedHandler"]



