from __future__ import annotations

import typing as t

from .filter import FilterFn
from .and_ import And
from .or_ import Or

from ..utils.altering import alter1, Alterer1
from ..utils.omit import OMIT, Omittable, non_omitted_or
from ..types.ctx import Ctx

D = t.TypeVar("D")

class _Missing: ...
_MISSING = _Missing()

class Filter(FilterFn[D]):
    __slots__ = ('pred', 'pure', '_hash', '_deepest_pred')

    pure: bool

    def __init__(
        self,
        pred: FilterFn[D],
        pure: Omittable[bool] = OMIT,
    ) -> None:
        pure = non_omitted_or(pure, True)
        self.pred = pred

        # Propagate impurity
        if pure:
            pure = pred.pure if isinstance(pred, Filter) else pure

        self.pure = pure

        # Precompute this for faster memoizing
        self._hash = hash(self.pred)
        self._deepest_pred = pred.pred if isinstance(pred, Filter) else pred

    def alter(
        self,
        *,
        pred: Omittable[Alterer1[FilterFn[D]]] = OMIT,
        pure: Omittable[Alterer1[bool]] = OMIT,
    ) -> t.Self:
        return type(self)(
            pred=alter1(pred, self.pred),
            pure=alter1(pure, self.pure),
        )

    def impure(self) -> t.Self:
        return self.alter(pure=lambda _: False)

    def modify(self, f: t.Callable[[Filter[D]], Filter[D]]) -> Filter[D]:
        return f(self)

    def __and__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda old: Filter(And(old, rhs)))

    def __or__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda f: Filter(Or(f, rhs)))

    def __xor__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.alter(pred=lambda f: Filter(Or(f, rhs, exclusive=True)))

    def __hash__(self) -> int:
        return self._hash

    def __eq__(self, rhs: t.Any) -> bool:
        if isinstance(rhs, Filter):
            return self._deepest_pred == rhs._deepest_pred

        return self.pred == rhs or self._deepest_pred == rhs or self is rhs

    def __call__(self, ctx: Ctx[D], /) -> bool:
        if not self.pure:
            return self.pred(ctx)

        # Memoize already seen filters
        memoized = ctx.memo.get(self, _MISSING)
        if memoized is not _MISSING:
            return memoized  # type: ignore

        result = self.pred(ctx)
        ctx.memo[self] = result
        return result


__all__ = ["Filter"]


