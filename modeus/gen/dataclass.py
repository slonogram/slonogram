from typing import Sequence, Iterable

from ..typing.tracking import Tracker
from ..typing.parser import TypeParser

from ..spec import Field

from .field import create_field
from .docstring import create_docstring
from .class_ import create_class
from .stmts import create_stmts
from .decorator import decorate
from .altering import create_alterer

def create_dataclass(
    name: str,
    docs: str,
    fields: Sequence[Field],
    type_parser: TypeParser,
    tracker: Tracker,
    derive: Iterable[str] | None = None,
) -> str:
    out_fields: list[str] = []
    out_methods: list[str] = []

    for field in sorted(fields, key=lambda field: field.required, reverse=True):
        out_fields.append(create_field(field, type_parser))

    out_methods.append(create_alterer(name, fields, type_parser, tracker=tracker))

    return decorate(
        "%s(slots=True)" % tracker('dataclasses', 'dataclass'),
        create_class(
            name,
            derive=derive,
            body=create_stmts((
                create_docstring(docs),
                create_stmts(out_fields),
                create_stmts(out_methods),
            ))
        )
    )

__all__ = ["create_dataclass"]
