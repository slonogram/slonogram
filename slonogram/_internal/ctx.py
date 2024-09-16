from __future__ import annotations

import typing as t
import dataclasses as dtc

from .stash import Stash
from .alter import Alter1, alter1
from .omit import Omittable, OMIT

D = t.TypeVar("D")
A = t.TypeVar("A")
Memo: t.TypeAlias = dict[t.Any, t.Any]


@dtc.dataclass(slots=True)
class Ctx(t.Generic[D]):
    data: D
    memo: Memo = dtc.field(default_factory=dict)
    stash: Stash = dtc.field(default_factory=Stash)

    def with_data(self, data: A) -> Ctx[A]:
        return dtc.replace(self, data=data)  # type: ignore

    def mut(self) -> t.Self:
        """Returns context instance which is safe to mutate."""
        return self.alter(stash=lambda old: Stash() ** old)

    def alter(
        self,
        *,
        data: Omittable[Alter1[D]] = OMIT,
        memo: Omittable[Alter1[Memo]] = OMIT,
        stash: Omittable[Alter1[Stash]] = OMIT,
    ) -> t.Self:
        return type(self)(
            data=alter1(self.data, data),
            memo=alter1(self.memo, memo),
            stash=alter1(self.stash, stash),
        )


__all__ = ["Ctx"]
