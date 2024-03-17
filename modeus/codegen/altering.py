from typing import Iterable

from ..utils import escape_kw
from ..spec import Field

from ..typing.tracking import Tracker
from ..typing.parser import TypeParser, parse_union

from .argument import arg
from .function import create_function

def create_alterer(
    self_name: str,
    fields: Iterable[Field],
    type_parser: TypeParser,
    tracker: Tracker,
) -> str:
    args: list[str] = [arg('self')]
    applies = ""

    for field in sorted(fields, key=lambda x: not x.required):
        name = escape_kw(field.name)
        type_ = parse_union(type_parser, field.types)
        if not field.required:
            type_ += ' | None'

        tp = "{omittable}[{alterer1}[{type}]]".format(
            omittable=tracker('slonogram.omittable', 'Omittable'),
            alterer1=tracker('slonogram.altering', 'Alterer1'),
            type=type_,
        )

        args.append(arg(name, tp, default=tracker('slonogram.omittable', 'OMIT')))
        applies += "{name}={alter1}({name}, self.{name}),".format(
            name=name,
            alter1=tracker('slonogram.altering', 'alter1'),
        )

    return create_function(
        'alter',
        args,
        f"return {self_name}({applies})",
        ret_annot=self_name
    )

__all__ = ["create_alterer"]
