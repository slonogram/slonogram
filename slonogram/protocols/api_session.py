from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Dict, AnyStr, TypeAlias, Any

HttpSerializable: TypeAlias = AnyStr | float | int | bool
MethodArgs: TypeAlias = Dict[AnyStr, HttpSerializable]


class ApiSession(metaclass=ABCMeta):
    @abstractmethod
    async def call_method(
        self, method: str, args: MethodArgs
    ) -> Dict[AnyStr, Any]:
        raise NotImplementedError

    @abstractmethod
    async def finalize(self) -> None:
        pass


__all__ = ["HttpSerializable", "MethodArgs", "ApiSession"]
