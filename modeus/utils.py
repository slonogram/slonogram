from .spec import Type

from textwrap import indent as _indent
from keyword import kwlist

def lines(*s: str) -> str:
    return "\n".join(s)

def escape_kw(ident: str) -> str:
    if ident in kwlist:
        return ident + '_'
    return ident

def indent(text: str) -> str:
    return _indent(text, " " * 4)

def get_schema_module(types: dict[str, Type], type_name: str) -> str:
    tp = types[type_name]
    try:
        parent = tp.subtype_of[0]
    except IndexError:
        return to_snake_case(type_name)
    
    return to_snake_case(parent)

def to_snake_case(value: str) -> str:
    out = ""
    if value[0].isupper():
        out += value[0].lower()
        value = value[1:]

    for char in value:
        if char.isupper():
            out += "_" + char.lower()
        else:
            out += char

    return out


__all__ = [
    "to_snake_case",
    "indent",
    "get_schema_module",
    "escape_kw",
    "lines",
]
