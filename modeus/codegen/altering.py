from typing import Iterable

from ..utils import escape_kw
from ..spec import Field
from ..type_parser import Tracker, no_tracking, TypeParser, parse_union

from .argument import arg
from .function import create_function

def create_alterer(
    self_name: str,
    fields: Iterable[Field],
    type_parser: TypeParser,
    tracker: Tracker = no_tracking,
) -> str:
    args: list[str] = [arg('self')]
    applies = ""

    for field in sorted(fields, key=lambda x: not x.required):
        tracker('slonogram.omittable', 'Omittable')
        tracker('slonogram.omittable', 'OMIT')
        tracker('slonogram.altering', 'Alterer1')
        tracker('slonogram.altering', 'alter1')

        name = escape_kw(field.name)
        tp = 'Omittable[Alterer1[' + parse_union(type_parser, field.types) + ']]'

        args.append(arg(name, tp, default='OMIT'))
        applies += f"{name}=alter1({name}, self.{name}),"

    return create_function(
        'alter',
        args,
        f"return {self_name}({applies})",
    )

__all__ = ["create_alterer"]
