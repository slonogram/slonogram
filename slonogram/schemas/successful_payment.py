"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import order_info as _order_info
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class SuccessfulPayment:
    """This object contains basic information about a successful payment.
    Telegram documentation:
    https://core.telegram.org/bots/api#successfulpayment"""

    currency: str
    """Three-letter ISO 4217 currency code"""
    invoice_payload: str
    """Bot specified invoice payload"""
    provider_payment_charge_id: str
    """Provider payment identifier"""
    telegram_payment_charge_id: str
    """Telegram payment identifier"""
    total_amount: int
    """Total price in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145.
    See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""
    order_info: _order_info.OrderInfo | None = None
    """Optional. Order information provided by the user"""
    shipping_option_id: str | None = None
    """Optional. Identifier of the shipping option chosen by the user"""

    def alter(
        self,
        currency: Omittable[Alterer1[str]] = OMIT,
        invoice_payload: Omittable[Alterer1[str]] = OMIT,
        provider_payment_charge_id: Omittable[Alterer1[str]] = OMIT,
        telegram_payment_charge_id: Omittable[Alterer1[str]] = OMIT,
        total_amount: Omittable[Alterer1[int]] = OMIT,
        order_info: Omittable[Alterer1[_order_info.OrderInfo | None]] = OMIT,
        shipping_option_id: Omittable[Alterer1[str | None]] = OMIT,
    ) -> SuccessfulPayment:
        return SuccessfulPayment(
            currency=alter1(currency, self.currency),
            invoice_payload=alter1(invoice_payload, self.invoice_payload),
            provider_payment_charge_id=alter1(
                provider_payment_charge_id, self.provider_payment_charge_id
            ),
            telegram_payment_charge_id=alter1(
                telegram_payment_charge_id, self.telegram_payment_charge_id
            ),
            total_amount=alter1(total_amount, self.total_amount),
            order_info=alter1(order_info, self.order_info),
            shipping_option_id=alter1(shipping_option_id, self.shipping_option_id),
        )


__all__ = ["SuccessfulPayment"]
