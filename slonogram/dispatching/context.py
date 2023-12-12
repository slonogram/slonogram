from __future__ import annotations
from typing import TypeVar

from ..bot import Bot
from .stash import Stash

from .._internal.context_shortcuts import ShortcutsMixin

M = TypeVar("M")


class Context(ShortcutsMixin[M]):
    __slots__ = ("stash", "model", "rpc")

    def __init__(
        self,
        stash: Stash,
        model: M,
        rpc: Bot,
    ) -> None:
        self.stash = stash
        self.model = model
        self.rpc = rpc

    def with_stash(self, stash: Stash) -> Context[M]:
        return Context(stash, self.model, self.rpc)


__all__ = ["Context"]
