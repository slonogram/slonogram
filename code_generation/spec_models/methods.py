from . import model
from dataclasses import field


@model
class Argument:
    name: str
    types: list[str]
    required: bool
    description: str


@model
class Method:
    name: str
    href: str

    description: list[str]
    returns: list[str]
    arguments: list[Argument] = field(default_factory=list)
