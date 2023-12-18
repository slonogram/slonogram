from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from slonogram.schemas import Message
from slonogram.exceptions.stash import NoItemInStash

if TYPE_CHECKING:
    from slonogram.abstract.context import AbstractContext


@dataclass
class TextState:
    text: str | None


def set_text(ctx: AbstractContext[Message], new_text: str | None) -> None:
    ctx.stash[TextState] = TextState(new_text)


def grasp_text(ctx: AbstractContext[Message]) -> str | None:
    try:
        return ctx.stash[TextState].text
    except NoItemInStash:
        return ctx.model.text


__all__ = [
    "TextState",
    "set_text",
    "grasp_text",
]
