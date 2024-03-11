from adaptix import Retort, loader, P, Chain, name_mapping
from dataclasses import dataclass, field
from typing import Any, Iterable

@dataclass(slots=True, frozen=True)
class Field:
    required: bool
    description: str
    types: list[str] = field(default_factory=list)

@dataclass(slots=True, frozen=True)
class Type:
    href: str
    fields: dict[str, Field] = field(default_factory=dict)

    subtypes: list[str] = field(default_factory=list)
    subtype_of: list[str] = field(default_factory=list)
    description: list[str] = field(default_factory=list)

@dataclass(slots=True, frozen=True)
class Method:
    href: str

    description: list[str]

    returns: list[str]
    args: dict[str, Field] = field(default_factory=dict)

@dataclass(slots=True, frozen=True)
class Specification:
    version: str
    release_date: str

    changelog: str

    types: dict[str, Type]
    methods: dict[str, Method]

def list_to_dict(it: Iterable[dict[Any, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for value in it:
        name = value['name']
        del value['name']

        out[name] = value

    return out

SPEC_RETORT = Retort(
    recipe=[
        name_mapping(Method, map={"args": "fields"}),
        loader(P[Method].args, list_to_dict, Chain.FIRST),
        loader(P[Type].fields, list_to_dict, Chain.FIRST)
    ]
)

__all__ = [
    "Specification",
    "Type",

    "SPEC_RETORT",
]

