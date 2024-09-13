import typing as t
import dataclasses as dtc
import enum

from ..utils.omit import Omittable, OMIT


@dtc.dataclass(slots=True)
class Activated:
    handler: t.Any

class Stalled(enum.IntEnum):
    STALLED = 0


STALLED = Stalled.STALLED
Activation: t.TypeAlias = Activated | Stalled

