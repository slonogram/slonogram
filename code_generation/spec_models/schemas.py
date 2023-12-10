from . import model
from dataclasses import field


@model
class Field:
    name: str
    required: bool
    description: str

    types: list[str] = field(default_factory=list)


@model
class Model:
    name: str
    href: str
    description: list[str] = field(default_factory=list)

    fields: list[Field] = field(default_factory=list)
    subtypes: list[str] = field(default_factory=list)
