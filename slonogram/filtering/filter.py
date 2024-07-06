import typing as t
from functools import wraps

from sena.predicate import PredicateFn

from ..types.ctx import Ctx

D = t.TypeVar("D")
FilterFn: t.TypeAlias = PredicateFn[Ctx[D]]

def lift(f: PredicateFn[D]) -> FilterFn[D]:
    return wraps(f)(lambda ctx: f(ctx.data))

__all__ = ["FilterFn", "lift"]

