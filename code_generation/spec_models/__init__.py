from typing import dataclass_transform, TypeVar, Type
from dataclasses import dataclass

T = TypeVar("T")


@dataclass_transform()
def model(cls: Type[T]) -> Type[T]:
    return dataclass(slots=True, frozen=True)(cls)


__all__ = ["model"]
