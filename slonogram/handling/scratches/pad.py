from __future__ import annotations
from typing import Generic, TypeVar, Dict, Any, Optional
from .scratch import Scratch

T = TypeVar("T")
R = TypeVar("R")


class ScratchPad(Generic[T]):
    __slots__ = ("_scratches", "_model", "_parent")

    def __init__(
        self, model: T, parent: Optional[ScratchPad[T]] = None
    ) -> None:
        self._scratches: Dict[Scratch[T, Any], Any] = {}
        self._model = model
        self._parent = parent

    def scratch(self, scratch: Scratch[T, R], value: R) -> None:
        self._scratches[scratch] = value

    def get(self, scratch: Scratch[T, R]) -> R:
        try:
            return self._scratches[scratch]
        except KeyError:
            parent = self._parent
            if parent is None:
                return scratch(self._model)
            return parent.get(scratch)

    def create_child(self) -> ScratchPad[T]:
        return ScratchPad(self._model, self)

    def clear(self) -> None:
        self._scratches.clear()
