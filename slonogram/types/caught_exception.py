from typing import TypeVar, Generic
from dataclasses import dataclass

M = TypeVar("M")
E = TypeVar("E", bound=Exception)

@dataclass(slots=True)
class CaughtException(Generic[M, E]):
    model: M
    exc: E


__all__ = ["CaughtException"]

