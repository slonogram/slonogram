# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 17:59:35.955291
from dataclasses import dataclass
from slonogram.schemas import (
    InputMediaVideo,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaDocument,
)
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SendMediaGroup:
    """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    media: list[InputMediaAudio] | list[InputMediaDocument] | list[
        InputMediaPhoto
    ] | list[InputMediaVideo]
    """A JSON-serialized array describing messages to be sent, must include 2-10 items """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    disable_notification: bool | None = None
    """Sends messages silently. Users will receive a notification with no sound. """
    protect_content: bool | None = None
    """Protects the contents of the sent messages from forwarding and saving """
    reply_to_message_id: int | None = None
    """If the messages are a reply, ID of the original message """
    allow_sending_without_reply: bool | None = None
    """Pass True if the message should be sent even if the specified replied-to message is not found """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        collect_attachs_from(self.media, dest)


__all__ = ["SendMediaGroup"]
