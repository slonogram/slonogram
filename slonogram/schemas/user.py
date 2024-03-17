from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class User:
    """This object represents a Telegram user or bot.

    Telegram documentation: https://core.telegram.org/bots/api#user"""

    first_name: str
    """ User's or bot's first name """
    id: int
    """ Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. """
    is_bot: bool
    """ True, if this user is a bot """
    added_to_attachment_menu: bool | None = None
    """ Optional. True, if this user added the bot to the attachment menu """
    can_join_groups: bool | None = None
    """ Optional. True, if the bot can be invited to groups. Returned only in getMe. """
    can_read_all_group_messages: bool | None = None
    """ Optional. True, if privacy mode is disabled for the bot. Returned only in getMe. """
    is_premium: bool | None = None
    """ Optional. True, if this user is a Telegram Premium user """
    language_code: str | None = None
    """ Optional. IETF language tag of the user's language """
    last_name: str | None = None
    """ Optional. User's or bot's last name """
    supports_inline_queries: bool | None = None
    """ Optional. True, if the bot supports inline queries. Returned only in getMe. """
    username: str | None = None
    """ Optional. User's or bot's username """

    def alter(
        self,
        first_name: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[int]] = OMIT,
        is_bot: Omittable[Alterer1[bool]] = OMIT,
        added_to_attachment_menu: Omittable[Alterer1[bool | None]] = OMIT,
        can_join_groups: Omittable[Alterer1[bool | None]] = OMIT,
        can_read_all_group_messages: Omittable[Alterer1[bool | None]] = OMIT,
        is_premium: Omittable[Alterer1[bool | None]] = OMIT,
        language_code: Omittable[Alterer1[str | None]] = OMIT,
        last_name: Omittable[Alterer1[str | None]] = OMIT,
        supports_inline_queries: Omittable[Alterer1[bool | None]] = OMIT,
        username: Omittable[Alterer1[str | None]] = OMIT,
    ) -> User:
        return User(
            first_name=alter1(first_name, self.first_name),
            id=alter1(id, self.id),
            is_bot=alter1(is_bot, self.is_bot),
            added_to_attachment_menu=alter1(
                added_to_attachment_menu, self.added_to_attachment_menu
            ),
            can_join_groups=alter1(can_join_groups, self.can_join_groups),
            can_read_all_group_messages=alter1(
                can_read_all_group_messages, self.can_read_all_group_messages
            ),
            is_premium=alter1(is_premium, self.is_premium),
            language_code=alter1(language_code, self.language_code),
            last_name=alter1(last_name, self.last_name),
            supports_inline_queries=alter1(
                supports_inline_queries, self.supports_inline_queries
            ),
            username=alter1(username, self.username),
        )


__all__ = ["User"]
