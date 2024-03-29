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
class SwitchInlineQueryChosenChat:
    """This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline
    query.  Telegram documentation:
    https://core.telegram.org/bots/api#switchinlinequerychosenchat"""

    allow_bot_chats: bool | None = None
    """Optional. True, if private chats with bots can be chosen"""
    allow_channel_chats: bool | None = None
    """Optional. True, if channel chats can be chosen"""
    allow_group_chats: bool | None = None
    """Optional. True, if group and supergroup chats can be chosen"""
    allow_user_chats: bool | None = None
    """Optional. True, if private chats with users can be chosen"""
    query: str | None = None
    """Optional. The default inline query to be inserted in the input field.
    If left empty, only the bot's username will be inserted"""

    def alter(
        self,
        allow_bot_chats: Omittable[Alterer1[bool | None]] = OMIT,
        allow_channel_chats: Omittable[Alterer1[bool | None]] = OMIT,
        allow_group_chats: Omittable[Alterer1[bool | None]] = OMIT,
        allow_user_chats: Omittable[Alterer1[bool | None]] = OMIT,
        query: Omittable[Alterer1[str | None]] = OMIT,
    ) -> SwitchInlineQueryChosenChat:
        return SwitchInlineQueryChosenChat(
            allow_bot_chats=alter1(allow_bot_chats, self.allow_bot_chats),
            allow_channel_chats=alter1(allow_channel_chats, self.allow_channel_chats),
            allow_group_chats=alter1(allow_group_chats, self.allow_group_chats),
            allow_user_chats=alter1(allow_user_chats, self.allow_user_chats),
            query=alter1(query, self.query),
        )


__all__ = ["SwitchInlineQueryChosenChat"]
