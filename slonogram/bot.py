from os import environ
from typing import AsyncIterator, Self
from contextlib import asynccontextmanager

from .abstract.session import Session
from .omittable import Omittable, OMIT

class Bot:
    __slots__ = ("session", )
    def __init__(self, session: Session) -> None:
        self.session = session

    @classmethod
    @asynccontextmanager
    async def from_env(cls, variable: str = 'TG_TOKEN') -> AsyncIterator[Self]:
        token = environ[variable]
        async with cls.from_defaults(token) as bot:
            yield bot

    @classmethod
    @asynccontextmanager
    async def from_defaults(
        cls,
        token: str,
        base_url: Omittable[str] = OMIT,
    ) -> AsyncIterator[Self]:
        from .extra.aiohttp import AiohttpSession

        async with AiohttpSession.from_options(token, base_url=base_url) as session:
            yield cls(session)


__all__ = ["Bot"]
