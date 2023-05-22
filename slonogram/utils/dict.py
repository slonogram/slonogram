from typing import (
    TypeVar,
    Dict,
    Iterable,
    Optional,
    Tuple,
    TypeAlias,
    Callable,
    Any,
)

JsonDumper: TypeAlias = Callable[[Any], str]
T = TypeVar("T")
K = TypeVar("K")


def set_if_not_none(
    dict_: Dict[K, Any],
    items: Iterable[
        Tuple[K, Optional[Any]] | Tuple[K, Optional[Any], JsonDumper]
    ],
):
    for key, maybe_value, *dumper in items:
        if maybe_value is not None:
            if dumper:
                (fn,) = dumper
                dict_[key] = fn(maybe_value)
                continue

            dict_[key] = maybe_value
