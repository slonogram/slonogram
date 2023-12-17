from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Callable, TypeAlias, TypeVar, Generic, Protocol
from abc import ABCMeta, abstractmethod

if TYPE_CHECKING:
    from ..dispatching.stash import Stash
    from ..dispatching.context import Context
from ..utils import origin_of

M = TypeVar("M")


class BareFilter(Protocol[M]):
    def __call__(self, context: Context[M], /) -> bool:
        ...


class ExtendedFilter(Generic[M], metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, ctx: Context[M]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError

    def __not__(self) -> Not[M]:
        return Not(self)

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

    def __repr__(self) -> str:
        operator = "^" if self.exclusive else "|"
        return f"{self.lhs!r} {operator} {self.rhs!r}"

    def __call__(self, ctx: Context[M]) -> bool:
        if self.exclusive:
            return bool(self.lhs(ctx) ^ self.rhs(ctx))
        return self.lhs(ctx) or self.rhs(ctx)


class And(ExtendedFilter[M]):
    __slots__ = ("lhs", "rhs")

    def __init__(self, lhs: BareFilter[M], rhs: BareFilter[M]) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self) -> str:
        return f"{self.lhs!r} & {self.rhs!r}"

    def __call__(self, ctx: Context[M]) -> bool:
        return self.lhs(ctx) and self.rhs(ctx)


class Predicate(ExtendedFilter[M]):
    __slots__ = ("pred",)

    def __init__(self, pred: BareFilter[M]) -> None:
        self.pred = pred

    def __repr__(self) -> str:
        return repr(self.pred)

    def __call__(self, ctx: Context[M]) -> bool:
        return self.pred(ctx)


class Not(ExtendedFilter[M]):
    __slots__ = ("filter",)

    def __init__(self, pred: BareFilter[M]) -> None:
        self.filter = pred

    def __repr__(self) -> str:
        if origin_of(self.filter) is not Predicate:
            return f"~({self.filter!r})"
        return f"~{self.filter!r}"

    def __call__(self, ctx: Context[M]) -> bool:
        return not self.filter(ctx)


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

    def __repr__(self) -> str:
        return f"{{{self.filter!r}}}"

    def __call__(self, ctx: Context[M]) -> bool:
        subctx = ctx.with_stash(
            Stash(self.stash.types, parent=ctx.stash)
            if self.extend_parent
            else self.stash
        )
        return self.filter(subctx)


__all__ = [
    "ExtendedFilter",
    "BareFilter",
    "And",
    "Or",
    "Predicate",
]
