import typing as t
import dataclasses as dtc


@dtc.dataclass(slots=True)
class Activation:
    handler: t.Any


__all__ = ["Activation"]
