from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from io import IOBase
from typing import Awaitable, Any

from ..const import DEFAULT_TELEGRAM_ENDPOINT


class NO_RESPONSE:
    __slots__ = ()


@dataclass(slots=True)
class MethodCall:
    name: str
    args: dict[str, str]
    files: dict[str, IOBase]

    response: Any | type[NO_RESPONSE]


class ApiGate(metaclass=ABCMeta):
    def __init__(
        self,
        endpoint: str | None = None,
    ) -> None:
        if endpoint is None:
            endpoint = DEFAULT_TELEGRAM_ENDPOINT

        endpoint = endpoint.rstrip("/")
        self.endpoint = endpoint

    @abstractmethod
    def call_method(
        self,
        call: MethodCall,
    ) -> Awaitable[Any]:
        raise NotImplementedError


__all__ = [
    "ApiGate",
    "MethodCall",
    "NO_RESPONSE",
]
