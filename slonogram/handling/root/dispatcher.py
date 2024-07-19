import typing as t

from ..handler import (
    AbstractHandler,
    HandlerFn,
    Handler,
    Mapper,
    Next,
)
from ..control_flow import ControlFlow
from ..reduction import Reducer

from .slots import Slots
from ..dispatcher import Dispatcher

from slonogram.types.ctx import Ctx
from slonogram.types.interest import Interest
from slonogram.types.handler_meta_info import HandlerMetaInfo

from slonogram.utils.altering import alter1, Alterer1
from slonogram.utils.omit import Omittable, OMIT
from slonogram.utils.collecting import CollectMetaInfo

from slonogram.schemas.update import Update
from slonogram.schemas.message import Message
from slonogram.schemas.callback_query import CallbackQuery

T = t.TypeVar("T")

# Dispatcher for multiple event types
class Root(AbstractHandler[Update], CollectMetaInfo):
    __slots__ = ('slots', )

    def __init__(self, slots: Omittable[Slots] = OMIT) -> None:
        self.slots = Slots() if slots is OMIT else t.cast(Slots, slots)

    def collect_meta_info(self) -> HandlerMetaInfo:
        slots = self.slots
        interests = frozenset[Interest]()

        _VARIANTS: tuple[tuple[Dispatcher[t.Any], Interest], ...] = (
            (slots.sent_message, Interest.MESSAGE),
            (slots.callback_query, Interest.CALLBACK_QUERY),
        )

        for dp, interest in _VARIANTS:
            if dp.handlers:
                interests = interests.union({interest})

        return HandlerMetaInfo(interests)

    def __repr__(self) -> str:
        return f"Root(slots={self.slots!r})"

    def reduce(self, f: Reducer[Update, T], initial: T) -> T:
        _ = f
        return initial

    def sent_message(self, *hs: HandlerFn[Message]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(sent_message=lambda dp: dp.register(*hs)))

    def callback_query(self, *hs: HandlerFn[CallbackQuery]) -> t.Self:
        return self.alter(slots=lambda s: s.alter(callback_query=lambda dp: dp.register(*hs)))

    def alter(
        self,
        *,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> t.Self:
        return type(self)(
            slots=alter1(slots, self.slots),
        )

    def map(self, f: Mapper[Update]) -> AbstractHandler[Update]:
        return Handler[Update](f(self))

    async def __call__(self, ctx: Ctx[Update], next: Next[Update]) -> ControlFlow[Update]:
        # TODO: let's write that tricky converting mess later
        raise NotImplementedError

__all__ = ["Root"]


