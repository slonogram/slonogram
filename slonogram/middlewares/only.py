from typing import (
    TypeVar,
    TYPE_CHECKING,
    Iterable,
    Awaitable,
    Generic,
)

from .base import Middlewared
from .utils import unwrap

from .._internal.utils import stalled
from ..abstract.interested import Interested
from ..types.interest import Interest


if TYPE_CHECKING:
    from ..dispatching.context import Context
    from ..dispatching.dispatcher import Dispatcher

    from ..handling.handler import Handler
    from ..handling.activation import Activation

from ..schemas.update import Update

M = TypeVar("M")


class Only(Generic[M], Middlewared[Update], Interested):
    __slots__ = ("interests", "handler")
    interests: set[Interest]

    def __init__(
        self,
        interests: Interest | Iterable[Interest],
        handler: "Handler[M]",
    ) -> None:
        if isinstance(interests, Interest):
            self.interests = {interests}
        else:
            self.interests = set(interests)
        self.handler = unwrap(handler)

    def try_merge(self, dp: "Dispatcher[M]") -> "Only":
        from ..dispatching.dispatcher import Dispatcher

        if isinstance(self.handler, Dispatcher):
            return Only(self.interests, self.handler.register(dp))
        return self

    def collect_interests(self) -> set[Interest]:
        return self.interests

    def __repr__(self) -> str:
        return f"Only(interested={self.interests}, handler={self.handler})"

    def __call__(self, ctx: "Context[Update]") -> "Awaitable[Activation]":
        upd = ctx.model
        for interest in self.interests:
            model = getattr(upd, interest)
            if model is not None:
                return self.handler(
                    ctx.with_model(model)
                )
        return stalled()

__all__ = [
    "Only",
]
