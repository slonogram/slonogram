from __future__ import annotations
from anyio.abc import TaskGroup

from typing import TypeVar, Generic, Dict, Any, Type

from ..protocols.patch_id import PatchId
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
    __slots__ = "model", "inter", "_patches"

    _patches: Dict[Type[PatchId[T, Any]], Any]

    def __init__(self, inter: InterContextData[D], model: T) -> None:
        self._patches = {}
        self.model = model
        self.inter = inter

    def patched(self, ty: Type[PatchId[T, R]]) -> R:
        try:
            return self._patches[ty]
        except KeyError:
            return ty.read(self.model)

    def patch(self, ty: Type[PatchId[T, R]], p: R) -> None:
        self._patches[ty] = p
