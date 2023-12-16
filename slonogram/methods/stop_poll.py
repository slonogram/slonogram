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
class StopPoll:
    """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int
    """Identifier of the original message with the poll """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for a new message inline keyboard. """


__all__ = ["StopPoll"]
