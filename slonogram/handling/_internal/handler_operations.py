import typing as t

from slonogram.types.ctx import Ctx
from slonogram.types.activation import Activation

from sena.handling.extended import (
    Mapper as _Mapper,
    Modifier,
)

D = t.TypeVar("D")


class Mapper(_Mapper[Activation, Ctx[D]], t.Protocol[D]):
    ...


__all__ = ["Mapper", "Modifier"]

