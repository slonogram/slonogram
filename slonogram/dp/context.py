from __future__ import annotations
from anyio.abc import TaskGroup

from typing import TypeVar, Generic

from ..handling.scratches.pad import ScratchPad
from ..bot import Bot


T = TypeVar("T")
D = TypeVar("D")
R = TypeVar("R")


class InterContextData(Generic[D]):
    __slots__ = "data", "bot", "task_group"

    def __init__(self, data: D, bot: Bot, task_group: TaskGroup) -> None:
        self.data = data
        self.bot = bot
        self.task_group = task_group


class Context(Generic[D, T]):
    def __init__(self, inter: InterContextData[D], model: T) -> None:
        self.inter = inter
        self.pad = ScratchPad[T](model)

    @property
    def model(self) -> T:
        return self.pad._model

    @model.setter
    def model(self, value: T) -> None:
        self.pad._model = value
