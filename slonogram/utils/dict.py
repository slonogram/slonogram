from typing import TypeVar, Dict, Iterable, Optional, Tuple

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def set_if_not_none(
    dict_: Dict[K, V], items: Iterable[Tuple[K, Optional[V]]]
):
    for key, maybe_value in items:
        if maybe_value is not None:
            dict_[key] = maybe_value
