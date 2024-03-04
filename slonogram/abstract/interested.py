from typing import Protocol, runtime_checkable
from ..types.interests import Interests


@runtime_checkable
class Interested(Protocol):
    def collect_interests(self) -> Interests:
        raise NotImplementedError


__all__ = ["Interested"]
