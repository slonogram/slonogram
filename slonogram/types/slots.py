from __future__ import annotations

import typing as t
import dataclasses as dtc

from ..schemas.callback_query import CallbackQuery
from ..schemas.message import Message

if t.TYPE_CHECKING:
    from ..handling.handler import HandlerFn

from ..utils.altering import alter1, Alterer1
from ..utils.omit import OMIT,Omittable

D = t.TypeVar("D")

_Handlers: t.TypeAlias = tuple['HandlerFn[D]', ...]
_HAlterer: t.TypeAlias = Alterer1[_Handlers[D]]


@dtc.dataclass(slots=True, frozen=True)
class Slots:
    callback_query: _Handlers[CallbackQuery] = ()
    message: _Handlers[Message] = ()

    def alter1(
        self,
        callback_query: Omittable[_HAlterer[CallbackQuery]] = OMIT,
        message: Omittable[_HAlterer[Message]] = OMIT,
    ) -> Slots:
        return Slots(
            callback_query=alter1(callback_query, self.callback_query),
            message=alter1(message, self.message),
        )

__slots__ = ["Slots"]


