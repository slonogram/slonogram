# Re-exporting stuff with slonogram specificity
import typing as t

from sena.handler import (
    Simple,
    Handler as _Handler,
    HandlerFn as _HandlerFn,
    HandlerFnFactory as _HandlerFnFactory,
)
from sena.handler.extended import (
    Mapper as _Mapper,
    Modifier,
    Next as _Next,
)

from ..types.ctx import Ctx
from ..types.activation import Activation

D = t.TypeVar("D")

Handler: t.TypeAlias = Simple[Activation, Ctx[D]]
AbstractHandler: t.TypeAlias = _Handler[Activation, Ctx[D]]

# To improve traces

class Mapper(t.Protocol[D], _Mapper[Activation, Ctx[D]]):
    ...

class Next(t.Protocol[D], _Next[Activation, Ctx[D]]):
    ...

class HandlerFnFactory(
    t.Protocol[D],
    _HandlerFnFactory[Activation, Ctx[D], Activation, Ctx[D]],
):
    ...

class HandlerFn(t.Protocol[D], _HandlerFn[Activation, Ctx[D]]):
    ...

__all__ = [
    "Handler",
    "AbstractHandler",
    "HandlerFnFactory",
    "HandlerFn",
    "Next",
    "Mapper",
    "Modifier",
]


