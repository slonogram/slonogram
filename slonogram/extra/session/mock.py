from typing import Any, Awaitable, BinaryIO
from slonogram.session import AllowedType, Session


class MockSession(Session):
    def call_method(
        self,
        name: str,
        args: dict[str, AllowedType] | None = None,
        files: dict[str, BinaryIO] | None = None,
    ) -> Awaitable[Any]:
        raise NotImplementedError
