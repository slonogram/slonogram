# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from slonogram.schemas import MessageEntity, InlineKeyboardMarkup
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditMessageCaption:
    """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""

    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message to edit """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    caption: str | None = None
    """New caption of the message, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Mode for parsing entities in the message caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for an inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditMessageCaption"]
