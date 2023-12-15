from aiohttp import ClientSession

from typing import Any, AsyncIterator, BinaryIO
from . import BASE_URL

from slonogram.exceptions.api import ApiError, ErrorDetails

from contextlib import asynccontextmanager
from slonogram.session import AllowedType, Session


class AiohttpSession(Session):
    __slots__ = ("token", "session")

    def __init__(self, session: ClientSession, token: str) -> None:
        self.token = token
        self.session = session

    async def call_method(
        self,
        name: str,
        args: dict[str, AllowedType] | None = None,
        files: dict[str, BinaryIO] | None = None,
    ) -> Any:
        args: dict[str, Any]  # type: ignore
        if args is None:
            args = {}
        if files is not None:
            for k in args.keys():
                val = args[k]
                if not isinstance(val, str):
                    args[k] = str(val)

            args.update(files)  # type: ignore

        async with self.session.post(f"/bot{self.token}/{name}", data=args) as response:
            js = await response.json()
            if js["ok"]:
                return js["result"]
            raise ApiError(
                method_name=name,
                args=args,
                error=ErrorDetails(
                    code=js["error_code"], description=js["description"]
                ),
            )


@asynccontextmanager
async def create_session(
    token: str, base_url: str = BASE_URL
) -> AsyncIterator[Session]:
    async with ClientSession(base_url=base_url) as http_session:
        yield AiohttpSession(http_session, token)


__all__ = ["AiohttpSession", "create_session"]
