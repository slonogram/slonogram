from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Optional,
    TypeVar,
    TypeAlias,
    Callable,
)

from ..types.filter import FilterFn
from ..types.middleware import MiddlewareFn
from ..types.event_flags import MessageFlags
from ..types.handler_fn import AnyHandlerFn

from ..handling.handler import Handler
from ..schemas import Message, CallbackQuery

if TYPE_CHECKING:
    from .local_set import LocalSet

T = TypeVar("T")

MsgHandler: TypeAlias = Handler[Message]
CbHandler: TypeAlias = Handler[CallbackQuery]
_OptFilterFn: TypeAlias = Optional[FilterFn[T]]
_OptMid: TypeAlias = Optional[MiddlewareFn[T]]
_RegRetDeco: TypeAlias = Callable[[AnyHandlerFn[T]], Handler[T]]


class _ReceivesSet:
    def __init__(self, set_: LocalSet):
        self._set = set_


class OnCallback(_ReceivesSet):
    def __call__(
        self,
        filter_: _OptFilterFn[CallbackQuery] = None,
        middleware: _OptMid[CallbackQuery] = None,
        observer: bool = False
    ) -> _RegRetDeco[CallbackQuery]:
        def inner(fn: AnyHandlerFn) -> CbHandler:
            handler = Handler(fn, observer, filter_, middleware)
            self._set.callback_handlers.append(handler)
            return handler

        return inner


class OnMessage(_ReceivesSet):
    def _register(
        self,
        observer: bool,
        subtypes: MessageFlags,
        filter_: _OptFilterFn[Message],
        middleware: _OptMid[Message],
    ) -> _RegRetDeco[Message]:
        def inner(fn: AnyHandlerFn) -> MsgHandler:
            handler = MsgHandler(fn, observer, filter_, middleware)
            if MessageFlags.SENT in subtypes:
                self._set.sent_message_handlers.append(handler)
            if MessageFlags.EDITED in subtypes:
                self._set.edited_message_handlers.append(handler)

            return handler

        return inner

    def __call__(
        self,
        subtypes: MessageFlags,
        filter_: _OptFilterFn[Message] = None,
        observer: bool = False,
        middleware: _OptMid[Message] = None,
    ) -> _RegRetDeco[Message]:
        return self._register(observer, subtypes, filter_, middleware)

    def sent(
        self,
        filter_: _OptFilterFn[Message] = None,
        observer: bool = False,
        middleware: _OptMid[Message] = None,
    ) -> _RegRetDeco[Message]:
        return self._register(
            observer, MessageFlags.SENT, filter_, middleware
        )

    def edited(
        self,
        filter_: _OptFilterFn[Message] = None,
        observer: bool = False,
        middleware: _OptMid[Message] = None,
    ) -> _RegRetDeco[Message]:
        return self._register(
            observer, MessageFlags.EDITED, filter_, middleware
        )
