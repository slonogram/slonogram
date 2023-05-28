from __future__ import annotations
from typing import TypeVar, Optional, Awaitable, cast, Any
from inspect import iscoroutine
from . import assert_instance_filter_fn, FilterFn, ExplicitFilter

T = TypeVar("T")


class ExtendedFilter(ExplicitFilter[T]):
    def __and__(self, right: FilterFn[T]) -> AndThenChain[T]:
        return self.and_then(right)

    def __invert__(self) -> InvertedFilter[T]:
        return self.invert()

    def __or__(self, right: FilterFn[T]) -> OrFilter[T]:
        return self.or_(right)

    def __xor__(self, right: FilterFn[T]) -> OrFilter[T]:
        return self.or_(right, exclusive=True)

    def invert(self) -> InvertedFilter[T]:
        return InvertedFilter(cast(FilterFn[T], self))

    def or_(
        self, right: FilterFn[T], exclusive: bool = False
    ) -> OrFilter[T]:
        return OrFilter(cast(FilterFn[T], self), right, exclusive)

    def and_then(self, right: FilterFn[T]) -> AndThenChain[T]:
        return AndThenChain(cast(FilterFn[T], self), right)


class OrFilter(ExtendedFilter[T]):
    def __init__(
        self, left: FilterFn[T], right: FilterFn[T], exclusive: bool
    ) -> None:
        self._left = left
        self._right = right
        self._exclusive = exclusive

    def __repr__(self) -> str:
        return f"{self._left} {self.sign} {self._right}"

    async def _exclusive_or(self, value: T) -> Optional[T]:
        left: Any = self._left(value)
        right: Any = self._right(value)

        if iscoroutine(left):
            left = await left
        if iscoroutine(right):
            right = await right

        if left is not None:
            if right is not None:
                return None
            return left
        else:
            return right

        return None

    async def _plain_or(self, value: T) -> Optional[T]:
        left: Any = self._left(value)
        if iscoroutine(left):
            left = await left
        if left is not None:
            return left

        right = self._right(value)
        if iscoroutine(right):
            return await right
        else:
            return right  # type: ignore

    def __call__(self, value: T) -> Awaitable[Optional[T]]:
        if self._exclusive:
            return self._exclusive_or(value)
        return self._plain_or(value)

    @property
    def exclusive(self) -> bool:
        return self._exclusive

    @property
    def sign(self) -> str:
        if self._exclusive:
            return "^"
        return "|"


class InvertedFilter(ExtendedFilter[T]):
    def __init__(self, fn: FilterFn[T]) -> None:
        self._fn = fn

    def __repr__(self) -> str:
        return f"~{self._fn!r}"

    def __call__(self, value: T) -> Optional[T]:
        result = self._fn(value)
        if result is None:
            return value
        return None


class AndThenChain(ExtendedFilter[T]):
    def __init__(self, left: FilterFn[T], right: FilterFn[T]) -> None:
        self._left = left
        self._right = right

    def __repr__(self) -> str:
        return f"{self._left} & {self._right}"

    async def __call__(self, value: T) -> Optional[T]:
        left = self._left(value)
        if iscoroutine(left):
            left_res: Optional[T] = await left
        else:
            left_res = left  # type: ignore

        if left_res is None:
            return None

        right = self._right(left_res)
        if iscoroutine(right):
            return await right
        else:
            return right  # type: ignore


assert_instance_filter_fn(ExtendedFilter)
assert_instance_filter_fn(AndThenChain)
