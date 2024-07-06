import typing as t

from .filter import FilterFn
from ..types.ctx import Ctx

D = t.TypeVar("D")

class And(FilterFn[D]):
    def __init__(self, lhs: FilterFn[D], rhs: FilterFn[D]) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __call__(self, req: Ctx[D], /) -> bool:
        return self.lhs(req) and self.rhs(req)

    def __repr__(self) -> str:
        return f"And({self.lhs!r}, {self.rhs!r})"

__all__ = ["And"]

