from typing import (
    TypeVar,
    TypeAlias,
    Callable,
    Awaitable,
    Optional,
    Type,
    Generic,
)
from abc import ABCMeta, abstractmethod

T = TypeVar("T")
FilterFnReturnTy: TypeAlias = Optional[T] | Awaitable[Optional[T]]


# Mypy crutch
class ExplicitFilter(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, value: T) -> FilterFnReturnTy[T]:
        _ = value
        raise NotImplementedError


FilterFn: TypeAlias = (
    ExplicitFilter[T] | Callable[[T], FilterFnReturnTy[T]]
)


def assert_filter_fn(fn: FilterFn) -> None:
    """
    This function is used to statically
    type-check `FilterFn` interface-compliance,
    for example:
    ```py
    from typing import TypeVar

    T = TypeVar("T")

    def identity(value: T) -> T:
        return value

    def incompatible() -> None:
        pass

    assert_filter_fn(identity) # passes type-check
    assert_filter_fn(incompatible) # fails type-check
    ```
    """
    _ = fn


def assert_instance_filter_fn(ty: Type[FilterFn]) -> None:
    """
    Same as `assert_filter_fn`, but checks type instance compliance instead of
    value
    """
    _ = ty


__all__ = [
    "assert_filter_fn",
    "assert_instance_filter_fn",
    "FilterFn",
]
