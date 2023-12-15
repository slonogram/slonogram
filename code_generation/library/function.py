from functools import reduce
from dataclasses import dataclass

from code_generation.library.type_hint import TypeRefs
from . import indent

from .type_hint import TypeHint
from .type_hint.known_refs import ANY
from .statement import Statement


@dataclass
class Argument:
    name: str
    type: TypeHint | None = None
    default: str | None = None

    def to_str(self) -> str:
        repr_ = self.name
        if self.type is not None:
            repr_ += ": " + self.type.translate()
        if self.default is not None:
            repr_ += " = " + self.default
        return repr_


class Function(Statement):
    def __init__(
        self,
        name: str,
        return_type: TypeHint,
        *,
        doc: str | None = None,
        is_async: bool = False,
        args: list[Argument] | None = None,
        body: list[Statement] | None = None,
        trailing_comma: bool = False,
    ) -> None:
        self.name = name
        self.is_async = is_async
        self.return_type = return_type
        self.body = body or []
        self.args = args or []
        self.trailing_comma = trailing_comma
        self.doc = doc

    def add_arg(
        self,
        name: str,
        *,
        type: TypeHint | None = None,
        default: str | None = None,
    ) -> None:
        if self.args and default is None and self.args[-1].default is not None:
            raise ValueError(
                "Argument without default must not follow argument with it"
            )

        self.args.append(Argument(name, type, default))

    def __repr__(self) -> str:
        return self.generate()

    def collect_refs(self) -> TypeRefs:
        return self.return_type.collect_refs() | reduce(
            lambda lhs, rhs: lhs | rhs,
            map(
                lambda x: x.type.collect_refs() if x.type is not None else TypeRefs(),
                self.args,
            ),
            TypeRefs(),
        )

    def generate(self) -> str:
        async_kw = "async " if self.is_async else ""

        sig = f"{async_kw}def {self.name}("
        sig += ", ".join(map(Argument.to_str, self.args))
        if self.args and self.trailing_comma:
            sig += ","
        sig += f") -> {self.return_type.translate()}:\n"

        stmts = ""
        if self.doc is not None:
            stmts += '"""' + self.doc + '\n"""\n'

        if self.body:
            stmts += "\n".join(s.generate() for s in self.body)
        else:
            stmts += "pass"

        return sig + indent(stmts)


def self_arg() -> Argument:
    return Argument("self")
