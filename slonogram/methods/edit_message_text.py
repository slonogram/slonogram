# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from slonogram.schemas import MessageEntity, InlineKeyboardMarkup
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditMessageText:
    """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""

    text: str
    """New text of the message, 1-4096 characters after entities parsing """
    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message to edit """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    parse_mode: str | None = None
    """Mode for parsing entities in the message text. See formatting options for more details. """
    entities: list[MessageEntity] | None = None
    """A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode """
    disable_web_page_preview: bool | None = None
    """Disables link previews for links in this message """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for an inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditMessageText"]
