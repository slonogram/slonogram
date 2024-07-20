import typing as t

from .handling.base import HandlerFn
from .endpoint.base import EndpointFn

P = t.ParamSpec("P")
L = t.TypeVar("L", contravariant=True)
B = t.TypeVar("B")
C = t.TypeVar("C")


def extract_endpoint(e: EndpointFn[B, C]) -> EndpointFn[B, C]:
    from .endpoint.simple import Simple

    if isinstance(e, Simple):
        return e.inner

    return e

def extract_handler(h: HandlerFn[B, C]) -> HandlerFn[B, C]:
    from .handling.simple import Simple

    if isinstance(h, Simple):
        return h.inner

    return h

__all__ = [
    "extract_handler",
    "extract_endpoint",
]

