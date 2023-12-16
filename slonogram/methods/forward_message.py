# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class ForwardMessage:
    """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    from_chat_id: int | str
    """Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername) """
    message_id: int
    """Message identifier in the chat specified in from_chat_id """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    disable_notification: bool | None = None
    """Sends the message silently. Users will receive a notification with no sound. """
    protect_content: bool | None = None
    """Protects the contents of the forwarded message from forwarding and saving """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["ForwardMessage"]
