from __future__ import annotations

from typing import TypeVar, Generic, TypeAlias, Callable, Awaitable
from dataclasses import dataclass

from .layers import Layers
from .context import Context
from .stash import Stash


M = TypeVar("M")
RawHandler: TypeAlias = Callable[[Context[M]], Awaitable[None]]


@dataclass(slots=True)
class Activation(Generic[M]):
    handler: Handler[M] | None = None

    @classmethod
    def ignored(cls) -> Activation[M]:
        return Activation(None)

    @classmethod
    def activated(cls, handler: Handler[M]) -> Activation[M]:
        return Activation(handler)

    @property
    def is_activated(self) -> bool:
        return self.handler is not None


class Handler(Generic[M]):
    __slots__ = ("raw", "layers", "observer")

    def __init__(
        self,
        raw: RawHandler[M],
        layers: Layers[[], M],
        observer: bool = False,
    ) -> None:
        self.raw = raw
        self.layers = layers
        self.observer = observer

    async def __call__(self, context: Context[M]) -> Activation[M]:
        layers = self.layers
        subctx = context.with_stash(Stash(context.stash))

        if layers.prepare is not None:
            await layers.prepare(subctx)
        if layers.filter is not None and not layers.filter(subctx):
            return Activation.ignored()

        if layers.before is not None:
            await layers.before(context)

        if layers.after is not None:
            try:
                await self.raw(subctx)
            except Exception as exc:
                await layers.after(subctx, exc)
            else:
                await layers.after(subctx, None)
        else:
            await self.raw(subctx)

        if self.observer:
            return Activation.ignored()
        return Activation.activated(self)


__all__ = ["RawHandler", "Handler", "Activation"]
