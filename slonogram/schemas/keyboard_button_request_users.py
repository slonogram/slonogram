"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class KeyboardButtonRequestUsers:
    """This object defines the criteria used to request suitable users. The
    identifiers of the selected users will be shared with the bot when the
    corresponding button is pressed. More about requesting users:
    https://core.telegram.org/bots/features#chat-and-user-selection
    Telegram documentation:
    https://core.telegram.org/bots/api#keyboardbuttonrequestusers"""

    request_id: int
    """Signed 32-bit identifier of the request that will be received back in
    the UsersShared object. Must be unique within the message"""
    max_quantity: int | None = None
    """Optional. The maximum number of users to be selected; 1-10. Defaults
    to 1."""
    user_is_bot: bool | None = None
    """Optional. Pass True to request bots, pass False to request regular
    users. If not specified, no additional restrictions are applied."""
    user_is_premium: bool | None = None
    """Optional. Pass True to request premium users, pass False to request
    non-premium users. If not specified, no additional restrictions are
    applied."""

    def alter(
        self,
        request_id: Omittable[Alterer1[int]] = OMIT,
        max_quantity: Omittable[Alterer1[int | None]] = OMIT,
        user_is_bot: Omittable[Alterer1[bool | None]] = OMIT,
        user_is_premium: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> KeyboardButtonRequestUsers:
        return KeyboardButtonRequestUsers(
            request_id=alter1(request_id, self.request_id),
            max_quantity=alter1(max_quantity, self.max_quantity),
            user_is_bot=alter1(user_is_bot, self.user_is_bot),
            user_is_premium=alter1(user_is_premium, self.user_is_premium),
        )


__all__ = ["KeyboardButtonRequestUsers"]
