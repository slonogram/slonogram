from __future__ import annotations

from functools import reduce
from typing import Sequence
from dataclasses import dataclass, field
from abc import ABCMeta, abstractmethod


def _prefer(v: set[str] | None, otherwise: set[str]) -> set[str]:
    if v is None:
        return otherwise
    return v


BUILTINS = {
    "True",
    "False",
    "None",
    "int",
    "str",
    "float",
    "list",
    "set",
}
TYPING = {
    "BinaryIO",
    "Any",
    "Awaitable",
}


@dataclass(slots=True, frozen=True)
class TypeRefs:
    builtins: set[str] = field(default_factory=set)
    typing: set[str] = field(default_factory=set)

    external: set[str] = field(default_factory=set)

    def __or__(self, rhs: TypeRefs) -> TypeRefs:
        return TypeRefs(
            builtins=self.builtins | rhs.builtins,
            typing=self.typing | rhs.typing,
            external=self.external | rhs.external,
        )

    def copy_with(
        self,
        builtins: set[str] | None = None,
        typing: set[str] | None = None,
        external: set[str] | None = None,
    ) -> TypeRefs:
        return TypeRefs(
            builtins=_prefer(builtins, self.builtins),
            typing=_prefer(typing, self.typing),
            external=_prefer(external, self.external),
        )


class TypeHint(metaclass=ABCMeta):
    @property
    def optional(self) -> Optional:
        return Optional(self)

    def __or__(self, rhs: TypeHint) -> Union:
        return Union([self, rhs])

    def __repr__(self) -> str:
        return self.translate()

    @abstractmethod
    def translate(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def collect_refs(self) -> TypeRefs:
        raise NotImplementedError


class Any(TypeHint):
    def translate(self) -> str:
        return "Any"

    def collect_refs(self) -> TypeRefs:
        return TypeRefs(typing={"Any"})


class List(TypeHint):
    def __init__(self, type: TypeHint) -> None:
        self.type = type

    def translate(self) -> str:
        return f"list[{self.type.translate()}]"

    def collect_refs(self) -> TypeRefs:
        return self.type.collect_refs() | TypeRefs(builtins={"list"})


class Union(TypeHint):
    def __init__(self, variants: Sequence[TypeHint]) -> None:
        if len(variants) == 0:
            raise TypeError("Union requires at least one element")

        self.variants = variants

    def translate(self) -> str:
        return " | ".join(n.translate() for n in self.variants)

    def collect_refs(self) -> TypeRefs:
        return (
            reduce(
                lambda lhs, rhs: lhs | rhs,
                map(lambda x: x.collect_refs(), self.variants),
            )
            | TypeRefs()
        )

    def __or__(self, rhs: TypeHint) -> Union:
        return Union([*self.variants, rhs])


class Optional(TypeHint):
    def __init__(self, tp: TypeHint) -> None:
        self.tp = tp

    def translate(self) -> str:
        return f"{self.tp.translate()} | None"

    def collect_refs(self) -> TypeRefs:
        return self.tp.collect_refs()


class Ref(TypeHint):
    def __init__(self, name: str) -> None:
        self.name = name

    def translate(self) -> str:
        return self.name

    def collect_refs(self) -> TypeRefs:
        if self.name in BUILTINS:
            return TypeRefs(builtins={self.name})
        elif self.name in TYPING:
            return TypeRefs(typing={self.name})
        return TypeRefs(external={self.name})
