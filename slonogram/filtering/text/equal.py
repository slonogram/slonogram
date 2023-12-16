from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context

from slonogram.schemas import Message
from slonogram.filtering.base import ExtendedFilter


class Equal(ExtendedFilter[Message]):
    __slots__ = ("text",)

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return f"== {self.text!r}"

    def __call__(self, ctx: Context[Message]) -> bool:
        return self.text == ctx.grasp_text()


__all__ = ["Equal"]
