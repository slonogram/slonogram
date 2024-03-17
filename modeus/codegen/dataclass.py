from typing import Sequence

from ..typing.tracking import Tracker
from ..typing.parser import TypeParser

from ..spec import Field
from ..utils import indent

from .field import create_field
from .altering import create_alterer

def create_dataclass(
    name: str,
    docs: str,
    fields: Sequence[Field],
    type_parser: TypeParser,
    tracker: Tracker,
) -> str:
    out_fields = ""
    out_methods = ""

    for field in sorted(fields, key=lambda field: field.required, reverse=True):
        out_fields += create_field(field, type_parser) + '\n'

    out_methods += create_alterer(name, fields, type_parser, tracker=tracker) + '\n'

    if not fields and not out_methods:
        out_fields = "pass"

    return (
        f"@{tracker('slonogram._internal.utils', 'model')}\n"
        f"class {name}:\n"
        + indent(f'""" {docs} """')
        + '\n'
        + indent(out_fields)
        + indent(out_methods)
    )

__all__ = ["create_dataclass"]
