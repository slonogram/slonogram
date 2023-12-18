# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from io import IOBase
from slonogram.schemas import (
    MessageEntity,
    ForceReply,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SendPhoto:
    """Use this method to send photos. On success, the sent Message is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    photo: IOBase | str
    """Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    caption: str | None = None
    """Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Mode for parsing entities in the photo caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode """
    has_spoiler: bool | None = None
    """Pass True if the photo needs to be covered with a spoiler animation """
    disable_notification: bool | None = None
    """Sends the message silently. Users will receive a notification with no sound. """
    protect_content: bool | None = None
    """Protects the contents of the sent message from forwarding and saving """
    reply_to_message_id: int | None = None
    """If the message is a reply, ID of the original message """
    allow_sending_without_reply: bool | None = None
    """Pass True if the message should be sent even if the specified replied-to message is not found """
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = (
        None
    )
    """Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.photo, IOBase):
            dest[str(id(self.photo))] = self.photo


__all__ = ["SendPhoto"]
