from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Generic,
    Optional,
    TypeVar,
    TypeAlias,
    Callable,
)

from ..filtering.types import FilterFn
from ..handling.handler import Handler, AnyHandlerFn
from ..schemas import Message
from .event_flags import MessageFlags

if TYPE_CHECKING:
    from .local_set import LocalSet

D = TypeVar("D")
T = TypeVar("T")

MsgHandler: TypeAlias = Handler[D, Message]
_OptFilterFn: TypeAlias = Optional[FilterFn[D, T]]
_RegRetDeco: TypeAlias = Callable[[AnyHandlerFn], Handler[D, T]]


class OnMessage(Generic[D]):
    def __init__(self, set_: LocalSet) -> None:
        self._set = set_

    def _register(
        self,
        subtypes: MessageFlags,
        filter_: _OptFilterFn[D, Message],
    ) -> _RegRetDeco[D, Message]:
        def inner(fn: AnyHandlerFn) -> MsgHandler[D]:
            handler = MsgHandler[D](fn, filter_)
            if MessageFlags.SENT in subtypes:
                self._set._sent_message_handlers.append(handler)
            if MessageFlags.EDITED in subtypes:
                self._set._edited_message_handlers.append(handler)

            return handler

        return inner

    def __call__(
        self,
        subtypes: MessageFlags,
        filter_: _OptFilterFn[D, Message] = None,
    ) -> _RegRetDeco[D, Message]:
        return self._register(subtypes, filter_)

    def sent(
        self, filter_: _OptFilterFn[D, Message] = None
    ) -> _RegRetDeco[D, Message]:
        return self._register(MessageFlags.SENT, filter_)

    def edited(
        self, filter_: _OptFilterFn[D, Message] = None
    ) -> _RegRetDeco[D, Message]:
        return self._register(MessageFlags.EDITED, filter_)
