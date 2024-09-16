import typing as t

from sena.control import Continue

from .alter import Alter1, alter1
from .omit import Omittable, OMIT
from .handler import Handler, Result
from .ext import HandlerExt

from .ctx import Ctx

Acc = t.TypeVar("Acc")
D = t.TypeVar("D")


class OneOf(HandlerExt, Handler[D]):
    __slots__ = ("handlers",)

    def __init__(self, handlers: tuple[Handler[D], ...]) -> None:
        self.handlers = handlers

    def alter(
        self,
        *,
        handlers: Omittable[Alter1[tuple[Handler[D], ...]]] = OMIT,
    ) -> t.Self:
        return type(self)(handlers=alter1(self.handlers, handlers))

    def register(self, *handlers: Handler[D]) -> t.Self:
        return self.alter(handlers=lambda h: (*h, *handlers))

    async def __call__(self, ctx: Ctx[D]) -> Result[D]:
        for handler in self.handlers:
            result = await handler(ctx.mut())

            match result:
                case Continue(value):
                    ctx = value
                case _:
                    return result

        return Continue(ctx)
