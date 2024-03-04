from typing import TypeVar, TypeAlias

from .stash import Stash
from .context import Context

from ..abstract.interested import Interested
from ..types.interests import Interests
from ..middlewares.base import Middlewared
from ..handling.handler import Handler
from ..handling.activation import Activation
from ..omittable import Omittable, omitted_or, OMIT
from ..altering import alter1, Alterer1

M = TypeVar("M")

_Handlers: TypeAlias = tuple[Handler[M], ...]

class Dispatcher(Middlewared[M], Interested):
    __slots__ = (
        'name',
        'stash',
        'handlers',
    )

    name: str | None
    handlers: _Handlers[M]

    def __init__(
        self,
        handlers: Omittable[_Handlers[M]] = OMIT,
        stash: Omittable[Stash] = OMIT,
        name: Omittable[str | None] = OMIT,
    ) -> None:
        self.stash = omitted_or(stash, Stash())
        self.handlers = omitted_or(handlers, ())
        self.name = omitted_or(name, None)

    def alter(
        self,
        handlers: Omittable[Alterer1[_Handlers[M]]] = OMIT,
        stash: Omittable[Alterer1[Stash]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
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
    
    def collect_interests(self) -> Interests:
        interests = Interests(0)
        for handler in self.handlers:
            if isinstance(handler, Interested):
                interests |= handler.collect_interests()

        return interests

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
