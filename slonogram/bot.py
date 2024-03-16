from typing import AsyncIterator, Self
from contextlib import asynccontextmanager

from .abstract.session import Session
from .omittable import Omittable, OMIT

class Bot:
    def __init__(self, session: Session) -> None:
        self.session = session

    @classmethod
    @asynccontextmanager
    async def from_defaults(
        cls,
        base_url: Omittable[str] = OMIT,
    ) -> AsyncIterator[Self]:
        from .extra.aiohttp import AiohttpSession

        async with AiohttpSession.from_options(base_url=base_url) as session:
            yield cls(session)


__all__ = ["Bot"]
