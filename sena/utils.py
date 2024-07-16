import typing as t

from .handler.base import HandlerFn
from .endpoint.base import EndpointFn

P = t.ParamSpec("P")
Ts = t.TypeVarTuple("Ts")
L = t.TypeVar("L", contravariant=True)
B = t.TypeVar("B")
C = t.TypeVar("C")


def extract_endpoint(e: EndpointFn[B, C]) -> EndpointFn[B, C]:
    from .endpoint.extended import Endpoint

    if isinstance(e, Endpoint):
        return e.fn
    return e

def extract_handler(h: HandlerFn[B, C]) -> HandlerFn[B, C]:
    from .handler.simple import Simple

    if isinstance(h, Simple):
        return h.inner

    return h

__all__ = [
    "extract_handler",
    "extract_endpoint",
]

