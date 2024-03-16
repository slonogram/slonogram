from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from slonogram.schemas import (
    link_preview_options as _link_preview_options,
    labeled_price as _labeled_price,
    message_entity as _message_entity,
)
from typing import TypeAlias


@model
class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query.
    Telegram docs: https://core.telegram.org/bots/api#inputcontactmessagecontent"""

    first_name: str
    """ Contact's first name """
    last_name: str
    """ Optional. Contact's last name """
    phone_number: str
    """ Contact's phone number """
    vcard: str
    """ Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes """

    def alter(
        self,
        first_name: Omittable[Alterer1[str]] = OMIT,
        phone_number: Omittable[Alterer1[str]] = OMIT,
        last_name: Omittable[Alterer1[str]] = OMIT,
        vcard: Omittable[Alterer1[str]] = OMIT,
    ) -> InputContactMessageContent:
        return InputContactMessageContent(
            first_name=alter1(first_name, self.first_name),
            phone_number=alter1(phone_number, self.phone_number),
            last_name=alter1(last_name, self.last_name),
            vcard=alter1(vcard, self.vcard),
        )


@model
class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query.
    Telegram docs: https://core.telegram.org/bots/api#inputinvoicemessagecontent"""

    currency: str
    """ Three-letter ISO 4217 currency code, see more on currencies """
    description: str
    """ Product description, 1-255 characters """
    is_flexible: bool
    """ Optional. Pass True if the final price depends on the shipping method """
    max_tip_amount: int
    """ Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0 """
    need_email: bool
    """ Optional. Pass True if you require the user's email address to complete the order """
    need_name: bool
    """ Optional. Pass True if you require the user's full name to complete the order """
    need_phone_number: bool
    """ Optional. Pass True if you require the user's phone number to complete the order """
    need_shipping_address: bool
    """ Optional. Pass True if you require the user's shipping address to complete the order """
    payload: str
    """ Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes. """
    photo_height: int
    """ Optional. Photo height """
    photo_size: int
    """ Optional. Photo size in bytes """
    photo_url: str
    """ Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. """
    photo_width: int
    """ Optional. Photo width """
    prices: list[_labeled_price.LabeledPrice]
    """ Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.) """
    provider_data: str
    """ Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider. """
    provider_token: str
    """ Payment provider token, obtained via @BotFather """
    send_email_to_provider: bool
    """ Optional. Pass True if the user's email address should be sent to provider """
    send_phone_number_to_provider: bool
    """ Optional. Pass True if the user's phone number should be sent to provider """
    suggested_tip_amounts: list[int]
    """ Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount. """
    title: str
    """ Product name, 1-32 characters """

    def alter(
        self,
        currency: Omittable[Alterer1[str]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        payload: Omittable[Alterer1[str]] = OMIT,
        prices: Omittable[Alterer1[list[_labeled_price.LabeledPrice]]] = OMIT,
        provider_token: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        is_flexible: Omittable[Alterer1[bool]] = OMIT,
        max_tip_amount: Omittable[Alterer1[int]] = OMIT,
        need_email: Omittable[Alterer1[bool]] = OMIT,
        need_name: Omittable[Alterer1[bool]] = OMIT,
        need_phone_number: Omittable[Alterer1[bool]] = OMIT,
        need_shipping_address: Omittable[Alterer1[bool]] = OMIT,
        photo_height: Omittable[Alterer1[int]] = OMIT,
        photo_size: Omittable[Alterer1[int]] = OMIT,
        photo_url: Omittable[Alterer1[str]] = OMIT,
        photo_width: Omittable[Alterer1[int]] = OMIT,
        provider_data: Omittable[Alterer1[str]] = OMIT,
        send_email_to_provider: Omittable[Alterer1[bool]] = OMIT,
        send_phone_number_to_provider: Omittable[Alterer1[bool]] = OMIT,
        suggested_tip_amounts: Omittable[Alterer1[list[int]]] = OMIT,
    ) -> InputInvoiceMessageContent:
        return InputInvoiceMessageContent(
            currency=alter1(currency, self.currency),
            description=alter1(description, self.description),
            payload=alter1(payload, self.payload),
            prices=alter1(prices, self.prices),
            provider_token=alter1(provider_token, self.provider_token),
            title=alter1(title, self.title),
            is_flexible=alter1(is_flexible, self.is_flexible),
            max_tip_amount=alter1(max_tip_amount, self.max_tip_amount),
            need_email=alter1(need_email, self.need_email),
            need_name=alter1(need_name, self.need_name),
            need_phone_number=alter1(need_phone_number, self.need_phone_number),
            need_shipping_address=alter1(
                need_shipping_address, self.need_shipping_address
            ),
            photo_height=alter1(photo_height, self.photo_height),
            photo_size=alter1(photo_size, self.photo_size),
            photo_url=alter1(photo_url, self.photo_url),
            photo_width=alter1(photo_width, self.photo_width),
            provider_data=alter1(provider_data, self.provider_data),
            send_email_to_provider=alter1(
                send_email_to_provider, self.send_email_to_provider
            ),
            send_phone_number_to_provider=alter1(
                send_phone_number_to_provider, self.send_phone_number_to_provider
            ),
            suggested_tip_amounts=alter1(
                suggested_tip_amounts, self.suggested_tip_amounts
            ),
        )


@model
class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query.
    Telegram docs: https://core.telegram.org/bots/api#inputlocationmessagecontent"""

    heading: int
    """ Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. """
    horizontal_accuracy: float
    """ Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    latitude: float
    """ Latitude of the location in degrees """
    live_period: int
    """ Optional. Period in seconds for which the location can be updated, should be between 60 and 86400. """
    longitude: float
    """ Longitude of the location in degrees """
    proximity_alert_radius: int
    """ Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. """

    def alter(
        self,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        heading: Omittable[Alterer1[int]] = OMIT,
        horizontal_accuracy: Omittable[Alterer1[float]] = OMIT,
        live_period: Omittable[Alterer1[int]] = OMIT,
        proximity_alert_radius: Omittable[Alterer1[int]] = OMIT,
    ) -> InputLocationMessageContent:
        return InputLocationMessageContent(
            latitude=alter1(latitude, self.latitude),
            longitude=alter1(longitude, self.longitude),
            heading=alter1(heading, self.heading),
            horizontal_accuracy=alter1(horizontal_accuracy, self.horizontal_accuracy),
            live_period=alter1(live_period, self.live_period),
            proximity_alert_radius=alter1(
                proximity_alert_radius, self.proximity_alert_radius
            ),
        )


@model
class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query.
    Telegram docs: https://core.telegram.org/bots/api#inputtextmessagecontent"""

    entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in message text, which can be specified instead of parse_mode """
    link_preview_options: _link_preview_options.LinkPreviewOptions
    """ Optional. Link preview generation options for the message """
    message_text: str
    """ Text of the message to be sent, 1-4096 characters """
    parse_mode: str
    """ Optional. Mode for parsing entities in the message text. See formatting options for more details. """

    def alter(
        self,
        message_text: Omittable[Alterer1[str]] = OMIT,
        entities: Omittable[Alterer1[list[_message_entity.MessageEntity]]] = OMIT,
        link_preview_options: Omittable[
            Alterer1[_link_preview_options.LinkPreviewOptions]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
    ) -> InputTextMessageContent:
        return InputTextMessageContent(
            message_text=alter1(message_text, self.message_text),
            entities=alter1(entities, self.entities),
            link_preview_options=alter1(
                link_preview_options, self.link_preview_options
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
        )


@model
class InputVenueMessageContent:
    """Represents the content of a venue message to be sent as the result of an inline query.
    Telegram docs: https://core.telegram.org/bots/api#inputvenuemessagecontent"""

    address: str
    """ Address of the venue """
    foursquare_id: str
    """ Optional. Foursquare identifier of the venue, if known """
    foursquare_type: str
    """ Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str
    """ Optional. Google Places identifier of the venue """
    google_place_type: str
    """ Optional. Google Places type of the venue. (See supported types.) """
    latitude: float
    """ Latitude of the venue in degrees """
    longitude: float
    """ Longitude of the venue in degrees """
    title: str
    """ Name of the venue """

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        foursquare_id: Omittable[Alterer1[str]] = OMIT,
        foursquare_type: Omittable[Alterer1[str]] = OMIT,
        google_place_id: Omittable[Alterer1[str]] = OMIT,
        google_place_type: Omittable[Alterer1[str]] = OMIT,
    ) -> InputVenueMessageContent:
        return InputVenueMessageContent(
            address=alter1(address, self.address),
            latitude=alter1(latitude, self.latitude),
            longitude=alter1(longitude, self.longitude),
            title=alter1(title, self.title),
            foursquare_id=alter1(foursquare_id, self.foursquare_id),
            foursquare_type=alter1(foursquare_type, self.foursquare_type),
            google_place_id=alter1(google_place_id, self.google_place_id),
            google_place_type=alter1(google_place_type, self.google_place_type),
        )


InputMessageContent: TypeAlias = (
    InputTextMessageContent
    | InputLocationMessageContent
    | InputVenueMessageContent
    | InputContactMessageContent
    | InputInvoiceMessageContent
)
__all__ = [
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "InputMessageContent",
]
