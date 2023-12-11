from aiohttp import ClientSession

from typing import Any, AsyncIterator, Awaitable, BinaryIO
from . import BASE_URL

from contextlib import asynccontextmanager
from slonogram.session import AllowedType, Session


class AiohttpSession(Session):
    __slots__ = ("token", "session")

    def __init__(self, session: ClientSession, token: str) -> None:
        self.token = token
        self.session = session

    def call_method(
        self,
        name: str,
        args: dict[str, AllowedType] | None = None,
        files: dict[str, BinaryIO] | None = None,
    ) -> Awaitable[Any]:
        raise NotImplementedError


@asynccontextmanager
async def create_session(
    token: str, base_url: str = BASE_URL
) -> AsyncIterator[Session]:
    async with ClientSession(base_url=base_url) as http_session:
        yield AiohttpSession(http_session, token)


__all__ = ["AiohttpSession", "create_session"]
