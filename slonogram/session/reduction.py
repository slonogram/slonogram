import typing as t

from sena.endpoint.reducible import (
    Reducible as _Reducible,
    Reducer as _Reducer,
)

from .request import Request
from .response import Response

Acc = t.TypeVar("Acc")

@t.runtime_checkable
class Reducible(_Reducible[Response, Request], t.Protocol):
    ...


class Reducer(_Reducer[Response, Request, Acc], t.Protocol):
    ...


__all__ = ["Reducible", "Reducer"]

