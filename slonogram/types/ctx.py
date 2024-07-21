from __future__ import annotations

import typing as t
import dataclasses as dtc

from .stash import Stash

from ..utils.omit import Omittable, OMIT
from ..utils.altering import Alterer1, alter1

from ..bot import Bot


D = t.TypeVar("D")
NewData = t.TypeVar("NewData")
Memo: t.TypeAlias = dict[t.Any, t.Any]

@dtc.dataclass(slots=True)
class Ctx(t.Generic[D]):
    data: D
    bot: Bot

    memo: Memo = dtc.field(default_factory=dict)
    stash: Stash = dtc.field(default_factory=Stash)

    def with_data(self, data: NewData) -> Ctx[NewData]:
        return Ctx(
            data=data,
            stash=self.stash,
            memo=self.memo,
            bot=self.bot,
        )

    def alter(
        self,
        data: Omittable[Alterer1[D]] = OMIT,
        stash: Omittable[Alterer1[Stash]] = OMIT,
        memo: Omittable[Alterer1[Memo]] = OMIT,
        bot: Omittable[Alterer1[Bot]] = OMIT,
    ) -> Ctx[D]:
        return Ctx(
            data=alter1(data, self.data),
            stash=alter1(stash, self.stash),
            memo=alter1(memo, self.memo),
            bot=alter1(bot, self.bot),
        )


__all__ = ["Ctx"]


