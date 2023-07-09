from typing import Any, Dict, AnyStr

try:
    from aiohttp import ClientSession
except ImportError as ie:
    raise ImportError(
        "failed to import `aiohttp`, install slonogram[aiohttp] "
        "to use aiohttp client"
    ) from ie

from ..types.api_session import ApiSession, MethodArgs
from ..utils.json import loads


class Session(ApiSession):
    def __init__(self, token: str, base_url: str) -> None:
        self._token = token
        self._session = ClientSession(base_url=base_url)

    async def call_method(
        self, method: str, args: MethodArgs
    ) -> Dict[AnyStr, Any]:
        async with self._session.post(
            f"/bot{self._token}/{method}", data=args
        ) as response:
            raw = await response.read()
            return loads(raw)

    async def finalize(self) -> None:
        await self._session.close()


__all__ = ["Session"]
