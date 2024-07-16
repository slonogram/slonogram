from __future__ import annotations

import typing as t

from .filter import FilterFn
from .and_ import And
from .or_ import Or

from ..types.ctx import Ctx

D = t.TypeVar("D")

class _Missing: ...
_MISSING = _Missing()

class Filter(FilterFn[D]):
    __slots__ = ('pred', )

    def __init__(self, pred: FilterFn[D]) -> None:
        self.pred = pred

    def apply(self, f: t.Callable[[Filter[D]], Filter[D]]) -> Filter[D]:
        return f(self)

    def __and__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.apply(lambda f: Filter(And(f, rhs)))

    def __or__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.apply(lambda f: Filter(Or(f, rhs)))

    def __xor__(self, rhs: FilterFn[D]) -> Filter[D]:
        return self.apply(lambda f: Filter(Or(f, rhs, exclusive=True)))

    def __hash__(self) -> int:
        # I suppose this is good trade-off, potentionally big filters
        # will be hashed fast
        return id(self)

    def __eq__(self, rhs: t.Any) -> bool:
        return isinstance(rhs, Filter) and self.pred == rhs.pred

    def __call__(self, ctx: Ctx[D], /) -> bool:
        # Memoize already seen filters
        memoized = ctx.memo.get(self, _MISSING)
        if memoized is not _MISSING:
            return memoized

        result = self.pred(ctx)
        ctx.memo[self] = result
        return result


__all__ = ["Filter"]


