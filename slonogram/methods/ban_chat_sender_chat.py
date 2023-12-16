# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class BanChatSenderChat:
    """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    sender_chat_id: int
    """Unique identifier of the target sender chat """


__all__ = ["BanChatSenderChat"]