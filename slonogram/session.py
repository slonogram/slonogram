from abc import ABCMeta, abstractmethod
from typing import TypeAlias, Awaitable, Any, BinaryIO

AllowedType: TypeAlias = float | int | bool | str


class Session(metaclass=ABCMeta):
    @abstractmethod
    def call_method(
        self,
        name: str,
        args: dict[str, AllowedType] | None = None,
        files: dict[str, BinaryIO] | None = None,
    ) -> Awaitable[Any]:
        """Calls specified method of the telegram api

        :param name: name of the method
        :param args: scalar arguments for the method, can be float, int, bool or str

        :raises: `slonogram.exceptions.api.ApiError` if call failed
        :return: Response of the telegram api, directly the `result` payload
        """
        raise NotImplementedError


__all__ = ["Session", "AllowedType"]
