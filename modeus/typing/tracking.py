from typing import Protocol, Callable
from functools import wraps


class Tracker(Protocol):
    def __call__(self, source: str, name: str, /) -> str:
        """Track import from `source` and return name which can be used

        :param source: import from where
        :param name: what name to import

        :return: name which can be used somewhere in the code
        """

def apply_source(tracker: Tracker, source: str) -> Callable[[str], str]:
    return wraps(tracker)(lambda name: tracker(source, name))

def no_tracking(source: str, name: str, /) -> str:
    _ = source
    return name


__all__ = [
    "Tracker",
    "apply_source",
    "no_tracking",
]
