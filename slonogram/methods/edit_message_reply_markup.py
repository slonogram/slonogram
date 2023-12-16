# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from slonogram.schemas import InlineKeyboardMarkup
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditMessageReplyMarkup:
    """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""

    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message to edit """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for an inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditMessageReplyMarkup"]
