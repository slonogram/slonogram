from typing import Iterable, TypeVar, TypeAlias

from .stash import Stash
from .context import Context
from ..middlewares.base import Middlewared
from ..handling.handler import Handler
from ..handling.activation import Activation
from ..omittable import Omit, Omittable, omitted_or
from ..altering import alter1, Alterer1

M = TypeVar("M")
_OMIT = Omit()

_Handlers: TypeAlias = tuple[Handler[M], ...]

class Dispatcher(Middlewared[M]):
    __slots__ = (
        'name',
        'stash',
        'handlers',
    )

    name: str | None
    handlers: _Handlers[M]

    def __init__(
        self,
        handlers: Omittable[_Handlers[M]] = _OMIT,
        stash: Omittable[Stash] = _OMIT,
        name: Omittable[str | None] = _OMIT,
    ) -> None:
        self.stash = omitted_or(stash, Stash())
        self.handlers = omitted_or(handlers, ())
        self.name = omitted_or(name, None)

    def alter(
        self,
        handlers: Omittable[Alterer1[_Handlers[M]]] = _OMIT,
        stash: Omittable[Alterer1[Stash]] = _OMIT,
        name: Omittable[Alterer1[str | None]] = _OMIT,
    ) -> 'Dispatcher[M]':
        return Dispatcher[M](
            handlers=alter1(handlers, self.handlers),
            stash=alter1(stash, self.stash),
            name=alter1(name, self.name),
        )

    def register(self, *handlers: Handler[M]) -> 'Dispatcher[M]':
        return self.alter(handlers=lambda prev: (*prev, *handlers))

    def __repr__(self) -> str:
        return f'Dispatcher(name={self.name!r})'

    async def __call__(
        self,
        context: Context[M],
        /,
    ) -> Activation:
        new = Context(
            context.bot,
            context.model,
            context.stash.append(self.stash)
        )
        for handler in self.handlers:
            old = new.stash
            new.stash = Stash(old)

            try:
                activation = await handler(context)
            finally:
                new.stash = old

            if activation:
                return activation

        return Activation.stalled()


__all__ = ["Dispatcher"]
