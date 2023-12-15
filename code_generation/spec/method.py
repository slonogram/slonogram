from functools import lru_cache
from dataclasses import dataclass

from ..library.type_hint import TypeHint
from .utils import to_snake_case


@dataclass
class Argument:
    name: str
    type: TypeHint
    doc: str

    required: bool
    default: str | None = None


@dataclass
class Method:
    name: str
    doc: str
    href: str

    args: list[Argument]
    return_type: TypeHint

    @property
    @lru_cache
    def snake_name(self) -> str:
        return to_snake_case(self.name)
