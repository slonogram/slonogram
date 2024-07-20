import typing as t

from slonogram.types.ctx import Ctx
from slonogram.types.activation import Activation

from sena.handling.reducible import (
    Reducible as SenaReducible,
    Reducer as SenaReducer,
)

T = t.TypeVar("T")
D = t.TypeVar("D")


@t.runtime_checkable
class Reducible(SenaReducible[Activation, Ctx[D]], t.Protocol[D]):
    ...


class Reducer(SenaReducer[Activation, Ctx[D], T], t.Protocol[D, T]):
    ...


__all__ = ["Reducible", "Reducer"]


