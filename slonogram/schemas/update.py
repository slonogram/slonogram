import dataclasses as dtc

from .message import Message
from .callback_query import CallbackQuery



@dtc.dataclass(slots=True)
class Update:
    message: Message | None = None
    callback_query: CallbackQuery | None = None


__all__ = ["Update"]

