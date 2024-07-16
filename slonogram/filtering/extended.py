from __future__ import annotations

import typing as t

from .filter import FilterFn
from .and_ import And
from .or_ import Or

from ..utils.altering import alter1, Alterer1
from ..utils.omit import OMIT, Omittable
from ..types.ctx import Ctx

D = t.TypeVar("D")

class _Missing: ...
_MISSING = _Missing()

class Filter(FilterFn[D]):
    __slots__ = ('pred', 'impure')

    pred: FilterFn[D]
    impure: bool

    def __init__(
        self,
        pred: FilterFn[D],
        impure: Omittable[bool] = OMIT,
    ) -> None:
        self.pred = pred

        if impure is OMIT:
            self.impure = False
        else:
            self.impure = impure  # type: ignore

    def alter(
        self,
        *,
        pred: Omittable[Alterer1[FilterFn[D]]] = OMIT,
        impure: Omittable[Alterer1[bool]] = OMIT,
    ) -> Filter[D]:
        return Filter(
            pred=alter1(pred, self.pred),
            impure=alter1(impure, self.impure),
        )

    def modify(self, f: t.Callable[[Filter[D]], Filter[D]]) -> Filter[D]:
        return f(self)

    def __and__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda old: Filter(And(old, rhs)))

    def __or__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda f: Filter(Or(f, rhs)))

    def __xor__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda f: Filter(Or(f, rhs, exclusive=True)))

    def __hash__(self) -> int:
        # I suppose this is good trade-off, potentionally big filters
        # will be hashed fast
        return id(self)

    def __eq__(self, rhs: t.Any) -> bool:
        # See `__hash__` impl
        return self is rhs

    def __call__(self, ctx: Ctx[D], /) -> bool:
        if self.impure:
            return self.pred(ctx)

        # Memoize already seen filters
        memoized = ctx.memo.get(self, _MISSING)
        if memoized is not _MISSING:
            return memoized  # type: ignore

        result = self.pred(ctx)
        ctx.memo[self] = result
        return result


__all__ = ["Filter"]


