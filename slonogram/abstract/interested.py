from typing import Protocol, runtime_checkable
from ..types.interest import Interest


@runtime_checkable
class Interested(Protocol):
    def collect_interests(self) -> set[Interest]:
        raise NotImplementedError


__all__ = ["Interested"]
