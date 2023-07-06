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
from ..handling.middleware import MiddlewareFn
from ..schemas import Message
from .event_flags import MessageFlags

if TYPE_CHECKING:
    from .local_set import LocalSet

D = TypeVar("D")
T = TypeVar("T")

MsgHandler: TypeAlias = Handler[D, Message]
_OptFilterFn: TypeAlias = Optional[FilterFn[D, T]]
_OptMid: TypeAlias = Optional[MiddlewareFn[D, T]]
_RegRetDeco: TypeAlias = Callable[[AnyHandlerFn], Handler[D, T]]


class OnMessage(Generic[D]):
    def __init__(self, set_: LocalSet) -> None:
        self._set = set_

    def _register(
        self,
        observer: bool,
        subtypes: MessageFlags,
        filter_: _OptFilterFn[D, Message],
        middleware: _OptMid[D, Message],
    ) -> _RegRetDeco[D, Message]:
        def inner(fn: AnyHandlerFn) -> MsgHandler[D]:
            handler = MsgHandler[D](fn, observer, filter_, middleware)
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
        observer: bool = False,
        middleware: _OptMid[D, Message] = None,
    ) -> _RegRetDeco[D, Message]:
        return self._register(observer, subtypes, filter_, middleware)

    def sent(
        self,
        filter_: _OptFilterFn[D, Message] = None,
        observer: bool = False,
        middleware: _OptMid[D, Message] = None,
    ) -> _RegRetDeco[D, Message]:
        return self._register(
            observer, MessageFlags.SENT, filter_, middleware
        )

    def edited(
        self,
        filter_: _OptFilterFn[D, Message] = None,
        observer: bool = False,
        middleware: _OptMid[D, Message] = None,
    ) -> _RegRetDeco[D, Message]:
        return self._register(
            observer, MessageFlags.EDITED, filter_, middleware
        )
