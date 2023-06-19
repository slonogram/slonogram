from typing import TypeVar, Generic
from ..bot import Bot


T = TypeVar("T")
D = TypeVar("D")


class InterContextData(Generic[D]):
    __slots__ = "data", "bot"

    def __init__(self, data: D, bot: Bot) -> None:
        self.data = data
        self.bot = bot


class Context(Generic[D, T]):
    model: T
    inter: InterContextData[D]

    def __init__(
        self, inter: InterContextData[D], bot: Bot, model: T
    ) -> None:
        self.bot = bot
        self.model = model
        self.inter = inter
