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

class Mapper(_Mapper[Activation, Ctx[D]], t.Protocol[D]):
    ...

class Next(_Next[Activation, Ctx[D]], t.Protocol[D]):
    ...

class HandlerFnFactory(
    _HandlerFnFactory[Activation, Ctx[D], Activation, Ctx[D]],
    t.Protocol[D],
):
    ...

class HandlerFn(_HandlerFn[Activation, Ctx[D]], t.Protocol[D]):
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


