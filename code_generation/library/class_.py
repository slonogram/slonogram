from typing import Sequence
from . import indent
from .statement import Statement


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
