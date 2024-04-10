from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..handling.handler import Handler


@dataclass(slots=True)
class Activation:
    handler: "Handler[Any] | None" = None

    @staticmethod
    def stalled() -> 'Activation':
        return _STALLED

    def __bool__(self) -> bool:
        return self.handler is not None

_STALLED = Activation(None)

__all__ = ["Activation"]
