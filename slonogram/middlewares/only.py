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

    from ..handling.handler import Handler
    from ..handling.activation import Activation

from ..schemas.update import Update

M = TypeVar("M")


class Only(Generic[M], Middlewared[Update], Interested):
    __slots__ = ("interests", "handler")
    interests: tuple[Interest, ...]

    def __init__(
        self,
        interests: Interest | Iterable[Interest],
        handler: "Handler[M]",
    ) -> None:
        if isinstance(interests, Interest):
            self.interests = (interests, )
        else:
            self.interests = tuple(interests)
        self.handler = unwrap(handler)

    def collect_interests(self) -> set[Interest]:
        return set(self.interests)
    
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
