import typing as t

from ..types.ctx import Ctx
from ..types.activation import Activation

from sena.handler import HandlerFn as _HandlerFn, Endpoint as _Endpoint
from sena.extended import Handler as _Handler
from sena.control_flow import (
    ControlFlow as _ControlFlow,
    Continue as _Continue,
    Break as _Break
)

D = t.TypeVar("D")

class HandlerFn(t.Protocol[D], _HandlerFn[Activation, Ctx[D]]):
    ...

class Endpoint(t.Protocol[D], _Endpoint[Activation, Ctx[D]]):
    ...

ControlFlow: t.TypeAlias = _ControlFlow[Activation, Ctx[D]]
Continue: t.TypeAlias = _Continue[Ctx[D]]
Break: t.TypeAlias = _Break[Ctx[D]]
Handler: t.TypeAlias = _Handler[Activation, Ctx[D]]


__all__ = [
    "HandlerFn",
    "Handler",
    "Endpoint",

    "ControlFlow",
    "Continue",
    "Break",
]

