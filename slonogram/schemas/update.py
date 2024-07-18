from __future__ import annotations

import typing as t
import dataclasses as dtc

from .message import Message
from .callback_query import CallbackQuery

@dtc.dataclass(slots=True)
class UpdateInfo:
    id: int


@dtc.dataclass(slots=True)
class Update:
    info: UpdateInfo
    event: WhatUpdated


@dtc.dataclass(slots=True)
class SentMessage:
    message: Message


WhatUpdated: t.TypeAlias = SentMessage | CallbackQuery


__all__ = [
    "UpdateInfo",
    "SentMessage",

    "WhatUpdated",
]

