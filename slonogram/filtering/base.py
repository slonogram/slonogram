from __future__ import annotations

from typing import Callable, TypeAlias, TypeVar, Generic
from abc import ABCMeta, abstractmethod

from ..dispatching.context import Context
from ..dispatching.stash import Stash

M = TypeVar("M", contravariant=True)
BareFilter: TypeAlias = Callable[[Context[M]], bool]


class ExtendedFilter(Generic[M], metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, ctx: Context[M]) -> bool:
        raise NotImplementedError

    def __and__(self, rhs: BareFilter[M]) -> And[M]:
        return And[M](self, rhs)

    def __xor__(self, rhs: BareFilter[M]) -> Or[M]:
        return Or(self, rhs, exclusive=True)

    def __or__(self, rhs: BareFilter[M]) -> Or[M]:
        return Or(self, rhs)


class Or(ExtendedFilter[M]):
    __slots__ = ("lhs", "rhs", "exclusive")

    def __init__(
        self,
        lhs: BareFilter[M],
        rhs: BareFilter[M],
        *,
        exclusive: bool = False,
    ) -> None:
        self.exclusive = exclusive
        self.lhs = lhs
        self.rhs = rhs

    def __call__(self, ctx: Context[M]) -> bool:
        if self.exclusive:
            return bool(self.lhs(ctx) ^ self.rhs(ctx))
        return self.lhs(ctx) or self.rhs(ctx)


class And(ExtendedFilter[M]):
    __slots__ = ("lhs", "rhs")

    def __init__(self, lhs: BareFilter[M], rhs: BareFilter[M]) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __call__(self, ctx: Context[M]) -> bool:
        return self.lhs(ctx) and self.rhs(ctx)


class Predicate(ExtendedFilter[M]):
    __slots__ = ("pred",)

    def __init__(self, pred: BareFilter[M]) -> None:
        self.pred = pred

    def __call__(self, ctx: Context[M]) -> bool:
        return self.pred(ctx)


class Scope(ExtendedFilter[M]):
    __slots__ = ("stash", "filter", "extend_parent")

    def __init__(
        self,
        filter: BareFilter[M],
        *,
        stash: Stash | None = None,
        extend_parent: bool = True,
    ) -> None:
        self.filter = filter
        self.extend_parent = extend_parent

        if stash is None:
            self.stash = Stash()
        else:
            self.stash = stash

    def __call__(self, ctx: Context[M]) -> bool:
        subctx = Context(
            Stash(ctx.stash, self.stash.types) if self.extend_parent else self.stash,
            ctx.model,
            ctx.bot,
        )
        return self.filter(subctx)


__all__ = [
    "ExtendedFilter",
    "BareFilter",
    "And",
    "Or",
    "Predicate",
]
