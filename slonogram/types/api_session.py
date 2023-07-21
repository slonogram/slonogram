from __future__ import annotations
from abc import ABCMeta, abstractmethod
from adaptix import Retort
from typing import Dict, AnyStr, TypeAlias, TypeVar, Type

ScalarSerializable: TypeAlias = AnyStr | float | int | bool
MethodArgs: TypeAlias = Dict[AnyStr, ScalarSerializable]
T = TypeVar("T")


class ApiSession(metaclass=ABCMeta):
    @property
    @abstractmethod
    def retort(self) -> Retort:
        raise NotImplementedError

    @abstractmethod
    async def call_method(
        self, tp: Type[T], method: str, args: MethodArgs
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def finalize(self) -> None:
        pass


__all__ = ["ScalarSerializable", "MethodArgs", "ApiSession"]
