# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 17:59:35.955291
from dataclasses import dataclass
from slonogram.schemas import (
    MessageEntity,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
)
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SendPoll:
    """Use this method to send a native poll. On success, the sent Message is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    question: str
    """Poll question, 1-300 characters """
    options: list[str]
    """A JSON-serialized list of answer options, 2-10 strings 1-100 characters each """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    is_anonymous: bool | None = None
    """True, if the poll needs to be anonymous, defaults to True """
    type: str | None = None
    """Poll type, "quiz" or "regular", defaults to "regular" """
    allows_multiple_answers: bool | None = None
    """True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False """
    correct_option_id: int | None = None
    """0-based identifier of the correct answer option, required for polls in quiz mode """
    explanation: str | None = None
    """Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing """
    explanation_parse_mode: str | None = None
    """Mode for parsing entities in the explanation. See formatting options for more details. """
    explanation_entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of parse_mode """
    open_period: int | None = None
    """Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date. """
    close_date: int | None = None
    """Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period. """
    is_closed: bool | None = None
    """Pass True if the poll needs to be immediately closed. This can be useful for poll preview. """
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
        pass


__all__ = ["SendPoll"]
