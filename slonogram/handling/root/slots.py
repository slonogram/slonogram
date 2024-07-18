import typing as t
import dataclasses as dtc

from ..dispatcher import Dispatcher

from slonogram.utils.altering import Alterer1, alter1
from slonogram.utils.omit import Omittable, OMIT

from slonogram.schemas.message import Message
from slonogram.schemas.callback_query import CallbackQuery


@dtc.dataclass(slots=True)
class Slots:
    sent_message: Dispatcher[Message] = Dispatcher()
    callback_query: Dispatcher[CallbackQuery] = Dispatcher()

    def alter(
        self,
        *,
        sent_message: Omittable[Alterer1[Dispatcher[Message]]] = OMIT,
        callback_query: Omittable[Alterer1[Dispatcher[CallbackQuery]]] = OMIT,
    ) -> t.Self:
        return type(self)(
            sent_message=alter1(sent_message, self.sent_message),
            callback_query=alter1(callback_query, self.callback_query),
        )


__all__ = ["Slots"]


