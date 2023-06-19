from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Awaitable
from .types import FilterFn

from ..dp.context import Context

T = TypeVar("T")
D = TypeVar("D")


class ExtendedFilter(Generic[T], metaclass=ABCMeta):
    def __invert__(self) -> Inverted[T]:
        return Inverted(self)

    def __or__(self, rhs: FilterFn[T]) -> Or[T]:
        return Or(self, rhs, False)

    def __xor__(self, rhs: FilterFn[T]) -> Or[T]:
        return Or(self, rhs, True)

    def __and__(self, rhs: FilterFn[T]) -> And[T]:
        return And(self, rhs)

    @abstractmethod
    def __call__(self, ctx: Context[D, T]) -> Awaitable[bool]:
        _ = ctx
        raise NotImplementedError


class Or(ExtendedFilter[T]):
    def __init__(
        self, lhs: FilterFn[T], rhs: FilterFn[T], exclusive: bool
    ) -> None:
        self.lhs_fn = lhs
        self.rhs_fn = rhs
        self.exclusive = exclusive

    @property
    def symbol(self) -> str:
        return "^" if self.exclusive else "|"

    def __repr__(self) -> str:
        return f"{self.lhs_fn} {self.symbol} {self.rhs_fn}"

    async def __call__(self, ctx: Context[D, T]) -> bool:
        if self.exclusive:
            lhs = await self.lhs_fn(ctx)
            rhs = await self.rhs_fn(ctx)
            return bool(lhs ^ rhs)
        else:
            lhs = await self.lhs_fn(ctx)
            if lhs is None:
                return await self.rhs_fn(ctx)
            return lhs


class And(ExtendedFilter[T]):
    def __init__(self, lhs: FilterFn[T], rhs: FilterFn[T]) -> None:
        self.lhs_fn = lhs
        self.rhs_fn = rhs

    def __repr__(self) -> str:
        return f"{self.lhs_fn} & {self.rhs_fn}"

    async def __call__(self, ctx: Context[D, T]) -> bool:
        lhs = await self.lhs_fn(ctx)
        if lhs is None:
            return None
        return await self.rhs_fn(ctx)


class Inverted(ExtendedFilter[T]):
    def __init__(self, fn: FilterFn[T]) -> None:
        self.fn = fn

    def __repr__(self) -> str:
        return f"~{self.fn}"

    async def __call__(self, ctx: Context[D, T]) -> bool:
        result = await self.fn(ctx)
        return result is not None


async def always_true(_: Context[D, T]) -> bool:
    return True


def not_(fn: FilterFn[T]) -> Inverted[T]:
    return Inverted(fn)


__all__ = ["not_", "always_true", "And", "Or", "ExtendedFilter"]
