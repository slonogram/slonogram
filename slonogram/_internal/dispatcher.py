import typing as t

from sena.control import map_cont

from .ext import HandlerExt
from .alter import Alter1, alter1
from .omit import Omittable, OMIT

from .handler import Handler, Result
from .ctx import Ctx
from .one_of import OneOf

from ..schemas.update import (
    Update,
    UpdateData,
    MessageEvent,
    MessageEventKind,
)
from ..schemas.message import Message
from ..schemas.callback_query import CallbackQuery
from ..schemas.inline_query import InlineQuery

from .slots import Slots

X = t.TypeVar("X")


def app(rhs: tuple[X, ...]) -> t.Callable[[OneOf[X]], OneOf[X]]:
    return lambda h: h.alter(handlers=lambda lhs: (*lhs, *rhs))


class Dispatcher(HandlerExt, Handler[Update]):
    slots: Slots

    def __init__(self, slots: Slots = Slots()) -> None:
        self.slots = slots

    def alter(
        self,
        *,
        slots: Omittable[Alter1[Slots]] = OMIT,
    ) -> t.Self:
        return type(self)(slots=alter1(self.slots, slots))

    def sent_message(self, *hs: Handler[Message]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(message=app(hs)))

    def edited_message(self, *hs: Handler[Message]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(edited_message=app(hs)))

    def inline_query(self, *hs: Handler[InlineQuery]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(inline_query=app(hs)))

    def callback_query(self, *hs: Handler[CallbackQuery]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(callback_query=app(hs)))

    async def __call__(self, ctx: Ctx[Update]) -> Result[Update]:
        updt = ctx.data.data
        slots = self.slots

        result: Result[UpdateData]
        match updt:
            case MessageEvent(kind, message):
                msg_ctx = ctx.with_data(message)

                if kind == MessageEventKind.SENT:
                    inner = await slots.message(msg_ctx)
                elif kind == MessageEventKind.EDITED:
                    inner = await slots.edited_message(msg_ctx)
                else:
                    raise NotImplementedError

                result = map_cont(
                    inner, lambda c: c.with_data(MessageEvent(kind, c.data))
                )

            case CallbackQuery() as cb_query:
                result = await slots.callback_query(ctx.with_data(cb_query))  # type: ignore

            case InlineQuery() as inl_query:
                result = await slots.inline_query(ctx.with_data(inl_query))  # type: ignore

            case _:
                raise NotImplementedError

        return map_cont(
            result, lambda c: ctx.with_data(Update(ctx.data.details, c.data))
        )
