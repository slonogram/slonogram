from typing import TypeVar, Generic

from .stash import Stash
from ..bot import Bot
from ..altering import Alterer1, alter1
from ..omittable import Omittable, OMIT

M = TypeVar("M")
NM = TypeVar("NM")

class Context(Generic[M]):
    __slots__ = (
        "bot",
        "model",
        "stash",
    )

    def __init__(
        self,
        bot: Bot,
        model: M,
        stash: Stash,
    ) -> None:
        self.model = model
        self.stash = stash
        self.bot = bot
    
    def alter(
        self,
        bot: Omittable[Alterer1[Bot]] = OMIT,
        model: Omittable[Alterer1[M]] = OMIT,
        stash: Omittable[Alterer1[Stash]] = OMIT,
    ) -> 'Context[M]':
        return Context(
            bot=alter1(bot, self.bot),
            model=alter1(model, self.model),
            stash=alter1(stash, self.stash),
        )
    
    def with_model(self, new_model: NM) -> 'Context[NM]':
        return Context(self.bot, new_model, self.stash)


__all__ = ["Context"]
