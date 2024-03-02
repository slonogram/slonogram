from typing import (
    Protocol,
    TypeVar,
    Awaitable,
    Iterable,
)

from ..bot import Bot
from ..handling.activation import Activation

from .stash import Stash
from .context import Context

M = TypeVar("M", contravariant=True)

class BasicDispatcher(Protocol[M]):
    def __call__(
        self,
        bot: Bot,
        stash: Stash,
        models: Iterable[M],
    ) -> Awaitable[Activation]:
        ...


__all__ = ["BasicDispatcher"]
