from typing import Sequence

from ..type_parser import TypeParser, Tracker, no_tracking
from ..spec import Field
from ..utils import indent

from .field import create_field
from .altering import create_alterer

def create_dataclass(
    name: str,
    fields: Sequence[Field],
    type_parser: TypeParser,
    tracker: Tracker = no_tracking,
) -> str:
    tracker('slonogram._internal.utils', 'model')

    out_fields = ""
    out_methods = ""

    for field in fields:
        out_fields += create_field(field, type_parser) + '\n'

    out_methods += create_alterer(name, fields, type_parser, tracker=tracker) + '\n'

    if not fields and not out_methods:
        out_fields = "pass"

    return (
        "@model\n"
        f"class {name}:\n"
        + indent(out_fields)
        + indent(out_methods)
    )

__all__ = ["create_dataclass"]
