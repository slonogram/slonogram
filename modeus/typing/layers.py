from .tracking import Tracker
from typing import Protocol, Generic, Callable, TypeVar

L = TypeVar("L", bound=Tracker)
R = TypeVar("R", bound=Tracker)

class TrackingMapper(Protocol):
    def __call__(
        self,
        source: str,
        name: str,
        tracker: Tracker,
        /,
    ) -> str | None:
        ...

def do_not_track(source: str, predicate: Callable[[str], bool]) -> TrackingMapper:
    def inner(call_source: str, name: str, _: Tracker) -> str | None:
        if call_source == source and predicate(name):
            return name
        return None
    
    return inner

def map_item(source: str, mapper: Callable[[str, Tracker], str]) -> TrackingMapper:
    def inner(call_source: str, name: str, tracker: Tracker) -> str | None:
        if call_source == source:
            return mapper(name, tracker)

        return None
    
    return inner

class CollectBoth(Tracker, Generic[L, R]):
    __slots__ = ("left", "right")
    
    def __init__(self, left: L, right: R) -> None:
        self.left = left
        self.right = right

    def __call__(self, source: str, name: str) -> str:
        self.left(source, name)
        return self.right(source, name)


class AndMappable(Tracker):
    __slots__ = ("inner", )
    
    def __init__(self, inner: Tracker) -> None:
        self.inner = inner
    
    def __and__(self, rhs: TrackingMapper) -> 'MapTracker':
        return MapTracker(self, rhs)

    def __call__(self, source: str, name: str) -> str:
        return self.inner(source, name)


class MapTracker(AndMappable):
    __slots__ = ("mapper", "tracker")

    def __init__(
        self,
        tracker: Tracker,
        mapper: TrackingMapper,
    ) -> None:
        self.mapper = mapper
        self.tracker = tracker

    def __call__(self, source: str, name: str) -> str:
        ret = self.mapper(source, name, self.tracker)
        if ret is None:
            return self.tracker(source, name)
        return ret


__all__ = [
    "MapTracker",
    "AndMappable",
    "CollectBoth",
    "TrackingMapper",
    "do_not_track",
    "map_item",
]

