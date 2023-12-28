from typing import Any, Awaitable, TypeVar
from slonogram.session import Session

T = TypeVar("T")


class MockSession(Session):
    def _call_method_impl(
        self,
        name: str,
        args: T,
    ) -> Awaitable[Any]:
        raise NotImplementedError


__all__ = ["MockSession"]
