from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Generic,
    Any,
)

from .middleware import MiddlewareFn
from ..filtering.types import FilterFn
from ._registrants import OnMessage, MsgHandler

T = TypeVar("T")
D = TypeVar("D")


class LocalSet(Generic[D]):
    def __init__(
        self,
        name: Optional[str] = None,
        filter_: Optional[FilterFn[D, Any]] = None,
        middleware: Optional[MiddlewareFn[D, Any]] = None,
    ) -> None:
        self.name = name

        self._children: List[LocalSet[D]] = []
        self.filter_ = filter_

        self._sent_message_handlers: List[MsgHandler[D]] = []
        self._edited_message_handlers: List[MsgHandler[D]] = []

        self._middleware = middleware

    def include(self, *sets: LocalSet[D]) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> OnMessage[D]:
        return OnMessage(self)
