from typing import Sequence, Iterable, cast

from .class_ import Class
from .statement import Statement
from .type_hint import TypeHint
from .simple import Decorated


class Field(Statement):
    def __init__(
        self,
        name: str,
        type: TypeHint,
        doc: str | None = None,
        default: str | None = None,
    ) -> None:
        self.name = name
        self.type = type
        self.default = default
        self.doc = doc

    def generate(self) -> str:
        out = f"{self.name}: {self.type.translate()}"
        if self.default is not None:
            out += " = " + self.default

        if self.doc is not None:
            out += '\n"""' + self.doc + ' """'

        return out


class Dataclass(Statement):
    def __init__(
        self,
        name: str,
        fields: Sequence[Field] | None = None,
        *,
        doc: str | None = None,
        path: str = "dataclass",
        slots: bool = True,
        frozen: bool = False,
        tail: Sequence[Statement] | None = None,
    ) -> None:
        self.name = name
        self.fields = fields or []
        self.slots = slots
        self.frozen = frozen
        self.path = path
        self.doc = doc
        self.tail = tail

    def generate(self) -> str:
        return Decorated(
            f"{self.path}(frozen={self.frozen}, slots={self.slots})",
            Class(
                self.name,
                body=[
                    *cast(Iterable[Statement], self.fields),
                    *cast(Iterable[Statement], self.tail),
                ],
                doc=self.doc,
            ),
        ).generate()
