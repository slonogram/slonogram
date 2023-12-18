from __future__ import annotations
from ..exceptions.stash import NoItemInStash

from typing import Type, Any, Self, TypeVar, Callable

T = TypeVar("T")


class Stash:
    __slots__ = ("types", "parent")

    parent: Stash | None
    types: dict[Type[Any], Any]

    def __init__(
        self,
        types: dict[Any, Any] | None = None,
        *,
        parent: Self | None = None,
    ) -> None:
        if types is None:
            self.types = {}
        else:
            self.types = types

        self.parent = parent

    def __repr__(self) -> str:
        return f"Stash({self.types!r}, parent={self.parent!r})"

    @classmethod
    def single(
        self,
        type: Any,
        value: T,
        *,
        parent: Stash | None = None,
    ) -> Stash:
        return Stash({type: value}, parent=parent)

    def __getitem__(self, tp: Type[T]) -> T:
        """Gets item from the stash

        :name tp: type of the value
        :raises: `slonogram.exceptions.stash.NoItemInStash` if there's no such item in stash

        :returns: `T`
        """
        try:
            return self.types[tp]  # type: ignore
        except KeyError as e:
            parent = self.parent
            if parent is None:
                raise NoItemInStash(tp) from e
            return parent[tp]

    def __setitem__(self, tp: Type[T], value: T) -> None:
        self.types[tp] = value

    def alter(self, tp: Type[T], f: Callable[[T], T]) -> None:
        """Morphs value with type `tp`

        :name tp: type of the value
        :name f: morphing function

        :raises: `slonogram.exceptions.no_item_in_stash.NoItemInStash` if there's no such item in stash

        :return: `None`
        """
        self[tp] = f(self[tp])


__all__ = ["Stash"]
