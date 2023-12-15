from textwrap import indent as _indent
from typing import Sequence, Iterable, TypeVar

T = TypeVar("T")


class IterableSequence(Sequence[T], Iterable[T]):
    ...


def indent(s: str) -> str:
    return _indent(s, "    ")


__all__ = ["indent"]
