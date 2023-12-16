# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from io import IOBase
from slonogram.schemas import (
    ForceReply,
    ReplyKeyboardMarkup,
    MessageEntity,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
)


@dataclass(frozen=False, slots=True)
class SendVideo:
    """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    video: IOBase | str
    """Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    duration: int | None = None
    """Duration of sent video in seconds """
    width: int | None = None
    """Video width """
    height: int | None = None
    """Video height """
    thumbnail: IOBase | str | None = None
    """Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Mode for parsing entities in the video caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode """
    has_spoiler: bool | None = None
    """Pass True if the video needs to be covered with a spoiler animation """
    supports_streaming: bool | None = None
    """Pass True if the uploaded video is suitable for streaming """
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


__all__ = ["SendVideo"]
