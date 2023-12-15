from enum import auto

from . import IterableSequence

from ..library.type_hint import TypeRefs
from ..library.type_hint.ref_sources import Source
from ..library.class_ import Class
from ..library.simple import Definition

from .statement import Statement

ENUM_SOURCE = Source("enum")


def _build_definition(v: str | tuple[str, str]) -> Definition:
    if isinstance(v, str):
        return Definition(v.upper(), assign="auto()")
    return Definition(v[0].upper(), assign=repr(v[1]))


class Enum(Statement):
    def __init__(
        self,
        name: str,
        variants: IterableSequence[str | tuple[str, str]],
        *,
        doc: str | None = None,
    ) -> None:
        self.variants = variants
        self.name = name
        self.doc = doc

    def generate(self) -> str:
        return Class(
            self.name,
            inherits=("StrEnum",),
            doc=self.doc,
            body=[_build_definition(v) for v in self.variants],
        ).generate()

    def collect_refs(self) -> TypeRefs:
        imports = {"StrEnum"}
        if not all(True for v in self.variants if isinstance(v, tuple)):
            imports.add("auto")

        return TypeRefs({ENUM_SOURCE: {"StrEnum"}})
