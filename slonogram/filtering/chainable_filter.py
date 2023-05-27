from __future__ import annotations
from typing import Generic, TypeVar, Optional, Awaitable, cast
from abc import ABCMeta, abstractmethod
from inspect import iscoroutine
from . import assert_instance_filter_fn, FilterFn

T = TypeVar("T")


class ChainableFilter(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, value: T) -> Optional[T] | Awaitable[Optional[T]]:
        _ = value
        raise NotImplementedError

    def and_then(self, right: FilterFn[T]) -> AndThenChain[T]:
        return AndThenChain(cast(FilterFn[T], self), right)


class AndThenChain(ChainableFilter[T]):
    def __init__(self, left: FilterFn[T], right: FilterFn[T]) -> None:
        self._left = left
        self._right = right

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


assert_instance_filter_fn(ChainableFilter)
assert_instance_filter_fn(AndThenChain)
