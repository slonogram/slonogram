from __future__ import annotations
from typing import TypeVar, TypeAlias, ParamSpec, Concatenate

from .stash import Stash

from ..bot import Bot
from ..middlewares import Middleware
from ..utils.typing import MaybeException
from .._internal.context_shortcuts import ShortcutsMixin

M = TypeVar("M")
Tail = ParamSpec("Tail")


class Context(ShortcutsMixin[M]):
    __slots__ = ("stash", "model", "rpc")

    def __init__(
        self,
        stash: Stash,
        model: M,
        rpc: Bot,
    ) -> None:
        self.stash = stash
        self.model = model
        self.rpc = rpc

    def with_stash(self, stash: Stash) -> Context[M]:
        return Context(stash, self.model, self.rpc)


CtxMiddleware: TypeAlias = Middleware[Concatenate[Context[M], Tail], None]
CtxExcMiddleware: TypeAlias = CtxMiddleware[M, [MaybeException]]

__all__ = [
    "Context",
    "CtxMiddleware",
    "CtxExcMiddleware",
]
