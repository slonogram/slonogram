# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from slonogram.schemas import ShippingOption
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class AnswerShippingQuery:
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""

    shipping_query_id: str
    """Unique identifier for the query to be answered """
    ok: bool
    """Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible) """
    shipping_options: list[ShippingOption] | None = None
    """Required if ok is True. A JSON-serialized array of available shipping options. """
    error_message: str | None = None
    """Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["AnswerShippingQuery"]
