from typing import Type, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def assert_value_subtype(subtype: Type[T], value: T) -> None:
    _ = subtype
    _ = value
