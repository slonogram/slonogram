# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from slonogram.schemas import LabeledPrice
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class CreateInvoiceLink:
    """Use this method to create a link for an invoice. Returns the created invoice link as String on success."""

    title: str
    """Product name, 1-32 characters """
    description: str
    """Product description, 1-255 characters """
    payload: str
    """Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes. """
    provider_token: str
    """Payment provider token, obtained via BotFather """
    currency: str
    """Three-letter ISO 4217 currency code, see more on currencies """
    prices: list[LabeledPrice]
    """Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.) """
    max_tip_amount: int | None = None
    """The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0 """
    suggested_tip_amounts: list[int] | None = None
    """A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount. """
    provider_data: str | None = None
    """JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider. """
    photo_url: str | None = None
    """URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. """
    photo_size: int | None = None
    """Photo size in bytes """
    photo_width: int | None = None
    """Photo width """
    photo_height: int | None = None
    """Photo height """
    need_name: bool | None = None
    """Pass True if you require the user's full name to complete the order """
    need_phone_number: bool | None = None
    """Pass True if you require the user's phone number to complete the order """
    need_email: bool | None = None
    """Pass True if you require the user's email address to complete the order """
    need_shipping_address: bool | None = None
    """Pass True if you require the user's shipping address to complete the order """
    send_phone_number_to_provider: bool | None = None
    """Pass True if the user's phone number should be sent to the provider """
    send_email_to_provider: bool | None = None
    """Pass True if the user's email address should be sent to the provider """
    is_flexible: bool | None = None
    """Pass True if the final price depends on the shipping method """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["CreateInvoiceLink"]
