import typing as t

from .omit import Omittable, OMIT

T = t.TypeVar("T")


class Alter1(t.Protocol[T]):
    def __call__(self, in_: T, /) -> T: ...


def alter1(value: T, alter: Omittable[Alter1[T]]) -> T:
    if alter is OMIT:
        return value
    return alter(value)


__all__ = ["alter1", "Alter1"]
