from typing import TypeVar, TypeAlias, Callable, Awaitable, Optional, Type

T = TypeVar("T")
FilterFn: TypeAlias = (
    Callable[[T], Optional[T]] | Callable[[T], Awaitable[Optional[T]]]
)


def identity(value: T) -> T:
    """
    identity function(`a -> a`). Useful, for example,
    when every update should be handled
    """
    return value


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


assert_filter_fn(identity)

__all__ = [
    "identity",
    "assert_filter_fn",
    "assert_instance_filter_fn",
    "FilterFn",
]
