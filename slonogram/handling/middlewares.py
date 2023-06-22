from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Generic, TypeVar

from ..protocols.middleware import Middleware

T = TypeVar("T")
D = TypeVar("D")


@dataclass(slots=True)
class MiddlewareSet(Generic[D, T]):
    out_of_order: List[Middleware[D, T]] = field(default_factory=list)
    strict: List[Middleware[D, T]] = field(default_factory=list)


@dataclass(slots=True)
class Middlewares(Generic[D, T]):
    run_before: MiddlewareSet[D, T] = field(default_factory=MiddlewareSet)
    run_after: MiddlewareSet[D, T] = field(default_factory=MiddlewareSet)
