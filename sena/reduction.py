from __future__ import annotations

import typing as t

Acc = t.TypeVar("Acc")
Src = t.TypeVar("Src", contravariant=True)

Src_co = t.TypeVar("Src_co", covariant=True)

class Reducible(t.Protocol[Src_co]):
    def reduce(self, f: Reducer[Acc, Src_co], initial: Acc, /) -> Acc:
        ...


class Reducer(t.Protocol[Acc, Src]):
    def __call__(self, accum: Acc, data: Src, /) -> Acc:
        ...

__all__ = [
    "Reducible",
    "Reducer",
]


