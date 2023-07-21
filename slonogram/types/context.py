from __future__ import annotations
from anyio.abc import TaskGroup

from typing import TypeVar, Generic, Any

from .fsm import FSMStorage
from .event_flags import EventFlags
from .scratch_pad import ScratchPad

from ..schemas import User
from ..bot import Bot


T = TypeVar("T")
R = TypeVar("R")


class InterContextData:
    __slots__ = "data", "bot", "me", "task_group", "fsm_storage"

    def __init__(
        self,
        me: User,
        fsm_storage: FSMStorage,
        data: Any,
        bot: Bot,
        task_group: TaskGroup,
    ) -> None:
        self.data = data
        self.bot = bot
        self.me = me
        self.fsm_storage = fsm_storage
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
        return self.pad._model  # noqa

    @model.setter
    def model(self, value: T) -> None:
        self.pad._model = value
