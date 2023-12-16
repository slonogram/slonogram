# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import InlineKeyboardMarkup


@dataclass(frozen=False, slots=True)
class SendGame:
    """Use this method to send a game. On success, the sent Message is returned."""

    chat_id: int
    """Unique identifier for the target chat """
    game_short_name: str
    """Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather. """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    disable_notification: bool | None = None
    """Sends the message silently. Users will receive a notification with no sound. """
    protect_content: bool | None = None
    """Protects the contents of the sent message from forwarding and saving """
    reply_to_message_id: int | None = None
    """If the message is a reply, ID of the original message """
    allow_sending_without_reply: bool | None = None
    """Pass True if the message should be sent even if the specified replied-to message is not found """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game. """


__all__ = ["SendGame"]
