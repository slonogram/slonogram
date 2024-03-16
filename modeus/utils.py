from textwrap import indent as _indent
from keyword import kwlist


def escape_kw(ident: str) -> str:
    if ident in kwlist:
        return ident + '_'
    return ident

def indent(text: str) -> str:
    return _indent(text, " " * 4)


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
    "escape_kw",
]
