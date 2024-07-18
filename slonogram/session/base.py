import typing as t
from sena.endpoint.base import EndpointFn

from .request import Request
from .response import Response


class SessionFn(t.Protocol, EndpointFn[Response, Request]):
    ...


__all__ = ["SessionFn"]


