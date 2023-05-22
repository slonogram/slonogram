from typing import Optional, List, Self


class LocalSet:
    def __init__(self, name: Optional[str] = None) -> None:
        self._name = name
        self._sets: List[Self] = []

    @property
    def name(self) -> Optional[str]:
        return self._name


__all__ = ["LocalSet"]
