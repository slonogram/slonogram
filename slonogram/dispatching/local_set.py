from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Any,
)

from ..types.middleware import MiddlewareFn
from ..types.filter import FilterFn
from ._registrants import OnMessage, MsgHandler

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

        self._sent_message_handlers: List[MsgHandler] = []
        self._edited_message_handlers: List[MsgHandler] = []

        self._middleware = middleware

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> OnMessage:
        return OnMessage(self)
