# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 08:56:56.806984
from dataclasses import dataclass
from slonogram.schemas import InlineKeyboardMarkup
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class StopMessageLiveLocation:
    """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""

    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message with live location to stop """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for a new inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["StopMessageLiveLocation"]
