from __future__ import annotations

from ..bot import Bot
from .stash import Stash

from ..schemas import Message

from typing import TypeVar, Generic

M = TypeVar("M", covariant=True)


class Context(Generic[M]):
    __slots__ = ("stash", "model", "bot")

    def __init__(
        self,
        stash: Stash,
        model: M,
        bot: Bot,
    ) -> None:
        self.stash = stash
        self.model = model
        self.bot = bot

    def with_stash(self, stash: Stash) -> Context[M]:
        return Context(stash, self.model, self.bot)

    def reply(self: Context[Message]) -> None:
        pass


__all__ = ["Context"]
