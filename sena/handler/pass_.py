import typing as t

from .base import Next
from ..control_flow import ControlFlow


C = t.TypeVar("C")
B = t.TypeVar("B")

def pass_(req: C, next: Next[B, C]) -> t.Awaitable[ControlFlow[B, C]]:
    """ Simply pass the request forwards """
    return next(req)


__all__ = ["pass_"]


