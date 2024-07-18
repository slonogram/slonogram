import typing as t

from ..handler import (
    AbstractHandler,
    HandlerFn,
    Handler,
    Mapper,
    Next,
)
from ..control_flow import ControlFlow

from .slots import Slots

from slonogram.types.ctx import Ctx
from slonogram.utils.altering import alter1, Alterer1
from slonogram.utils.omit import Omittable, OMIT

from slonogram.schemas.update import Update
from slonogram.schemas.message import Message
from slonogram.schemas.callback_query import CallbackQuery


class Root(AbstractHandler[Update]):
    __slots__ = ('slots', )

    def __init__(self, slots: Omittable[Slots] = OMIT) -> None:
        self.slots = Slots() if slots is OMIT else t.cast(Slots, slots)

    def __repr__(self) -> str:
        return f"Root(slots={self.slots!r})"

    def sent_message(self, *hs: HandlerFn[Message]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(sent_message=lambda prev: (*prev, *hs)))

    def callback_query(self, *hs: HandlerFn[CallbackQuery]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(callback_query=lambda prev: (*prev, *hs)))

    def alter(
        self,
        *,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> t.Self:
        return type(self)(
            slots=alter1(slots, self.slots),
        )

    def map(self, f: Mapper[Update]) -> AbstractHandler[Update]:
        return Handler(f(self))

    async def __call__(self, ctx: Ctx[Update], next: Next[Update]) -> ControlFlow[Update]:
        # TODO: let's write that tricky converting mess later
        raise NotImplementedError


__all__ = ["Root"]


