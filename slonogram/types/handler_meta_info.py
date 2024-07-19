import typing as t
import dataclasses as dtc

from ..utils.altering import Alterer1, alter1
from ..utils.omit import OMIT, Omittable

from .interest import Interest

@dtc.dataclass(slots=True)
class HandlerMetaInfo:
    interests: frozenset[Interest] = frozenset()

    @classmethod
    def default(cls) -> t.Self:
        return cls()

    def alter(
        self,
        *,
        interests: Omittable[Alterer1[frozenset[Interest]]] = OMIT,
    ) -> t.Self:
        return type(self)(
            interests=alter1(interests, self.interests),
        )

    def combine(self, rhs: t.Self) -> t.Self:
        return self.alter(
            interests=lambda i: i.union(rhs.interests),
        )


__all__ = ["HandlerMetaInfo"]


