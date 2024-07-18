import typing as t

from sena.control_flow import Continue

from ..types.ctx import Ctx
from ..utils.omit import Omittable, OMIT
from ..utils.altering import Alterer1, alter1

from .handler import (
    HandlerFn,
    AbstractHandler,
    Handler,
    Mapper,
    Next,
)
from .control_flow import ControlFlow


D = t.TypeVar("D")
_Handlers: t.TypeAlias = tuple[HandlerFn[D], ...]

# Dispatcher for single event type
class Dispatcher(AbstractHandler[D]):
    handlers: _Handlers[D]

    def __init__(self, handlers: _Handlers[D] = ()) -> None:
        self.handlers = handlers

    def __repr__(self) -> str:
        return f"Dispatcher(handlers={self.handlers!r})"

    def alter(
        self,
        *,
        handlers: Omittable[Alterer1[_Handlers[D]]] = OMIT,
    ) -> t.Self:
        return type(self)(
            handlers=alter1(handlers, self.handlers),
        )

    def register(self, *handlers: HandlerFn[D]) -> t.Self:
        return self.alter(handlers=lambda prev: (*prev, *handlers))

    def map(self, f: Mapper[D]) -> AbstractHandler[D]:
        return Handler[D](f(self))

    async def __call__(self, ctx: Ctx[D], next: Next[D]) -> ControlFlow[D]:
        for handler in self.handlers:
            result = await handler(ctx, next)
            if isinstance(result, Continue):
                ctx = result.value
            return result
        return Continue(ctx)


__all__ = ["Dispatcher"]


