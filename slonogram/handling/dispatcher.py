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

from ..omittable import Omittable, omitted_or, OMIT, Omit
from ..altering import alter1, Alterer1

M = TypeVar("M")
_Handlers: TypeAlias = tuple[Handler[M], ...]

def _try_flatten(handler: Handler[M]) -> Iterable[Handler[M]]:
    if isinstance(handler, Dispatcher) and handler.mergeable:
        return handler.handlers
    return (handler, )

class Dispatcher(ExtendedHandler[M]):
    __slots__ = (
        "name",
        "stash",
        "handlers",
        "_mergeable",
    )

    name: str | None
    handlers: _Handlers[M]

    def __init__(
        self,
        handlers: Omittable[_Handlers[M]] = OMIT,
        stash: Omittable[Stash] = OMIT,
        name: Omittable[str | None] = OMIT,
        mergeable: Omittable[bool] = OMIT,
    ) -> None:
        self.stash = stash
        self.handlers = omitted_or(handlers, ())
        self.name = omitted_or(name, None)
        self._mergeable = omitted_or(mergeable, True)

    @property
    def __name__(self) -> str:
        return self.name or ''

    @__name__.setter
    def __name__(self, value: str) -> None:
        self.name = value

    @auto_collect
    def collect_interests(self):
        return self.handlers

    @property
    def mergeable(self) -> bool:
        return self._mergeable and isinstance(self.stash, Omit)

    def alter(
        self,
        handlers: Omittable[Alterer1[_Handlers[M]]] = OMIT,
        stash: Omittable[Alterer1[Omittable[Stash]]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
    ) -> "Dispatcher[M]":
        return Dispatcher[M](
            handlers=alter1(handlers, self.handlers),
            stash=alter1(stash, self.stash),
            name=alter1(name, self.name),
        )

    def register(self, *handlers: Handler[M]) -> "Dispatcher[M]":
        return self.alter(handlers=lambda prev: (
            *flatten(map(_try_flatten, handlers)),
            *prev,
        ))

    def __repr__(self) -> str:
        return f"Dispatcher(name={self.name!r}, handlers={self.handlers})"

    async def __call__(
        self,
        context: Context[M],
        /,
    ) -> Activation:
        if not isinstance(self.stash, Omit):
            context = context.alter(stash=lambda x: x.append(self.stash))

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
