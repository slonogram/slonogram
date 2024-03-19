from ..spec import Field
from ..typing.parser import TypeParser, parse_union

from ..utils import escape_kw

from .stmts import create_stmts
from .variable import create_variable
from .docstring import create_docstring

def create_field(
    field: Field,
    type_parser: TypeParser,
) -> str:
    tp = parse_union(type_parser, field.types)
    name = escape_kw(field.name)
    rest = None

    if not field.required:
        tp += " | None"
        rest = "None"

    return create_stmts((
        create_variable(name, type=tp, value=rest),
        create_docstring(field.description)
    ))

__all__ = ["create_field"]
