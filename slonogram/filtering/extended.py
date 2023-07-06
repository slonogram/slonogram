from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Awaitable

from .types import FilterFn
from ..dispatching.context import Context

T = TypeVar("T")
D = TypeVar("D")


class AlwaysConst:
    def __init__(self, const: bool) -> None:
        self.const = const

    def __repr__(self) -> str:
        return f"const({self.const})"

    async def __call__(self, _: Context[D, T]) -> bool:
        return self.const


always_true = AlwaysConst(True)
always_false = AlwaysConst(False)


class ExtendedFilter(Generic[D, T], metaclass=ABCMeta):
    def __invert__(self) -> Inverted[D, T]:
        return Inverted(self)

    def __or__(self, rhs: FilterFn[D, T]) -> Or[D, T]:
        return Or(self, rhs, False)

    def __xor__(self, rhs: FilterFn[D, T]) -> Or[D, T]:
        return Or(self, rhs, True)

    def __and__(self, rhs: FilterFn[D, T]) -> And[D, T]:
        return And(self, rhs)

    @abstractmethod
    def __call__(self, ctx: Context[D, T]) -> Awaitable[bool]:
        _ = ctx
        raise NotImplementedError


class If(ExtendedFilter[D, T]):
    __slots__ = "condition", "on_then", "on_else"

    def __init__(
        self,
        condition: FilterFn[D, T],
        on_then: FilterFn[D, T] = always_true,
        on_else: FilterFn[D, T] = always_false,
        restore_scratches: bool = True,
    ) -> None:
        self.condition = condition
        self.on_then = on_then
        self.on_else = on_else
        self.restore_scratches = restore_scratches

    def then(self, new_then: FilterFn[D, T]) -> If[D, T]:
        return If(self.condition, new_then, self.on_else)

    def else_(self, new_else: FilterFn[D, T]) -> If[D, T]:
        return If(self.condition, self.on_then, new_else)

    def __repr__(self) -> str:
        restore_flag = "" if self.restore_scratches else "!r"
        return (
            f"(if{restore_flag} {self.condition} then"
            f" {self.on_then} else {self.on_else})"
        )

    async def __call__(self, ctx: Context[D, T]) -> bool:
        if self.restore_scratches:
            _copy = ctx.pad.copy()
        cond = await self.condition(ctx)
        if cond:
            return await self.on_then(ctx)
        elif self.restore_scratches:
            ctx.pad = _copy
        return await self.on_else(ctx)


class Just(ExtendedFilter[D, T]):
    __slots__ = ("fn",)

    def __init__(self, fn: FilterFn[D, T]) -> None:
        self.fn = fn

    def __call__(self, ctx: Context[D, T]) -> Awaitable[bool]:
        return self.fn(ctx)


class Or(ExtendedFilter[D, T]):
    __slots__ = "lhs_fn", "rhs_fn", "exclusive"

    def __init__(
        self, lhs: FilterFn[D, T], rhs: FilterFn[D, T], exclusive: bool
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
            if not lhs:
                return await self.rhs_fn(ctx)
            return lhs


class And(ExtendedFilter[D, T]):
    __slots__ = "lhs_fn", "rhs_fn"

    def __init__(self, lhs: FilterFn[D, T], rhs: FilterFn[D, T]) -> None:
        self.lhs_fn = lhs
        self.rhs_fn = rhs

    def __repr__(self) -> str:
        return f"{self.lhs_fn} & {self.rhs_fn}"

    async def __call__(self, ctx: Context[D, T]) -> bool:
        lhs = await self.lhs_fn(ctx)
        if not lhs:
            return False
        return await self.rhs_fn(ctx)


class Inverted(ExtendedFilter[D, T]):
    __slots__ = ("fn",)

    def __init__(self, fn: FilterFn[D, T]) -> None:
        self.fn = fn

    def __repr__(self) -> str:
        return f"~{self.fn}"

    async def __call__(self, ctx: Context[D, T]) -> bool:
        result = await self.fn(ctx)
        return not result


def not_(fn: FilterFn[D, T]) -> Inverted[D, T]:
    return Inverted(fn)


__all__ = ["not_", "always_true", "And", "Or", "ExtendedFilter"]
