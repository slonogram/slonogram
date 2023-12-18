# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class UnpinChatMessage:
    """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["UnpinChatMessage"]
