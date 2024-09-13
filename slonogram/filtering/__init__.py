import typing as t

from sena import Ext

from .._internal.filter import (
    Filter,
    SeqFilter,
)

F = t.TypeVar("F")

class ExtFilter(Ext[F]):
    """Filter-specific extensions.
    """


__all__ = [
    "Filter",
    "SeqFilter",
    "ExtFilter",
]

