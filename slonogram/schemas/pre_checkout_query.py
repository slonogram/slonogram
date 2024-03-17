from __future__ import annotations
from slonogram.schemas import user as _user, order_info as _order_info
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query.

    Telegram documentation: https://core.telegram.org/bots/api#precheckoutquery"""

    currency: str
    """ Three-letter ISO 4217 currency code """
    from_: _user.User
    """ User who sent the query """
    id: str
    """ Unique query identifier """
    invoice_payload: str
    """ Bot specified invoice payload """
    total_amount: int
    """ Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """
    order_info: _order_info.OrderInfo | None = None
    """ Optional. Order information provided by the user """
    shipping_option_id: str | None = None
    """ Optional. Identifier of the shipping option chosen by the user """

    def alter(
        self,
        currency: Omittable[Alterer1[str]] = OMIT,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        invoice_payload: Omittable[Alterer1[str]] = OMIT,
        total_amount: Omittable[Alterer1[int]] = OMIT,
        order_info: Omittable[Alterer1[_order_info.OrderInfo | None]] = OMIT,
        shipping_option_id: Omittable[Alterer1[str | None]] = OMIT,
    ) -> PreCheckoutQuery:
        return PreCheckoutQuery(
            currency=alter1(currency, self.currency),
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            invoice_payload=alter1(invoice_payload, self.invoice_payload),
            total_amount=alter1(total_amount, self.total_amount),
            order_info=alter1(order_info, self.order_info),
            shipping_option_id=alter1(shipping_option_id, self.shipping_option_id),
        )


__all__ = ["PreCheckoutQuery"]
