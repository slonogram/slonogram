import typing as t

from sena.endpoint.extended import Endpoint

from .request import Request
from .response import Response


Session: t.TypeAlias = Endpoint[Response, Request]


__all__ = ["Session"]


