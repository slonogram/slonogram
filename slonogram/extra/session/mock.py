from typing import Any, Awaitable, TypeVar
from slonogram.session import Session

T = TypeVar("T")


class MockSession(Session):
    def call_method(
        self,
        name: str,
        args: T,
    ) -> Awaitable[Any]:
        raise NotImplementedError
