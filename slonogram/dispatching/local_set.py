from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Generic,
    Any,
)

from ..filtering.types import FilterFn
from ._registrants import OnMessage, MsgHandler

T = TypeVar("T")
D = TypeVar("D")


class LocalSet(Generic[D]):
    def __init__(
        self,
        name: Optional[str] = None,
        filter_: Optional[FilterFn[D, Any]] = None,
    ) -> None:
        self.name = name

        self._children: List[LocalSet] = []
        self.filter_ = filter_

        self._sent_message_handlers: List[MsgHandler[D]] = []
        self._edited_message_handlers: List[MsgHandler[D]] = []

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> OnMessage[D]:
        return OnMessage(self)
