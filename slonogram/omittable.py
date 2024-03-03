from typing import TypeAlias, TypeVar, TypeGuard

T = TypeVar("T")


class Omit:
    __slots__ = ()

    def __bool__(self) -> bool:
        return False

Omittable: TypeAlias = T | Omit

def omitted_or(o: Omittable[T], or_: T) -> T:
    if isinstance(o, Omit):
        return or_
    return o

__all__ = [
    "Omit",
    "Omittable",
    "omitted_or",
]
