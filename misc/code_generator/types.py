from yaml import safe_load  # type: ignore
from adaptix import Retort
from pathlib import Path
from typing import Dict, NewType, TypeAlias, List, Set
from dataclasses import dataclass, field

RETORT = Retort()

AbsolutePath = NewType("AbsolutePath", str)
Ty = NewType("Ty", str)

MethodName: TypeAlias = str
Alias: TypeAlias = str
RenameValue: TypeAlias = str


@dataclass
class Field:
    name: str
    types: List[str]
    required: bool
    description: str


@dataclass
class Method:
    name: str
    href: str

    returns: List[str]
    description: List[str]

    subtypes: List[str] = field(default_factory=list)
    subtype_of: List[str] = field(default_factory=list)
    fields: List[Field] = field(default_factory=list)


@dataclass
class Type:
    name: str
    href: str
    description: List[str]
    fields: List[Field] = field(default_factory=list)


@dataclass
class Spec:
    methods: Dict[str, Method]
    types: Dict[str, Type]


@dataclass
class EnumsConfig:
    types: Dict[Ty, List[Alias] | Dict[Alias, RenameValue]]
    overrides: Dict[AbsolutePath, Ty]


@dataclass
class CallGroupsConfig:
    groups: Dict[str, List[MethodName]]
    renames: Dict[str, RenameValue]
    dump: Set[AbsolutePath]
    replace_types: Dict[AbsolutePath, Ty]


@dataclass
class CodegenerationConfig:
    unions: Dict[Ty, List[Ty]]
    enums: EnumsConfig
    call_groups: CallGroupsConfig
    renames: Dict[AbsolutePath, RenameValue]

    @classmethod
    def read_from(cls, path: Path) -> "CodegenerationConfig":
        d = safe_load(open(path, "r"))
        return RETORT.load(d, cls)
