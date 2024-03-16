from dataclasses import dataclass
from typing import dataclass_transform, TypeVar, Type

T = TypeVar("T")


@dataclass_transform()
def model(cls: Type[T]) -> Type[T]:
    return dataclass(slots=True)(cls)


__all__ = ["model"]
