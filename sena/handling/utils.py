import functools
import typing as t

from .base import HandlerFn
if t.TYPE_CHECKING:
    from .extended import Handler

P = t.ParamSpec("P")
B = t.TypeVar("B")
C = t.TypeVar("C")


def lift(f: t.Callable[P, HandlerFn[B, C]]) -> t.Callable[P, 'Handler[B, C]']:
    from .simple import Simple

    @functools.wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> 'Handler[B, C]':
        return Simple(f(*args, **kwargs))

    return inner


__all__ = ["lift"]

