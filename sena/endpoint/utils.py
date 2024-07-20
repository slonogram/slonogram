import functools
import typing as t

from .base import EndpointFn
if t.TYPE_CHECKING:
    from .extended import Endpoint

P = t.ParamSpec("P")
B = t.TypeVar("B")
C = t.TypeVar("C")

def extend(fn: t.Callable[P, EndpointFn[B, C]]) -> t.Callable[P, 'Endpoint[B, C]']:
    from .simple import Simple

    @functools.wraps(fn)
    def inner(*args: P.args, **kwargs: P.kwargs) -> 'Endpoint[B, C]':
        return Simple(fn(*args, **kwargs))

    return inner


__all__ = ["extend"]

