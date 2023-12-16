from typing import TypeVar

from slonogram.abstract.context import AbstractContext
from ._generated_shortcuts import GeneratedShortcuts

from ..filtering.text.state import set_text, grasp_text
from ..schemas import Message

M = TypeVar("M")


class ShortcutsMixin(GeneratedShortcuts[M]):
    def grasp_text(self: AbstractContext[Message]) -> str | None:
        return grasp_text(self)

    def set_text(self: AbstractContext[Message], text: str | None) -> None:
        set_text(self, text)
