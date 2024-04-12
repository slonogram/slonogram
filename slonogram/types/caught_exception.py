from typing import TypeVar, Generic
from dataclasses import dataclass

from ..handling.handler import Handler

M = TypeVar("M")
E = TypeVar("E", bound=Exception)

@dataclass(slots=True)
class CaughtException(Generic[M, E]):
    model: M
    exc: E
    handler: Handler[M]


__all__ = ["CaughtException"]

