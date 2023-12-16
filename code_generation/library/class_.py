from typing import Sequence

from code_generation.library.type_hint import TypeRefs
from . import indent
from .statement import Statement, collect_from_all_stmts


class Class(Statement):
    def __init__(
        self,
        name: str,
        *,
        doc: str | None = None,
        inherits: Sequence[str] | None = None,
        body: Sequence[Statement] | None = None,
    ) -> None:
        self.name = name
        self.inherits = inherits or []
        self.body = body or []
        self.doc = doc

    def collect_refs(self) -> TypeRefs:
        return collect_from_all_stmts(self.body or [])

    def generate(self) -> str:
        stmts = "\n".join(stmt.generate() for stmt in self.body)
        if self.inherits:
            inheritance = "(" + ", ".join(self.inherits) + ")"
        else:
            inheritance = ""

        if not stmts:
            stmts = "pass"

        if self.doc is not None:
            doc = indent('"""' + self.doc + ' """\n')
        else:
            doc = ""

        return f"class {self.name}{inheritance}:\n{doc}" + indent(stmts)
