# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import (
    ForceReply,
    ReplyKeyboardMarkup,
    MessageEntity,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
)


@dataclass(frozen=False, slots=True)
class SendMessage:
    """Use this method to send text messages. On success, the sent Message is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    text: str
    """Text of the message to be sent, 1-4096 characters after entities parsing """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    parse_mode: str | None = None
    """Mode for parsing entities in the message text. See formatting options for more details. """
    entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode """
    disable_web_page_preview: bool | None = None
    """Disables link previews for links in this message """
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


__all__ = ["SendMessage"]
