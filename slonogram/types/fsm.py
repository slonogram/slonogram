from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class StorageScope(Generic[T]):
    id: T


class ChatScope(StorageScope[int]):
    ...


class UserScope(StorageScope[int]):
    ...


__all__ = [
    "ChatScope",
    "UserScope",
    "StorageScope",
]
