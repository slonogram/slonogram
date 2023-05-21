from typing import Dict
from adaptix import Retort
from aiohttp import ClientSession
from typing import Type, TypeVar

from ..schemas.result import Result
from ..exceptions.api_error import ApiError
from ..utils.json import loads as parse_json

T = TypeVar("T")


class AiohttpSession:
    def __init__(self, retort: Retort, token: str, api_url: str) -> None:
        self._token = token
        self._url = api_url
        self._retort = retort
        self._session = ClientSession()

    async def raw_method(
        self,
        ty: Type[T],
        method_name: str,
        args: Dict,
        raise_if_error: bool = True,
    ) -> Result[T]:
        async with self._session.post(
            self._url.format(method=method_name), data=args
        ) as response:
            data = await response.read()
            json = parse_json(data)

            result = self._retort.load(json, Result[ty])  # type: ignore
            if raise_if_error and not result.ok:
                raise ApiError(
                    error_code=result.error_code,  # type: ignore
                    description=result.description,  # type: ignore
                )
            return result

    async def finalize(self) -> None:
        await self._session.close()
