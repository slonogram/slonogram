from anyio.abc import TaskGroup

from typing import TypeVar, Generic
from ..bot import Bot


T = TypeVar("T")
D = TypeVar("D")


class InterContextData(Generic[D]):
    __slots__ = "data", "bot", "task_group"

    def __init__(self, data: D, bot: Bot, task_group: TaskGroup) -> None:
        self.data = data
        self.bot = bot
        self.task_group = task_group


class Context(Generic[D, T]):
    __slots__ = "model", "inter"

    def __init__(self, inter: InterContextData[D], model: T) -> None:
        self.model = model
        self.inter = inter
