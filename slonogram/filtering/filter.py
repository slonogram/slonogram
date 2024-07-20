import typing as t

from sena.handling.filtered import Predicate

from ..types.ctx import Ctx

D = t.TypeVar("D")
FilterFn: t.TypeAlias = Predicate[Ctx[D]]

__all__ = ["FilterFn"]

