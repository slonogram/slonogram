from typing import TypeVar, Protocol

from ..omittable import Omittable, Omit

T = TypeVar("T")


class Alterer1(Protocol[T]):
    def __call__(self, value: T, /) -> T:
        ...


def alter1(alterer: Omittable[Alterer1[T]], otherwise: T) -> T:
    if isinstance(alterer, Omit):
        return otherwise
    return alterer(otherwise)


__all__ = ["Alterer1", "alter1"]
