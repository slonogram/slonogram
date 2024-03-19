from typing import TypeAlias, TypeVar, Callable

T = TypeVar("T")
R = TypeVar("R")


class Omit:
    __slots__ = ()

    def __bool__(self) -> bool:
        return False


Omittable: TypeAlias = T | Omit
OMIT = Omit()


def omitted_or(o: Omittable[T], or_: T) -> T:
    if isinstance(o, Omit):
        return or_
    return o

def map_omitted(o: Omittable[T], f: Callable[[T], R]) -> Omittable[R]:
    if isinstance(o, Omit):
        return OMIT
    return f(o)


__all__ = [
    "Omit",
    "OMIT",
    "Omittable",
    "map_omitted",
    "omitted_or",
]
