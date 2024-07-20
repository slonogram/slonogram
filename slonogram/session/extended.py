import typing as t

from sena.endpoint.extended import (
    Endpoint,
    Mapper as _Mapper,
    Modifier,
)

from .request import Request
from .response import Response

class Mapper(_Mapper[Response, Request], t.Protocol):
    ...

Session: t.TypeAlias = Endpoint[Response, Request]

__all__ = ["Session", "Mapper", "Modifier"]


