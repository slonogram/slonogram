from __future__ import annotations

import typing as t

from sena import Ext

from .._internal.filter import (
    Filter,
    SeqFilter,
)

from .binary import Binary
from .unary import Unary

D = t.TypeVar("D")
R = t.TypeVar("R")
F = t.TypeVar("F")

class ExtFilter(Ext[F]):
    """Filter-specific extensions.
    """

    def __not__(
        self: ExtFilter[Filter[D]],
    ) -> ExtFilter[Filter[D]]:
        return self.untyped_modify(Unary.not_)

    def __and__(
        self: ExtFilter[Filter[D]],
        rhs: Filter[D],
    ) -> ExtFilter[Filter[D]]:
        return self.untyped_modify(lambda lhs: Binary.and_(lhs, rhs))

    def __or__(
        self: ExtFilter[Filter[D]],
        rhs: Filter[D],
    ) -> ExtFilter[Filter[D]]:
        return self.untyped_modify(lambda lhs: Binary.or_(lhs, rhs))

    def __xor__(
        self: ExtFilter[Filter[D]],
        rhs: Filter[D],
    ) -> ExtFilter[Filter[D]]:
        return self.untyped_modify(lambda lhs: Binary.xor(lhs, rhs))


__all__ = [
    "Filter",
    "SeqFilter",
    "ExtFilter",
]

