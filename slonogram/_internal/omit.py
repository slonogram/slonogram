import typing as t
from enum import IntEnum


class Omit(IntEnum):
    OMIT = 1


T = t.TypeVar("T")
Omittable: t.TypeAlias = T | Omit
OMIT = Omit.OMIT

__all__ = ["Omit", "Omittable", "OMIT"]
