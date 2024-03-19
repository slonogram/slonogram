"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import user as _user, shipping_address as _shipping_address
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ShippingQuery:
    """This object contains information about an incoming shipping query.
    Telegram documentation:
    https://core.telegram.org/bots/api#shippingquery"""

    from_: _user.User
    """User who sent the query"""
    id: str
    """Unique query identifier"""
    invoice_payload: str
    """Bot specified invoice payload"""
    shipping_address: _shipping_address.ShippingAddress
    """User specified shipping address"""

    def alter(
        self,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        invoice_payload: Omittable[Alterer1[str]] = OMIT,
        shipping_address: Omittable[Alterer1[_shipping_address.ShippingAddress]] = OMIT,
    ) -> ShippingQuery:
        return ShippingQuery(
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            invoice_payload=alter1(invoice_payload, self.invoice_payload),
            shipping_address=alter1(shipping_address, self.shipping_address),
        )


__all__ = ["ShippingQuery"]
