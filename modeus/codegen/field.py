from ..spec import Field
from ..typing.parser import TypeParser, parse_union

from ..utils import escape_kw

def create_field(
    field: Field,
    type_parser: TypeParser,
) -> str:
    tp = parse_union(type_parser, field.types)
    name = escape_kw(field.name)
    rest = ""

    if not field.required:
        tp += " | None"
        rest = " = None"

    return (
        f"{name}: {tp}{rest}\n"
        f"''' {field.description} '''"
    )

__all__ = ["create_field"]
