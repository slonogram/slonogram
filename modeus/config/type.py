from typing import Literal, TypeAlias as TAlias, Protocol
from dataclasses import dataclass

from ..spec import Field

class HasMeta(Protocol):
    meta: 'Meta'

@dataclass
class Meta:
    name: str
    description: list[str]
    href: str


@dataclass(slots=True)
class Struct:
    meta: Meta
    fields: dict[str, Field]

    kind: Literal["struct"] = "struct"


@dataclass(slots=True)
class TaggedUnion:
    meta: Meta
    union: list[str]

    kind: Literal["type-alias"] = "type-alias"


@dataclass(slots=True)
class Enum:
    meta: Meta
    variants: dict[str, str]

    kind: Literal["enum"] = "enum"


AnyType: TAlias = Struct | TaggedUnion | Enum

__all__ = [
    "Struct",
    "TaggedUnion",
    "Enum",
    "AnyType",
    "Meta",
]
