from dataclasses import dataclass
from typing import Any, TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ..handling.handler import Handler


@dataclass(slots=True)
class Activation:
    handler: "Handler[Any] | None" = None

    @classmethod
    def stalled(cls) -> Self:
        return cls(None)

    def __bool__(self) -> bool:
        return self.handler is not None


__all__ = ["Activation"]
