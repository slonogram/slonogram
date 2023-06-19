from typing import Optional, Self
from .schemas.user import User

from .protocols.api_session import ApiSession
from .consts import DEFAULT_API_URL


class Bot:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[ApiSession] = None,
    ) -> None:
        u_session: ApiSession

        if session is None:
            from .extra.aiohttp_session import Session

            if token is None:
                raise ValueError("No bot token passed")

            u_session = Session(
                token=token, base_url=base_url or DEFAULT_API_URL
            )
        else:
            u_session = session

        self._me: Optional[User] = None
        self._session = u_session

    @property
    def initialized(self) -> bool:
        return self._me is not None

    @property
    def me(self) -> User:
        me = self._me
        if me is None:
            raise TypeError(
                "`me` is None, to access `me` through the `Bot` type "
                "it is necessary to use instance "
                "inside the `async with` context"
            )
        return me

    async def __aenter__(self) -> Self:
        # TODO: add initialization
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        _ = exc_value
        _ = traceback

        await self._session.finalize()
        if exc_type is not None:
            raise exc_type
