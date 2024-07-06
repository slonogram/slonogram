import typing as t
import dataclasses as dtc

D = t.TypeVar("D")

@dtc.dataclass(slots=True)
class Ctx(t.Generic[D]):
    data: D
    memo: dict[t.Any, t.Any]


__all__ = ["Ctx"]


