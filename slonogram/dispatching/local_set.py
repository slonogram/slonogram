from __future__ import annotations
from typing import Optional, List, TypeVar, Any, Set

from ..schemas import UpdateType, Message, InlineQuery, CallbackQuery
from ..types.middleware import MiddlewareFn
from ..types.filter import FilterFn

from ..handling.handler import Handler
from ._registrants import OnMessage, OnCallback, OnInline

T = TypeVar("T")


class LocalSet:
    def __init__(
        self,
        name: Optional[str] = None,
        filter_: Optional[FilterFn[Any]] = None,
        middleware: Optional[MiddlewareFn[Any]] = None,
    ) -> None:
        self.name = name

        self._children: List[LocalSet] = []
        self.filter_ = filter_

        self.sent_message_handlers: List[Handler[Message]] = []
        self.edited_message_handlers: List[Handler[Message]] = []
        self.callback_handlers: List[Handler[CallbackQuery]] = []
        self.inline_handlers: List[Handler[InlineQuery]] = []

        self._middleware = middleware

    def collect_update_types(self) -> Set[UpdateType]:
        tps: Set[UpdateType] = set()
        if self.sent_message_handlers:
            tps.add(UpdateType.MESSAGE)
        if self.edited_message_handlers:
            tps.add(UpdateType.EDITED_MESSAGE)
        if self.callback_handlers:
            tps.add(UpdateType.CALLBACK_QUERY)
        if self.inline_handlers:
            tps.add(UpdateType.INLINE_QUERY)

        for child in self._children:
            tps.update(child.collect_update_types())
        return tps

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_inline(self) -> OnInline:
        return OnInline(self)

    @property
    def on_callback(self) -> OnCallback:
        return OnCallback(self)

    @property
    def on_message(self) -> OnMessage:
        return OnMessage(self)
