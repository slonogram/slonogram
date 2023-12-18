from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass
from typing import Generic, TypeVar

if TYPE_CHECKING:
    from .handler import Handler

M = TypeVar("M")


@dataclass(slots=True)
class Activation(Generic[M]):
    handler: Handler[M] | None = None

    @classmethod
    def ignored(cls) -> Activation[M]:
        return Activation(None)

    @classmethod
    def activated(cls, handler: Handler[M]) -> Activation[M]:
        return Activation(handler)

    @property
    def is_activated(self) -> bool:
        return self.handler is not None
