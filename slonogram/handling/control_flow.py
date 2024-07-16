import typing as t

from sena.control_flow import (
    ControlFlow as _ControlFlow,
    Continue as _Continue,
    Break as _Break,
)

from ..types.ctx import Ctx
from ..types.activation import Activation

D = t.TypeVar("D")

ControlFlow: t.TypeAlias = _ControlFlow[Activation, Ctx[D]]
Continue: t.TypeAlias = _Continue[Ctx[D]]
Break: t.TypeAlias = _Break[Activation]


__all__ = [
    "ControlFlow",
    "Continue",
    "Break",
]


