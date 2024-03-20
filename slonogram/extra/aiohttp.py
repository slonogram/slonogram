from ..abstract.session import FilesMap, Params, Session
from ..consts import DEFAULT_BASE_URL
from ..omittable import (
    Omittable,
    omitted_or,
    OMIT,
    Omit,
)
from ..exceptions.api import APIError
from ..abstract.json import JSONParser

from json import loads
from contextlib import asynccontextmanager
from typing import AsyncIterator, Self, Any, Awaitable

try:
    from aiohttp import ClientSession
except ImportError as e:
    from ..exceptions.no_feature import NoFeatureError

    raise NoFeatureError("aiohttp", "Failed to import `aiohttp` package") from e


class AiohttpSession(Session):
    __slots__ = ("token", "client", "json_parser")

    json_parser: JSONParser

    def __init__(
        self,
        token: str,
        client: ClientSession,
        json_parser: Omittable[JSONParser] = OMIT,
    ) -> None:
        self.token = token
        self.client = client

        if isinstance(json_parser, Omit):
            self.json_parser = loads
        else:
            self.json_parser = json_parser

    async def __call__(
        self,
        name: str,
        params: Params,
        files: FilesMap,
        /
    ) -> Awaitable[Any]:
        async with self.client.post(
            f"/bot{self.token}/{name}",
            data={**params, **files}
        ) as response:
            js = self.json_parser(await response.read())
            try:
                return js['result']
            except KeyError as e:
                raise APIError(
                    js['error_code'],
                    js['description'],
                ) from e

    @classmethod
    @asynccontextmanager
    async def from_options(
        cls,
        token: str,
        json_parser: Omittable[JSONParser] = OMIT,
        base_url: Omittable[str] = OMIT,
    ) -> AsyncIterator[Self]:
        async with ClientSession(
            base_url=omitted_or(base_url, DEFAULT_BASE_URL)
        ) as raw_session:
            session = cls(token, raw_session)
            yield session
            await session.finalize()

    async def finalize(self) -> None:
        await self.client.close()


__all__ = [
    "AiohttpSession",
]
