import typing as t

from sena.handler.reducing import (
    Reducing as _Reducing,
    Reducer as _Reducer,
    try_reduce
)

from ..types.activation import Activation
from ..types.ctx import Ctx


T = t.TypeVar("T")
D = t.TypeVar("D")


class Reducer(_Reducer[Activation, Ctx[D], T], t.Protocol[D, T]):
    ...

@t.runtime_checkable
class Reducing(_Reducing[Activation, Ctx[D]], t.Protocol[D]):
    ...


__all__ = [
    "Reducer",
    "Reducing",
    "try_reduce",
]



