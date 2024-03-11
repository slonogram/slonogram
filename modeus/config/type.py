from typing import Literal, TypeAlias as TAlias
from dataclasses import dataclass

from ..spec import Field

@dataclass
class Described:
    description: list[str]

@dataclass(slots=True)
class Struct(Described):
    fields: dict[str, Field]

    kind: Literal['struct'] = 'struct'

@dataclass(slots=True)
class TypeAlias(Described):
    union: list[str]

    kind: Literal['type-alias'] = 'type-alias'

@dataclass(slots=True)
class Enum(Described):
    variants: dict[str, str]

    kind: Literal['enum'] = 'enum'

AnyType: TAlias = Struct | TypeAlias | Enum 

__all__ = [
    "Struct",
    "TypeAlias",
    "Enum",
    "AnyType",
]
