from typing import Awaitable, Optional, List  # noqa
from slonogram import schemas  # noqa
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps  # noqa


class UserCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    def get_me(self) -> Awaitable[schemas.User]:
        """
        A simple method for testing your bot's authentication token.
        Requires no parameters. Returns basic information about the bot
        in form of a User object. for more:
        https://core.telegram.org/bots/api#getme
        :return: See link mentioned above for more information
        """
        params: dict = {}

        return self._session.call_method(schemas.User, "getMe", params)
