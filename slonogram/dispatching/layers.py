from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar, ParamSpec, Concatenate

from ..filtering.base import BareFilter
from ..middleware import BareMiddleware

M = TypeVar("M")
T = TypeVar("T")
P = ParamSpec("P")


def _prefer(v: T | None, otherwise: T | None) -> T | None:
    if v is None:
        return otherwise
    return v


@dataclass(frozen=True, slots=True)
class Layers(Generic[P, M]):
    prepare: BareMiddleware[M, P] | None = None

    before: BareMiddleware[M, P] | None = None
    after: BareMiddleware[M, Concatenate[Exception | None, P]] | None = None

    filter: BareFilter[M] | None = None

    def copy_with(
        self,
        prepare: BareMiddleware[M, P] | None = None,
        before: BareMiddleware[M, P] | None = None,
        after: BareMiddleware[M, Concatenate[Exception | None, P]] | None = None,
        filter: BareFilter[M] | None = None,
    ) -> Layers[P, M]:
        return Layers(
            prepare=_prefer(prepare, self.prepare),
            before=_prefer(before, self.before),
            after=_prefer(after, self.after),
            filter=_prefer(filter, self.filter),
        )


__all__ = ["Layers"]
