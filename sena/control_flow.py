import typing as t
import dataclasses as dtc

C = t.TypeVar("C")
B = t.TypeVar("B")

@dtc.dataclass(slots=True)
class Break(t.Generic[B]):
    value: B

@dtc.dataclass(slots=True)
class Continue(t.Generic[C]):
    value: C


ControlFlow: t.TypeAlias = Break[B] | Continue[C]


__all__ = ["Break", "Continue"]

