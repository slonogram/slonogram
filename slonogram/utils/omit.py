import typing as t

from .singleton import SingletonMeta

T = t.TypeVar("T")

class Omit(metaclass=SingletonMeta):
    def __bool__(self) -> bool:
        raise TypeError("Do not use `Omit` in the boolean context")

OMIT = Omit()
Omittable: t.TypeAlias = T | Omit

__all__ = ["Omit", "Omittable", "OMIT"]

