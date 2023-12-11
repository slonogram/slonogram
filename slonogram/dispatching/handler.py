from typing import TypeVar, Generic, TypeAlias, Callable, Awaitable
from enum import IntEnum, auto

from .layers import Layers
from .context import Context
from .stash import Stash


M = TypeVar("M")
RawHandler: TypeAlias = Callable[[Context[M]], Awaitable[None]]


class HandlerActivation(IntEnum):
    activated = auto()
    ignored = auto()


class Handler(Generic[M]):
    __slots__ = ("raw_handler", "layers", "observer")

    def __init__(
        self,
        raw_handler: RawHandler[M],
        layers: Layers[[], M],
        observer: bool = False,
    ) -> None:
        self.raw_handler = raw_handler
        self.layers = layers
        self.observer = observer

    async def __call__(self, context: Context[M]) -> HandlerActivation:
        layers = self.layers
        subctx = context.with_stash(Stash(context.stash))

        if layers.prepare is not None:
            await layers.prepare(subctx)
        if layers.filter is not None and not layers.filter(subctx):
            return HandlerActivation.ignored

        if layers.before is not None:
            await layers.before(context)

        if layers.after is not None:
            try:
                await self.raw_handler(subctx)
            except Exception as exc:
                await layers.after(subctx, exc)
            else:
                await layers.after(subctx, None)
        else:
            await self.raw_handler(subctx)

        if self.observer:
            return HandlerActivation.ignored
        return HandlerActivation.activated


__all__ = ["RawHandler", "Handler", "HandlerActivation"]
