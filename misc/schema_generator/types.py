from dataclasses import dataclass, field
from typing import List, Dict


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
