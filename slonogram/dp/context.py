from typing import TypeVar, Generic
from ..bot import Bot


T = TypeVar("T")
D = TypeVar("D")


class InterContextData(Generic[D]):
    def __init__(self, data: D) -> None:
        self.data = data


class Context(Generic[D, T]):
    bot: Bot
    model: T

    inter: InterContextData[D]

    def __init__(
        self, inter: InterContextData[D], bot: Bot, model: T
    ) -> None:
        self.bot = bot
        self.model = model
        self.inter = inter
