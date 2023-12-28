from contextlib import asynccontextmanager
from io import IOBase
from typing import (
    Any,
    AsyncIterator,
    cast,
    Callable,
)

from aiohttp import ClientSession

from slonogram.utils.json import parse_json
from slonogram.exceptions.api import ApiError, ErrorDetails
from slonogram.session.gate import ApiGate, MethodCall


class AiohttpGate(ApiGate):
    __slots__ = (
        "token",
        "session",
        "endpoint",
    )

    def __init__(
        self,
        session_factory: Callable[[str], ClientSession],
        token: str,
        *,
        endpoint: str | None = None,
    ) -> None:
        self.token = token
        super().__init__(endpoint)

        self.session = session_factory(self.endpoint)

    async def call_method(
        self,
        call: MethodCall,
    ) -> Any:
        data = cast(dict[str, str | IOBase], call.args)
        data.update(call.files)

        async with self.session.post(
            f"/bot{self.token}/{call.name}",
            data=data,
        ) as response:
            result = parse_json(await response.read())
            try:
                return result["result"]
            except KeyError as exc:
                raise ApiError(
                    call.name,
                    call.args,
                    ErrorDetails(
                        result["error_code"],
                        result["description"],
                    ),
                ) from exc


@asynccontextmanager
async def create_api_gate(
    token: str,
    *,
    endpoint: str | None = None,
) -> AsyncIterator[AiohttpGate]:
    gate = AiohttpGate(
        session_factory=lambda ep: ClientSession(base_url=ep),
        token=token,
        endpoint=endpoint,
    )
    async with gate.session:
        yield gate


__all__ = ["AiohttpGate", "create_api_gate"]
