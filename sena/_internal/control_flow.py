import dataclasses as dtc
import typing as t


A = t.TypeVar("A")
C = t.TypeVar("C")
B = t.TypeVar("B")


@dtc.dataclass(slots=True)
class Continue(t.Generic[C]):
    value: C


@dtc.dataclass(slots=True)
class Break(t.Generic[B]):
    value: B


ControlFlow: t.TypeAlias = Continue[C] | Break[B]


def map_cont(src: ControlFlow[C, B], f: t.Callable[[C], A]) -> ControlFlow[A, B]:
    match src:
        case Continue(value):
            return Continue(f(value))

        case Break(value):
            return Break(value)
