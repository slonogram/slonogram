from typing import Protocol, TypeVar, Callable, ParamSpec, Concatenate, Generic, Mapping, Iterable
from functools import wraps

from .utils import to_snake_case

T = TypeVar("T")
R = TypeVar("R")
P = ParamSpec("P")

TrackerT = TypeVar("TrackerT", bound='Tracker')

class Tracker(Protocol):
    def __call__(self, source: str, name: str, /) -> None:
        ...

class TypeParser(Protocol):
    def __call__(self, tp: str, /) -> str:
        ...

def track(func: Callable[P, R], tracker: Tracker) -> Callable[Concatenate[str, str, P], R]:
    def inner(source: str, name: str, *args: P.args, **kwargs: P.kwargs) -> R:
        tracker(source, name)
        return func(*args, **kwargs)
    return inner

def no_tracking(source: str, name: str, /) -> None:
    ...

class DoNotTrackNaive(Generic[TrackerT]):
    def __init__(self, tracker: TrackerT, names: list[str]) -> None:
        self.names = names
        self.tracker = tracker

    def __call__(self, source: str, name: str, /) -> None:
        _, check_name = strip_array(name)
        if check_name in self.names:
            return
        self.tracker(source, name)

_ARRAY_OF = 'Array of'

def parse_union(
    parser: TypeParser,
    tps: Iterable[str],
) -> str:
    result = ' | '.join(map(parser, tps))

    return result

def strip_array(tp: str) -> tuple[int, str]:
    depth = 0
    while tp.startswith(_ARRAY_OF):
        tp = tp[len(_ARRAY_OF):].lstrip()
        depth += 1

    return (depth, tp)

def restore_array_of(depth: int, tp: str) -> str:
    return "Array of " * depth + tp

def rename(
    parser: TypeParser,
    map: Mapping[str, str] | Callable[[str], str | None],
) -> TypeParser:
    if callable(map):
        def inner(name: str) -> str:
            depth, name = strip_array(name)
            mapped = map(name)

            if mapped is not None:
                return mapped
            return parser(restore_array_of(depth, name))
    else:
        def inner(name: str) -> str:
            depth, name = strip_array(name)
            if name in map:
                return map[name]
            return parser(restore_array_of(depth, name))

    return wraps(parser)(inner)

def apply_tracker(tracker: Tracker = no_tracking) -> TypeParser:
    return lambda x: _parse_type(x, tracker)

def _parse_type(tp: str, tracker: Tracker = no_tracking) -> str:
    if tp == "Integer":
        return "int"
    elif tp == "Float":
        return "float"
    elif tp == "Boolean":
        return "bool"
    elif tp == "String":
        return "str"
    elif tp in ('True', 'False'):
        tracker('typing', 'Literal')
        return f'Literal[{tp}]'
    elif tp.startswith(_ARRAY_OF):
        stripped_off = tp[len(_ARRAY_OF):].lstrip()

        return 'list[%s]' % _parse_type(stripped_off, tracker)
    else:
        snaked = to_snake_case(tp)
        tracker('slonogram.schemas', snaked)
        return f"_{snaked}.{tp}"

__all__ = [
    "Tracker",
    "DoNotTrackNaive",
    "TypeParser",
    "no_tracking",
    "track",
    "apply_tracker",
    "parse_union",
    "rename",
]

