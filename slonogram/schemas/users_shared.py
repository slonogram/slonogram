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
class UsersShared:
    """This object contains information about the users whose identifiers
    were shared with the bot using a KeyboardButtonRequestUsers button.
    Telegram documentation: https://core.telegram.org/bots/api#usersshared"""

    request_id: int
    """Identifier of the request"""
    user_ids: tuple[int, ...]
    """Identifiers of the shared users. These numbers may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting them. But they have at most
    52 significant bits, so 64-bit integers or double-precision float
    types are safe for storing these identifiers. The bot may not have
    access to the users and could be unable to use these identifiers,
    unless the users are already known to the bot by some other means."""

    def alter(
        self,
        request_id: Omittable[Alterer1[int]] = OMIT,
        user_ids: Omittable[Alterer1[tuple[int, ...]]] = OMIT,
    ) -> UsersShared:
        return UsersShared(
            request_id=alter1(request_id, self.request_id),
            user_ids=alter1(user_ids, self.user_ids),
        )


__all__ = ["UsersShared"]
