from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass(slots=True)
class RevisedConfig(Generic[T]):
    dirty: bool
    file_name: str

    data: T


__all__ = ["RevisedConfig"]
