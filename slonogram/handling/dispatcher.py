from typing import (
    TypeVar,
    TypeAlias,
    Iterable,
)

from ..types.stash import Stash
from ..types.context import Context

from .._internal.utils import flatten

from .auto_collect import auto_collect
from .extended import ExtendedHandler
from .handler import Handler
from .activation import Activation

from ..omittable import Omittable, omitted_or, OMIT
from ..altering import alter1, Alterer1

M = TypeVar("M")
_Handlers: TypeAlias = tuple[Handler[M], ...]

def _try_flatten(handler: Handler[M]) -> Iterable[Handler[M]]:
    if isinstance(handler, Dispatcher) and handler.mergeable:
        return handler.handlers
    return (handler, )

def _find_interested_indices(handlers: Iterable[Handler[M]]) -> tuple[int, ...]:
    from .interested_in import InterestedIn

    return tuple(
        index
        for index, handler in enumerate(handlers)
        if isinstance(handler, InterestedIn)
    )

class Dispatcher(ExtendedHandler[M]):
    """Simple dispatching mechanism.

    Merging
    =======

    :class:`Dispatcher` is just a handler, actually, so everything applicable to the handlers 
    applicable to :class:`Dispatcher` too, for example, you can nest one dispatcher in another:

        .. code-block:: python

            from slonogram import handler_from_compatible

            @handler_from_compatible
            async def handler_even(ctx: Context[int]) -> None:
                print('even', ctx.model)

            @handler_from_compatible
            async def handler_odd(ctx: Context[int]) -> None:
                print('odd', ctx.model)

            odd_dp = (
                Dispatcher[int]()
                    .register(handler_odd.filtered(Lambda ctx: ctx.model % 2 != 0))
            )
            even_dp = (
                Dispatcher[int]()
                    .register(handler_even.filtered(lambda ctx: ctx.model % 2 == 0))
            )
            dp = Dispatcher[int]().register(even_dp, odd_dp)
            
            await dp(Context.stub(10))  # expected console output is `even 10`
            await dp(Context.stub(11))  # expected console output is `odd 11`

    Our call stack for this will look like this:

        .. code-block:: text
            dp
            |  odd_dp
            |  |  handler_odd
            |
            |  even_dp
            |  |  handler_even
            +-----------------

    Where each ``|`` on line represents one stack level increase only for this line. This can be heavily simplified, actually,
    into something like this:

        .. code-block:: text

            dp
            | handler_odd
            | handler_even

    Merging does this - it flattens nested dispatchers when that's possible and allowed (see :ref:`mergeable` property)

    :param handlers: homogenous tuple of :class:`Handler`s
    :param name: name of the dispatcher,
        useful for, for example, calling `.command()` on :class:`Dispatcher`
        or purely for debugging purposes
    :param mergeable: whether :class:`Dispatcher` can be merged or not (information above)
    """
    __slots__ = (
        "name",
        "handlers",
        "mergeable",
    )

    name: str | None
    handlers: _Handlers[M]

    def __init__(
        self,
        handlers: Omittable[_Handlers[M]] = OMIT,
        name: Omittable[str | None] = OMIT,
        mergeable: Omittable[bool] = OMIT,
    ) -> None:
        self.handlers = omitted_or(handlers, ())
        self.name = omitted_or(name, None)
        self.mergeable = omitted_or(mergeable, True)

    @property
    def __name__(self) -> str:
        return self.name or ''

    @__name__.setter
    def __name__(self, value: str) -> None:
        self.name = value

    @auto_collect
    def collect_interests(self):
        return self.handlers

    def alter(
        self,
        handlers: Omittable[Alterer1[_Handlers[M]]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
        mergeable: Omittable[Alterer1[bool]] = OMIT,
    ) -> "Dispatcher[M]":
        """Return copy of the dispatcher with specified functions applied
        """
        return Dispatcher[M](
            handlers=alter1(handlers, self.handlers),
            name=alter1(name, self.name),
            mergeable=alter1(mergeable, self.mergeable),
        )

    def register(self, *handlers: Handler[M]) -> "Dispatcher[M]":
        """Returns copy of the dispatcher with specified handlers prepended.

        :param handlers: which handlers to prepend
        """
        # Here we try to flat handlers, this is beneficial
        # since our code would use less nesting on stack
        flat = flatten(map(_try_flatten, handlers))

        return self.alter(handlers=lambda prev: (
            *flat,
            *prev,
        ))

    def __repr__(self) -> str:
        return f"Dispatcher(name={self.name!r}, handlers={self.handlers})"

    async def __call__(
        self,
        context: Context[M],
        /,
    ) -> Activation:
        for handler in self.handlers:
            old = context.stash
            context.stash = Stash(old)

            try:
                activation = await handler(context)
            finally:
                context.stash = old

            if activation:
                return activation

        return Activation.stalled()


__all__ = ["Dispatcher"]
