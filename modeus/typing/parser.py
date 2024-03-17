from typing import Protocol, Iterable
from functools import wraps, partial

from .tracking import Tracker

_ARRAY_OF = "Array of"
def unwrap_arrays(tp: str) -> tuple[int, str]:
    depth = 0
    while tp.startswith(_ARRAY_OF):
        tp = tp[len(_ARRAY_OF):].lstrip()
        depth += 1

    return depth, tp

def restore_arrays(depth: int, tp: str) -> str:
    return "Array of " * depth + tp

def wrap_list(depth: int, tp: str) -> str:
    if depth <= 0:
        return tp
    return 'tuple[%s, ...]' % wrap_list(depth - 1, tp)

class TypeParser(Protocol):
    def __call__(self, tp: str, /) -> str:
        ...

def apply_tracker(tracker: Tracker) -> TypeParser:
    return wraps(parse_type)(partial(parse_type, tracker))

def parse_type(tracker: Tracker, tp: str) -> str:
    if tp == "Integer":
        return "int"
    elif tp == "Boolean":
        return "bool"
    elif tp in ("True", "False"):
        return f"{tracker('typing', 'Literal')}[{tp}]"
    elif tp == "Float":
        return "float"
    elif tp == "String":
        return "str"
    elif tp.startswith(_ARRAY_OF):
        depth, inner = unwrap_arrays(tp)
        return wrap_list(depth, parse_type(tracker, inner))

    return tracker('<schemas>', tp)

def parse_union(parser: TypeParser, un: Iterable[str]) -> str:
    return " | ".join(map(parser, un))

__all__ = [
    "TypeParser",
    "parse_type",
    "apply_tracker",
    "parse_union",

    "wrap_list",
    "restore_arrays",
    "unwrap_arrays",
]

