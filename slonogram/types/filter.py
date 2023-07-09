from __future__ import annotations

from abc import ABCMeta, abstractmethod

from typing import Callable, TypeAlias, Awaitable, TypeVar, Generic
from .context import Context

T = TypeVar("T")

FilterFn: TypeAlias = Callable[[Context[T]], Awaitable[bool]]


class AlwaysConst:
    def __init__(self, const: bool) -> None:
        self.const = const

    def __repr__(self) -> str:
        return f"const({self.const})"

    async def __call__(self, _: Context[T]) -> bool:
        return self.const


always_true = AlwaysConst(True)
always_false = AlwaysConst(False)


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
    def __call__(self, ctx: Context[T]) -> Awaitable[bool]:
        _ = ctx
        raise NotImplementedError


class If(ExtendedFilter[T]):
    __slots__ = "condition", "on_then", "on_else"

    def __init__(
        self,
        condition: FilterFn[T],
        on_then: FilterFn[T] = always_true,
        on_else: FilterFn[T] = always_false,
        restore_scratches: bool = True,
    ) -> None:
        self.condition = condition
        self.on_then = on_then
        self.on_else = on_else
        self.restore_scratches = restore_scratches

    def then(self, new_then: FilterFn[T]) -> If[T]:
        return If(self.condition, new_then, self.on_else)

    def else_(self, new_else: FilterFn[T]) -> If[T]:
        return If(self.condition, self.on_then, new_else)

    def __repr__(self) -> str:
        restore_flag = "" if self.restore_scratches else "!r"
        return (
            f"(if{restore_flag} {self.condition} then"
            f" {self.on_then} else {self.on_else})"
        )

    async def __call__(self, ctx: Context[T]) -> bool:
        if self.restore_scratches:
            _copy = ctx.pad.copy()
        cond = await self.condition(ctx)
        if cond:
            return await self.on_then(ctx)
        elif self.restore_scratches:
            ctx.pad = _copy
        return await self.on_else(ctx)


class Predicate(ExtendedFilter[T]):
    __slots__ = ("fn",)

    def __init__(self, fn: FilterFn[T]) -> None:
        self.fn = fn

    def __call__(self, ctx: Context[T]) -> Awaitable[bool]:
        return self.fn(ctx)


class Or(ExtendedFilter[T]):
    __slots__ = "lhs_fn", "rhs_fn", "exclusive"

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

    async def __call__(self, ctx: Context[T]) -> bool:
        if self.exclusive:
            lhs = await self.lhs_fn(ctx)
            rhs = await self.rhs_fn(ctx)
            return bool(lhs ^ rhs)
        else:
            lhs = await self.lhs_fn(ctx)
            if not lhs:
                return await self.rhs_fn(ctx)
            return lhs


class And(ExtendedFilter[T]):
    __slots__ = "lhs_fn", "rhs_fn"

    def __init__(self, lhs: FilterFn[T], rhs: FilterFn[T]) -> None:
        self.lhs_fn = lhs
        self.rhs_fn = rhs

    def __repr__(self) -> str:
        return f"{self.lhs_fn} & {self.rhs_fn}"

    async def __call__(self, ctx: Context[T]) -> bool:
        lhs = await self.lhs_fn(ctx)
        if not lhs:
            return False
        return await self.rhs_fn(ctx)


class Inverted(ExtendedFilter[T]):
    __slots__ = ("fn",)

    def __init__(self, fn: FilterFn[T]) -> None:
        self.fn = fn

    def __repr__(self) -> str:
        return f"~{self.fn}"

    async def __call__(self, ctx: Context[T]) -> bool:
        result = await self.fn(ctx)
        return not result


def not_(fn: FilterFn[T]) -> Inverted[T]:
    return Inverted(fn)


__all__ = [
    "FilterFn",
    "ExtendedFilter",
    "Inverted",
    "And",
    "Or",
    "Predicate",
    "If",
]
