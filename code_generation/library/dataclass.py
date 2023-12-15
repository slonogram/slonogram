from typing import Sequence, Iterable, cast

from ..library.type_hint import TypeRefs, collect_all_refs

from .class_ import Class
from .statement import Statement
from .type_hint import TypeHint
from .type_hint.ref_sources import Source
from .simple import Decorated

DTC_SOURCE = Source("dataclasses")


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

    def collect_refs(self) -> TypeRefs:
        return self.type.collect_refs()

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
        tail: Statement | None = None,
    ) -> None:
        self.name = name
        self.fields = fields or []
        self.slots = slots
        self.frozen = frozen
        self.path = path
        self.doc = doc
        self.tail = tail

    def generate(self) -> str:
        body = [
            *cast(Iterable[Statement], self.fields),
        ]
        if self.tail is not None:
            body.append(self.tail)
        return Decorated(
            f"{self.path}(frozen={self.frozen}, slots={self.slots})",
            Class(
                self.name,
                body=body,
                doc=self.doc,
            ),
        ).generate()

    def collect_refs(self) -> TypeRefs:
        refs = TypeRefs({DTC_SOURCE: {"dataclass"}}) | collect_all_refs(
            map(lambda x: x.type, self.fields)
        )
        if self.tail is not None:
            refs |= self.tail.collect_refs()
        return refs
