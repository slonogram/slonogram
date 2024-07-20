import typing as t

from .base import EndpointFn
from ..reduction import (
    Reducer as _Reducer,
    Reducible as _Reducible,
)

In = t.TypeVar("In", covariant=True)

Acc = t.TypeVar("Acc")
Ret = t.TypeVar("Ret", contravariant=True)

In_contra = t.TypeVar("In_contra", contravariant=True)
Ret_co = t.TypeVar("Ret_co", covariant=True)

@t.runtime_checkable
class Reducible(_Reducible[EndpointFn[Ret_co, In_contra]], t.Protocol[Ret_co, In_contra]):
    ...

class Reducer(_Reducer[Acc, EndpointFn[Ret, In]], t.Protocol[Ret, In, Acc]):
    ...


__all__ = ["Reducible", "Reducer"]



