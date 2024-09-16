import typing as t
import enum
import dataclasses as dtc

from .message import Message
from .callback_query import CallbackQuery
from .inline_query import InlineQuery


class MessageEventKind(enum.IntEnum):
    SENT = enum.auto()
    EDITED = enum.auto()


@dtc.dataclass(slots=True)
class MessageEvent:
    kind: MessageEventKind
    message: Message


@dtc.dataclass(slots=True)
class UpdateDetails: ...


UpdateData: t.TypeAlias = MessageEvent | CallbackQuery | InlineQuery


@dtc.dataclass(slots=True)
class Update:
    details: UpdateDetails
    data: UpdateData
