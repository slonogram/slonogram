from __future__ import annotations

from typing import Sequence
from functools import reduce

from code_generation.library.type_hint import TypeRefs

from . import indent

from .type_hint import TypeHint
from .statement import Statement, collect_from_all_stmts


class AddRefs(Statement):
    def __init__(self, child: Statement, refs: TypeRefs) -> None:
        self.child = child
        self.refs = refs

    def collect_refs(self) -> TypeRefs:
        return self.child.collect_refs() | self.refs

    def generate(self) -> str:
        return self.child.generate()


class AllExports(Statement):
    def __init__(self, exports: list[str]) -> None:
        self.exports = exports

    def create_definition(self) -> Definition:
        return Definition("__all__", assign="[%s]" % ", ".join(map(repr, self.exports)))

    def generate(self) -> str:
        return self.create_definition().generate()

    def collect_refs(self) -> TypeRefs:
        return self.create_definition().collect_refs()


class MultilineComment(Statement):
    lines: Sequence[str]

    def __init__(self, lines: Sequence[str] | str) -> None:
        if isinstance(lines, str):
            self.lines = (lines,)
        else:
            self.lines = lines

    def generate(self) -> str:
        return "\n".join("# " + line for line in self.lines)


class UseFeature(Statement):
    def __init__(self, name: str) -> None:
        self.name = name

    def generate(self) -> str:
        return f"from __future__ import {self.name}"


class TypeAlias(Statement):
    def __init__(
        self,
        name: str,
        alias_to: TypeHint,
        *,
        doc: str | None = None,
    ) -> None:
        self.name = name
        self.alias_to = alias_to
        self.doc = doc

    def generate(self) -> str:
        out = f"{self.name}: TypeAlias = {self.alias_to.translate()}"
        if self.doc is not None:
            out += "\n" + '"""' + self.doc + '"""'
        return out

    def collect_refs(self) -> TypeRefs:
        return self.alias_to.collect_refs() | TypeRefs.typing({"TypeAlias"})


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

    def collect_refs(self) -> TypeRefs:
        if self.type is None:
            return TypeRefs()
        return self.type.collect_refs()

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

    def collect_refs(self) -> TypeRefs:
        return reduce(
            lambda lhs, rhs: lhs | rhs,
            map(lambda x: x.collect_refs(), self.stmts),
            TypeRefs(),
        )


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

    def collect_refs(self) -> TypeRefs:
        refs = self.then.collect_refs() | collect_from_all_stmts(
            s[1] for s in self.elifs
        )
        if self.else_ is not None:
            refs |= self.else_.collect_refs()

        return refs

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
