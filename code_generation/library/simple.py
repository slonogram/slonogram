from typing import Sequence

from . import indent

from .type_hint import TypeHint
from .statement import Statement


class TypeAlias(Statement):
    def __init__(self, name: str, alias_to: TypeHint) -> None:
        self.name = name
        self.alias_to = alias_to

    def generate(self) -> str:
        return f"{self.name}: TypeAlias = {self.alias_to.translate()}"


class Definition(Statement):
    def __init__(
        self,
        name: str,
        type: TypeHint | None = None,
        assign: str | None = None,
    ) -> None:
        self.name = name
        self.type = type
        self.assign = assign

    def generate(self) -> str:
        if self.assign is not None:
            assign = " = " + self.assign
        else:
            assign = ""
        r = f"{self.name}"

        if self.type is not None:
            r += f": {self.type.translate()}"
        return r + assign


class Collection(Statement):
    def __init__(self, stmts: Sequence[Statement]) -> None:
        self.stmts = stmts

    def generate(self) -> str:
        return "\n".join(s.generate() for s in self.stmts)


class FromImport(Statement):
    def __init__(self, from_: str, names: Sequence[str] | str) -> None:
        if isinstance(names, str):
            names = (names,)
        if len(names) == 0:
            raise ValueError("names must not be empty")

        self.from_ = from_
        self.names = names

    def generate(self) -> str:
        return f"from {self.from_} import " + ", ".join(self.names)


class PlainImport(Statement):
    def __init__(self, names: Sequence[str] | None = None) -> None:
        self.names = names or []

    def generate(self) -> str:
        return "import " + ", ".join(self.names)


class Decorated(Statement):
    def __init__(self, expr: str, stmt: Statement) -> None:
        self.expr = expr
        self.stmt = stmt

    def generate(self) -> str:
        return f"@{self.expr}\n{self.stmt.generate()}"


class If(Statement):
    def __init__(
        self,
        cond: str,
        then: Statement,
        elifs: list[tuple[str, Statement]] | None = None,
        else_: Statement | None = None,
    ) -> None:
        self.cond = cond
        self.then = then
        self.elifs = elifs or []
        self.else_ = else_

    def generate(self) -> str:
        out = f"if {self.cond}:\n" + indent(self.then.generate())
        for cond, stmt in self.elifs:
            out += f"\nelif {cond}:\n{indent(stmt.generate())}"

        if self.else_ is not None:
            out += "\nelse:\n" + indent(self.else_.generate())

        return out


class Expr(Statement):
    def __init__(self, expr: str) -> None:
        self.expr = expr

    def generate(self) -> str:
        return self.expr


class Return(Statement):
    def __init__(self, expr: str) -> None:
        self.expr = expr

    def generate(self) -> str:
        return f"return {self.expr}"
