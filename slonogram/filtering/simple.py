from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context

from .base import ExtendedFilter


class Const(ExtendedFilter[Any]):
    __slots__ = ("value",)

    def __init__(self, value: bool) -> None:
        self.value = value

    def __repr__(self) -> str:
        return repr(self.value)

    def __call__(self, _: Context[Any]) -> bool:
        return self.value


__all__ = ["Const"]
