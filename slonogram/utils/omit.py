import typing as t

from .singleton import SingletonMeta

T = t.TypeVar("T")

class Omit(metaclass=SingletonMeta):
    def __bool__(self) -> bool:
        raise TypeError("Do not use `Omit` in the boolean context")

OMIT = Omit()
Omittable: t.TypeAlias = T | Omit

def non_omitted_or(val: Omittable[T], or_: T) -> T:
    return or_ if val is OMIT else or_


__all__ = ["Omit", "Omittable", "OMIT", "non_omitted_or"]

