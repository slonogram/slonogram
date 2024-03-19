from dataclasses import dataclass
from typing import (
    dataclass_transform,
    TypeVar,
    Type,
    Iterable,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from slonogram.handling.activation import Activation

T = TypeVar("T")

@dataclass_transform()
def model(cls: Type[T]) -> Type[T]:
    return dataclass(slots=True)(cls)


def flatten(iter: Iterable[Iterable[T]]) -> tuple[T, ...]:
    mut: list[T] = []
    for collection in iter:
        mut.extend(collection)

    return tuple(mut)

async def stalled() -> "Activation":
    from slonogram.handling.activation import Activation

    return Activation.stalled()

__all__ = ["model", "flatten"]
