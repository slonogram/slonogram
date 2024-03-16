from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class SwitchInlineQueryChosenChat:
    allow_bot_chats: bool
    """ Optional. True, if private chats with bots can be chosen """
    allow_channel_chats: bool
    """ Optional. True, if channel chats can be chosen """
    allow_group_chats: bool
    """ Optional. True, if group and supergroup chats can be chosen """
    allow_user_chats: bool
    """ Optional. True, if private chats with users can be chosen """
    query: str
    """ Optional. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted """

    def alter(
        self,
        allow_bot_chats: Omittable[Alterer1[bool]] = OMIT,
        allow_channel_chats: Omittable[Alterer1[bool]] = OMIT,
        allow_group_chats: Omittable[Alterer1[bool]] = OMIT,
        allow_user_chats: Omittable[Alterer1[bool]] = OMIT,
        query: Omittable[Alterer1[str]] = OMIT,
    ):
        return SwitchInlineQueryChosenChat(
            allow_bot_chats=alter1(allow_bot_chats, self.allow_bot_chats),
            allow_channel_chats=alter1(allow_channel_chats, self.allow_channel_chats),
            allow_group_chats=alter1(allow_group_chats, self.allow_group_chats),
            allow_user_chats=alter1(allow_user_chats, self.allow_user_chats),
            query=alter1(query, self.query),
        )


__all__ = ["SwitchInlineQueryChosenChat"]
