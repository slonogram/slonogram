from typing import Callable, Any, TypeVar, Iterable, TYPE_CHECKING
from ..abstract.interested import collect_interests

if TYPE_CHECKING:
    from .handler import Handler
    from ..types.interest import Interest

S = TypeVar("S")
def auto_collect(f: Callable[[S], Iterable['Handler[Any]']]) -> Callable[[S], set['Interest']]:
    def collector(self: S) -> set['Interest']:
        return collect_interests(f(self))
    return collector

__all__ = ["auto_collect"]


