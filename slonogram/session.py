from __future__ import annotations

from .exceptions.api import ApiError

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
    def __init__(
        self,
        retort: Retort,
        *,
        max_retries: int = 10,
        retry_after_factory: float = 1.5,
    ) -> None:
        self.retort = retort
        self.retry_after_factor = retry_after_factory
        self.max_retries = max_retries

    async def call_method(
        self,
        name: str,
        args: T,
    ) -> Any:
        """Calls specified method of the telegram api

        :param name: name of the method
        :param args: Arguments for the method

        :raises: `slonogram.exceptions.api.ApiError` if call failed
        :return: Response of the telegram api, directly the `result` payload
        """

        retries = 0
        wait: float = 1

        while True:
            try:
                return await self._call_method_impl(name, args)
            except ApiError[Any] as exc:
                if exc.details.code == 429 and retries < self.max_retries:
                    wait *= self.retry_after_factor
                    retries += 1
                    continue
                raise exc

    @abstractmethod
    def _call_method_impl(
        self,
        name: str,
        args: T,
    ) -> Awaitable[Any]:
        raise NotImplementedError


__all__ = ["Session"]
