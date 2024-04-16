from typing import Protocol, runtime_checkable, Iterable, Any, TYPE_CHECKING
from ..types.interest import Interest

if TYPE_CHECKING:
    from ..handling.handler import Handler


@runtime_checkable
class Interested(Protocol):
    def collect_interests(self) -> frozenset[Interest]:
        raise NotImplementedError


def collect_interests(handlers: Iterable['Handler[Any]']) -> frozenset['Interest']:
    interests = set['Interest']()
    for handler in handlers:
        if isinstance(handler, Interested):
            interests.update(handler.collect_interests())

    return frozenset(interests)

__all__ = ["Interested", "collect_interests"]
