from contextlib import asynccontextmanager
from io import IOBase
from typing import (
    Any,
    AsyncIterator,
    TypeVar,
    Callable,
)

from aiohttp import ClientSession
from adaptix import Retort

from . import BASE_URL

from slonogram.utils import parse_json
from slonogram.exceptions.api import ApiError, ErrorDetails
from slonogram.session import CanCollectAttachs, Session


T = TypeVar("T", bound=CanCollectAttachs)


class AiohttpSession(Session):
    __slots__ = ("token", "session", "retort")

    def __init__(
        self,
        session: ClientSession,
        token: str,
        retort: Retort,
    ) -> None:
        self.token = token
        self.session = session
        self.retort = retort

    async def call_method(self, name: str, args: T) -> Any:
        files: dict[str, IOBase] = {}
        args.collect_attachs(files)

        data = self.retort.dump(args)
        for attach_id, fp in files.items():
            data[attach_id] = fp

        async with self.session.post(f"/bot{self.token}/{name}", data=data) as response:
            result = parse_json(await response.read())
            if result["ok"]:
                return result["result"]
            raise ApiError(
                name,
                args,
                ErrorDetails(
                    result["error_code"],
                    result["description"],
                ),
            )


@asynccontextmanager
async def create_session(
    token: str,
    base_url: str = BASE_URL,
) -> AsyncIterator[Callable[[Retort], AiohttpSession]]:
    async with ClientSession(base_url=base_url) as http_session:
        yield lambda retort: AiohttpSession(http_session, token, retort)


__all__ = ["AiohttpSession", "create_session"]
