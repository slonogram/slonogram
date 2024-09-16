from __future__ import annotations

import typing as t

from .alter import Alter1, alter1
from .omit import Omittable, OMIT


A = t.TypeVar("A")


class Stash:
    __slots__ = ("head", "tail")

    head: dict[t.Any, t.Any]
    tail: Stash | None

    def __init__(
        self,
        head: Omittable[dict[t.Any, t.Any]] = OMIT,
        tail: Stash | None = None,
    ) -> None:
        self.head = {} if head is OMIT else head
        self.tail = tail

    # ** was chosen since it's right-associative.
    def __pow__(self, rhs: t.Self | None) -> t.Self:
        if rhs is None:
            return self

        tail = self.tail
        if tail is None:
            return self.alter(tail=lambda _: rhs)

        return self.alter(tail=lambda _: tail**rhs)

    def clear(self) -> None:
        self.head.clear()

    def alter(
        self,
        head: Omittable[Alter1[dict[t.Any, t.Any]]] = OMIT,
        tail: Omittable[Alter1[Stash | None]] = OMIT,
    ) -> t.Self:
        return type(self)(
            head=alter1(self.head, head),
            tail=alter1(self.tail, tail),
        )

    def __repr__(self) -> str:
        return f"Stash(head={self.head!r}, tail={self.tail!r})"

    # Until `TypeForm` implementation -_-.
    @t.overload
    def __getitem__(self, tp: t.Type[A]) -> A: ...

    @t.overload
    def __getitem__(self, tp: t.Any) -> t.Any: ...

    def __getitem__(self, tp: t.Any) -> t.Any:
        try:
            return self.head[tp]
        except KeyError:
            tail = self.tail
            if tail is None:
                raise

            return tail[tp]

    @t.overload
    def __setitem__(self, tp: t.Type[A], value: A) -> None: ...

    @t.overload
    def __setitem__(self, tp: t.Any, value: t.Any) -> None: ...

    def __setitem__(self, tp: t.Any, value: t.Any) -> None:
        self.head[tp] = value
