import typing as t

from .omit import Omittable, OMIT

T = t.TypeVar("T")

KIn = t.TypeVar("KIn", contravariant=True)
KOut = t.TypeVar("KOut", covariant=True)


class MorphingAlterer1(t.Protocol[KIn, KOut]):
    def __call__(self, input: KIn, /) -> KOut:
        ...

class Alterer1(t.Protocol[T], MorphingAlterer1[T, T]):
    ...

def alter1(alterer: Omittable[Alterer1[T]], value: T, /) -> T:
    if alterer is OMIT:
        return value
    return alterer(value)  # type: ignore


__all__ = ["Alterer1", "alter1"]

