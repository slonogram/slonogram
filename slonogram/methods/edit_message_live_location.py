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
class EditMessageLiveLocation:
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""

    latitude: float
    """Latitude of new location """
    longitude: float
    """Longitude of new location """
    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message to edit """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    horizontal_accuracy: float | None = None
    """The radius of uncertainty for the location, measured in meters; 0-1500 """
    heading: int | None = None
    """Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. """
    proximity_alert_radius: int | None = None
    """The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for a new inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditMessageLiveLocation"]
