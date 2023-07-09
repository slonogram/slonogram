from __future__ import annotations
from anyio.abc import TaskGroup

from typing import TypeVar, Generic, Any

from .event_flags import EventFlags
from .scratch_pad import ScratchPad

from ..schemas import User
from ..bot import Bot


T = TypeVar("T")
R = TypeVar("R")


class InterContextData:
    __slots__ = "data", "bot", "me", "task_group"

    def __init__(
        self, me: User, data: Any, bot: Bot, task_group: TaskGroup
    ) -> None:
        self.data = data
        self.bot = bot
        self.me = me
        self.task_group = task_group


class Context(Generic[T]):
    __slots__ = "pad", "inter", "flags"

    def __init__(
        self, inter: InterContextData, flags: EventFlags, model: T
    ) -> None:
        self.flags = flags
        self.inter = inter
        self.pad = ScratchPad[T](model)

    @property
    def model(self) -> T:
        return self.pad._model

    @model.setter
    def model(self, value: T) -> None:
        self.pad._model = value
