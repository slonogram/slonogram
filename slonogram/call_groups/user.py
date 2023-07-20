from typing import Awaitable, Optional, List  # noqa
import slonogram.schemas  # noqa
from adaptix import Retort
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps  # noqa


class UserCallGroup:
    __slots__ = "_retort", "_session"

    def __init__(self, session: ApiSession, retort: Retort) -> None:
        self._session = session
        self._retort = retort

    async def get_me(self) -> slonogram.schemas.User:
        """
        A simple method for testing your bot's authentication token.
        Requires no parameters. Returns basic information about the bot
        in form of a User object. for more:
        https://core.telegram.org/bots/api#getme
        :return: See link mentioned above for more information
        """
        params: dict = {}

        return self._retort.load(
            await self._session.call_method("getMe", params),
            slonogram.schemas.User,
        )
