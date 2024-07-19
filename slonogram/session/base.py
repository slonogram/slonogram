import typing as t
from sena.endpoint.base import EndpointFn

from .request import Request
from .response import Response


class SessionFn(EndpointFn[Response, Request], t.Protocol):
    ...


__all__ = ["SessionFn"]


