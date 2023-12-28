"""
Higher order functions utilities
"""

from typing import (
    TypeVar,
    Generic,
    Protocol,
    Callable,
    Concatenate,
    ParamSpec,
    TypeAlias,
    Any,
)
from types import EllipsisType

T = TypeVar("T")
R = TypeVar("R")
Head = TypeVar("Head")
Marker = TypeVar("Marker")

T_contra = TypeVar("T_contra", contravariant=True)
Marker_co = TypeVar("Marker_co", covariant=True)
Tail = ParamSpec("Tail")


class Alter1Marker(Protocol[T_contra, Marker_co]):
    def __call__(self, input: T_contra, /) -> T_contra | Marker_co:
        ...


Alter1: TypeAlias = Alter1Marker[T_contra, T_contra]


def unset(_: Any) -> None:
    return None


def apply1(f: Callable[Concatenate[Head, Tail], R], value: Head) -> Callable[Tail, R]:
    return lambda *rest, **kwrest: f(value, *rest, **kwrest)


def alter1(alterer: Alter1[T] | None, apply: T) -> T:
    if alterer is None:
        return apply
    return alterer(apply)


def alter1_ellipsis(
    alterer: Alter1Marker[T | None, EllipsisType] | None,
    apply: T | None,
) -> T | None:
    if alterer is None:
        return apply

    if (result := alterer(apply)) is not ...:
        return result
    return None


class Const(Generic[T]):
    __slots__ = ("value",)
    __name__ = "const"

    def __init__(self, value: T) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.__name__}({self.value!r})"

    def __call__(self, _: Any) -> T:
        return self.value


__all__ = [
    "Const",
    "Alter1",
    "Alter1Marker",
    "alter1",
    "alter1_ellipsis",
    "apply1",
    "unset",
]
