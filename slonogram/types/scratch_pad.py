from __future__ import annotations
from copy import copy
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

    def copy(self) -> ScratchPad[T]:
        """
        Returns new `ScratchPad` with exact same parameters, but
        scratches dict is copied, so scratches modification will not
        affect original `ScratchPad`
        """

        pad = ScratchPad(self._model, self._parent)
        pad._scratches = copy(self._scratches)
        return pad

    def __repr__(self) -> str:
        return (
            f"<ScratchPad scratches={self._scratches!r} "
            f"parent={self._parent!r}>"
        )

    def __setitem__(self, scratch: Scratch[T, R], value: R) -> None:
        self._scratches[scratch] = value

    def __getitem__(self, scratch: Scratch[T, R]) -> R:
        try:
            return self._scratches[scratch]
        except KeyError:
            parent = self._parent
            if parent is None:
                return scratch(self._model)
            return parent[scratch]

    def create_child(self) -> ScratchPad[T]:
        return ScratchPad(self._model, self)

    def clear(self) -> None:
        self._scratches.clear()
