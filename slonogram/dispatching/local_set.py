from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Any,
    Set
)

from ..schemas import UpdateType
from ..types.middleware import MiddlewareFn
from ..types.filter import FilterFn
from ._registrants import OnMessage, OnCallback, MsgHandler, CbHandler

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

        self.sent_message_handlers: List[MsgHandler] = []
        self.edited_message_handlers: List[MsgHandler] = []
        self.callback_handlers: List[CbHandler] = []

        self._middleware = middleware

    def collect_update_types(self) -> Set[UpdateType]:
        tps: Set[UpdateType] = set()
        if self.sent_message_handlers:
            tps.add(UpdateType.MESSAGE)
        if self.edited_message_handlers:
            tps.add(UpdateType.EDITED_MESSAGE)
        if self.callback_handlers:
            tps.add(UpdateType.CALLBACK_QUERY)

        for child in self._children:
            tps.update(child.collect_update_types())
        return tps

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_callback(self) -> OnCallback:
        return OnCallback(self)

    @property
    def on_message(self) -> OnMessage:
        return OnMessage(self)
