import warnings

from typing import Self

from .types.api_session import ApiSession
from .call_groups import chat, user, update, query


class Bot:
    def __init__(
        self,
        session: ApiSession,
    ) -> None:
        self.chat = chat.ChatCallGroup(session)
        self.user = user.UserCallGroup(session)
        self.update = update.UpdateCallGroup(session)
        self.query = query.QueryCallGroup(session)

        self._session = session
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
