from __future__ import annotations

from ..utils.omit import Omittable, OMIT

import typing as t

T = t.TypeVar("T")


class NotFoundError(Exception):
    def __init__(self, key: t.Any) -> None:
        self.key = key

        super().__init__(f"Not found {key!r} in the stash")


class Stash:
    __slots__ = ('parent', 'heap')

    parent: Stash | None
    heap: dict[t.Any, t.Any]

    def __init__(
        self,
        parent: Omittable[Stash] = OMIT,
        heap: Omittable[dict[t.Any, t.Any]] = OMIT,
    ) -> None:
        if parent is OMIT:
            self.parent = Stash()
        else:
            self.parent = parent  # type: ignore

    @t.overload
    def __getitem__(self, tp: t.Type[T]) -> T:
        ...

    @t.overload
    def __getitem__(self, tp: t.Any) -> t.Any:
        ...

    def __getitem__(self, tp: t.Any) -> t.Any:
        try:
            return self.heap[tp]
        except KeyError as exc:
            raise NotFoundError(tp) from exc

    @t.overload
    def __setitem__(self, tp: t.Type[T], value: T) -> None:
        ...

    @t.overload
    def __setitem__(self, tp: t.Any, value: t.Any) -> None:
        ...

    def __setitem__(self, tp: t.Any, value: t.Any) -> None:
        self.heap[tp] = value


__all__ = ["Stash", "NotFoundError"]

