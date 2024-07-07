import typing as t

from sena.predicate import PredicateFn

from ..types.ctx import Ctx

D = t.TypeVar("D")
FilterFn: t.TypeAlias = PredicateFn[Ctx[D]]

__all__ = ["FilterFn"]

