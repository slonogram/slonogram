# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 15:06:50.427429
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SendChatAction:
    """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
    We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.
    """

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    action: str
    """Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes. """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread; supergroups only """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SendChatAction"]
