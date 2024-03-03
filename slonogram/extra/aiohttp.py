from ..abstract.session import Session
from ..consts import DEFAULT_BASE_URL
from ..omittable import (
    Omittable,
    omitted_or,
    OMIT,
)

from contextlib import asynccontextmanager
from typing import AsyncIterator, Self

try:
    from aiohttp import ClientSession
except ImportError as e:
    from ..exceptions.no_feature import NoFeatureError

    raise NoFeatureError('aiohttp', 'Failed to import `aiohttp` package') from e

class AiohttpSession(Session):
    def __init__(
        self,
        client: ClientSession,
    ) -> None:
        self.client = client

    @classmethod
    @asynccontextmanager
    async def from_options(
        cls,
        base_url: Omittable[str] = OMIT,
    ) -> AsyncIterator[Self]:
        async with ClientSession(base_url=omitted_or(base_url, DEFAULT_BASE_URL)) as raw_session:
            session = cls(raw_session)
            yield session
            await session.finalize()

    async def finalize(self) -> None:
        await self.client.close()


__all__ = [
    "AiohttpSession",
]
