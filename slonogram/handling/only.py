from typing import (
    TypeVar,
    TYPE_CHECKING,
    Iterable,
    Awaitable,
    Generic,
)

from .extended import ExtendedHandler
from .utils import unwrap_handler

from .._internal.utils import stalled
from ..abstract.interested import Interested
from ..types.interest import Interest
from ..types.context import Context
from ..reflect.named import get_name


if TYPE_CHECKING:
    from ..handling.handler import Handler
    from ..handling.activation import Activation

from ..schemas.update import Update

M = TypeVar("M")

class Only(Generic[M], ExtendedHandler[Update], Interested):
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
        self.handler = unwrap_handler(handler)
        self.__name__ = get_name(handler, '')

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
