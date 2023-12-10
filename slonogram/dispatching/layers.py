from dataclasses import dataclass
from typing import Generic, TypeVar

from ..filtering.base import BareFilter
from ..middleware import BareMiddleware

M = TypeVar("M")


@dataclass(frozen=True, slots=True)
class Layers(Generic[M]):
    prepare: BareMiddleware[M, []] | None = None

    before: BareMiddleware[M, []] | None = None
    after: BareMiddleware[M, [Exception | None]] | None = None

    filter: BareFilter[M] | None = None


__all__ = ["Layers"]
