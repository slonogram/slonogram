import typing as t
import dataclasses as dtc

from .utils.alter import Alter1, alter1
from .utils.omit import Omittable, OMIT

D = t.TypeVar("D")
Memo: t.TypeAlias = dict[t.Any, t.Any]


@dtc.dataclass(slots=True)
class Ctx(t.Generic[D]):
    data: D
    memo: Memo

    def alter(
        self,
        *,
        data: Omittable[Alter1[D]] = OMIT,
        memo: Omittable[Alter1[Memo]] = OMIT,
    ) -> t.Self:
        return type(self)(
            data=alter1(self.data, data),
            memo=alter1(self.memo, memo),
        )

__all__ = ["Ctx"]


