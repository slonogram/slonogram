from __future__ import annotations

from abc import ABCMeta, abstractmethod
from adaptix import Retort
from io import IOBase
from typing import (
    Awaitable,
    Any,
    Protocol,
    TypeVar,
)


class CanCollectAttachs(Protocol):
    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        ...


T = TypeVar("T", bound=CanCollectAttachs)


class Session(metaclass=ABCMeta):
    def __init__(self, retort: Retort) -> None:
        self.retort = retort

    @abstractmethod
    def call_method(
        self,
        name: str,
        args: T,
    ) -> Awaitable[Any]:
        """Calls specified method of the telegram api

        :param name: name of the method
        :param args: Arguments for the method

        :raises: `slonogram.exceptions.api.ApiError` if call failed
        :return: Response of the telegram api, directly the `result` payload
        """
        raise NotImplementedError


__all__ = ["Session"]
