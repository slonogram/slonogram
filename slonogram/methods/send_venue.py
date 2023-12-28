# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from slonogram.schemas import (
    ForceReply,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
)
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SendVenue:
    """Use this method to send information about a venue. On success, the sent Message is returned."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    latitude: float
    """Latitude of the venue """
    longitude: float
    """Longitude of the venue """
    title: str
    """Name of the venue """
    address: str
    """Address of the venue """
    message_thread_id: int | None = None
    """Unique identifier for the target message thread (topic) of the forum; for forum supergroups only """
    foursquare_id: str | None = None
    """Foursquare identifier of the venue """
    foursquare_type: str | None = None
    """Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str | None = None
    """Google Places identifier of the venue """
    google_place_type: str | None = None
    """Google Places type of the venue. (See supported types.) """
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


__all__ = ["SendVenue"]
