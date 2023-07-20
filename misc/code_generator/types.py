from yaml import safe_load  # type: ignore
from adaptix import Retort
from pathlib import Path
from typing import Dict, NewType, TypeAlias, List
from dataclasses import dataclass, field

RETORT = Retort()

AbsolutePath = NewType("AbsolutePath", str)
Ty = NewType("Ty", str)

Alias: TypeAlias = str
RenameValue: TypeAlias = str


@dataclass
class Field:
    name: str
    types: List[str]
    required: bool
    description: str


@dataclass
class Type:
    name: str
    href: str
    description: List[str]
    fields: List[Field] = field(default_factory=list)


@dataclass
class Spec:
    types: Dict[str, Type]


@dataclass
class EnumsConfig:
    types: Dict[Ty, List[Alias] | Dict[Alias, RenameValue]]
    overrides: Dict[AbsolutePath, Ty]


@dataclass
class CodegenerationConfig:
    enums: EnumsConfig
    renames: Dict[AbsolutePath, RenameValue]

    @classmethod
    def read_from(cls, path: Path) -> "CodegenerationConfig":
        d = safe_load(open(path, "r"))
        return RETORT.load(d, cls)
