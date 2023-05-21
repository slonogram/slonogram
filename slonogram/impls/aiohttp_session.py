from typing import Dict
from adaptix import Retort
from aiohttp import ClientSession
from typing import Type, TypeVar

from slonogram.protocols.session import Session
from slonogram.schemas.result import Result

try:
    from orjson import loads as parse_json
except ImportError:
    from json import loads as parse_json

T = TypeVar("T")


class AiohttpSession(Session):
    def __init__(self, retort: Retort, token: str, api_url: str) -> None:
        self._token = token
        self._url = api_url
        self._retort = retort
        self._session = ClientSession()

    async def raw_method(
            self, ty: Type[T], method_name: str, args: Dict
    ) -> Result[T]:
        async with self._session.post(
                self._url.format(method=method_name), data=args
        ) as response:
            data = await response.read()
            json = parse_json(data)

            return self._retort.load(json, Result[ty])  # type: ignore

    async def finalize(self) -> None:
        await self._session.close()
