from typing import TypeVar
from ..handling.handler import Handler

M = TypeVar("M")


def unwrap(handler: Handler[M]) -> Handler[M]:
    from .wrap import Wrap

    while isinstance(handler, Wrap):
        handler = handler.function
    return handler


__all__ = ["unwrap"]

