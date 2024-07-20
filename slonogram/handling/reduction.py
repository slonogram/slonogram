import typing as t

from sena.handler.reducible import (
    Reducible as _Reducible,
    Reducer as _Reducer,
)

from ..types.activation import Activation
from ..types.ctx import Ctx


T = t.TypeVar("T")
D = t.TypeVar("D")


class Reducer(_Reducer[Activation, Ctx[D], T], t.Protocol[D, T]):
    ...

@t.runtime_checkable
class Reducible(_Reducible[Activation, Ctx[D]], t.Protocol[D]):
    ...


__all__ = [
    "Reducer",
    "Reducible",
]



