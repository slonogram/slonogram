from typing import TypeVar, TypeGuard

from .handler import Handler
from .extended import ExtendedHandler

M = TypeVar("M")

def is_extended_handler(handler: Handler[M]) -> TypeGuard[ExtendedHandler[M]]:
    return getattr(handler, '__extended_handler__', False)

def unwrap_handler(handler: Handler[M]) -> Handler[M]:
    from .wrap import Wrap

    while isinstance(handler, Wrap):
        handler = handler.inner

    return handler

__all__ = ["unwrap_handler", "is_extended_handler"]

