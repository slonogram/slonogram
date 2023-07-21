from typing import TypeVar, Type
from adaptix import Retort

from ..consts import DEFAULT_API_URL, DEFAULT_RETORT

try:
    from aiohttp import ClientSession
except ImportError as ie:
    raise ImportError(
        "failed to import `aiohttp`, install slonogram[aiohttp] "
        "to use aiohttp client"
    ) from ie

from ..exceptions.api_error import ApiError
from ..types.api_session import ApiSession, MethodArgs
from ..utils.json import loads

T = TypeVar("T")


class Session(ApiSession):
    def __init__(
        self,
        token: str,
        retort: Retort = DEFAULT_RETORT,
        base_url: str = DEFAULT_API_URL,
    ) -> None:
        self._retort = retort
        self._token = token
        self._session = ClientSession(base_url=base_url)

    @property
    def retort(self) -> Retort:
        return self._retort

    async def call_method(
        self, tp: Type[T], method: str, args: MethodArgs
    ) -> T:
        async with self._session.post(
            f"/bot{self._token}/{method}", data=args
        ) as response:
            raw = await response.read()
            res = loads(raw)

            if "result" in res:
                return self.retort.load(res["result"], tp)
            raise ApiError(
                code=res["error_code"], description=res["description"]
            )

    async def finalize(self) -> None:
        await self._session.close()


__all__ = ["Session"]
