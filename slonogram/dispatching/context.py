from typing import TypeVar, Generic

from .stash import Stash
from ..bot import Bot

M = TypeVar("M")

class Context(Generic[M]):
    __slots__ = ('bot', 'model', 'stash')

    def __init__(
        self,
        bot: Bot,
        model: M,
        stash: Stash,
    ) -> None:
        self.model = model
        self.stash = stash
        self.bot = bot


__all__ = ["Context"]
