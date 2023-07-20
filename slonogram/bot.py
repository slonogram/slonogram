import warnings
from adaptix import Retort, name_mapping

from typing import Optional, Self

from .types.api_session import ApiSession
from .schemas import Message, Update

from .consts import DEFAULT_API_URL
from .call_groups import chat, user, update, query


class Bot:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[ApiSession] = None,
    ) -> None:
        u_session: ApiSession
        retort = Retort(
            debug_path=True,
            recipe=[
                name_mapping(Update, map={"id": "update_id"}),
                name_mapping(Message, map={"id": "message_id"}),
                name_mapping(trim_trailing_underscore=True),
            ],
        )

        if session is None:
            from .extra.aiohttp_session import Session

            if token is None:
                raise ValueError("No bot token passed")

            u_session = Session(
                token=token, base_url=base_url or DEFAULT_API_URL
            )
        else:
            u_session = session

        self.chat = chat.ChatCallGroup(retort, u_session)
        self.user = user.UserCallGroup(retort, u_session)
        self.update = update.UpdateCallGroup(retort, u_session)
        self.query = query.QueryCallGroup(retort, u_session)

        self._session = u_session
        self._finalized = False

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        _ = exc_value
        _ = traceback

        await self.finalize()
        if exc_type is not None:
            raise exc_type

    async def finalize(self) -> None:
        if self._finalized:
            warnings.warn(
                "tried to call `finalize` when `Bot`"
                " instance is already finalized."
            )
            return

        await self._session.finalize()
        self._finalized = True

    def __del__(self) -> None:
        if not self._finalized:
            warnings.warn(
                "`Bot` is not finalized properly, you can do"
                " this either by calling `await bot.finalize()` or wrapping "
                "`Bot` creation in the `async with` context"
            )
