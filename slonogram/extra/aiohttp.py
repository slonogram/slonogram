import typing as t
from contextlib import asynccontextmanager

from ..consts import DEFAULT_API_ENDPOINT

from ..utils.omit import OMIT, Omittable, non_omitted_or
from ..utils.altering import Alterer1, alter1

from ..session.extended import Session
from ..session.request import Request
from ..session.response import Response

from aiohttp import ClientSession


class AiohttpSession(Session):
    __slots__ = ('inner', 'api_endpoint', 'token')

    def __init__(
        self,
        inner: ClientSession,
        token: str,
        api_endpoint: Omittable[str] = OMIT,
    ) -> None:
        self.inner = inner
        self.token = token
        self.api_endpoint = non_omitted_or(api_endpoint, DEFAULT_API_ENDPOINT).removesuffix('/')

    def alter(
        self,
        *,
        inner: Omittable[Alterer1[ClientSession]] = OMIT,
        token: Omittable[Alterer1[str]] = OMIT,
        api_endpoint: Omittable[Alterer1[str]] = OMIT,
    ) -> t.Self:
        return type(self)(
            inner=alter1(inner, self.inner),
            token=alter1(token, self.token),
            api_endpoint=alter1(api_endpoint, self.api_endpoint),
        )

    def __repr__(self) -> str:
        return f"AiohttpSession(token=<REDACTED>, api_endpoint={self.api_endpoint!r})"

    async def __call__(self, request: Request) -> Response:
        raise NotImplementedError


@asynccontextmanager
async def create_session(
    token: str,
    api_endpoint: Omittable[str] = OMIT,
    session_factory: Omittable[t.Callable[[], ClientSession]] = OMIT
) -> t.AsyncIterator[AiohttpSession]:
    factory = t.cast(t.Callable[[], ClientSession], non_omitted_or(session_factory, ClientSession))

    async with factory() as aiohttp_session:
        yield AiohttpSession(aiohttp_session, token, api_endpoint)


__all__ = ["AiohttpSession"]

