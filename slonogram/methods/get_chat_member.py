# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetChatMember:
    """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername) """
    user_id: int
    """Unique identifier of the target user """


__all__ = ["GetChatMember"]
