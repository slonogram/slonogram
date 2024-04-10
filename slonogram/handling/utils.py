from typing import TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from .handler import Handler

M = TypeVar("M")

def unwrap(handler: 'Handler[M]') -> 'Handler[M]':
    from .wrap import Wrap

    while isinstance(handler, Wrap):
        handler = handler.inner

    return handler

__all__ = ["unwrap"]

