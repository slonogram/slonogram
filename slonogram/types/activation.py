import typing as t
import dataclasses as dtc


@dtc.dataclass(slots=True)
class Activation:
    id: t.Any


__all__ = ["Activation"]

