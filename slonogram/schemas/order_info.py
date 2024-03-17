from __future__ import annotations
from slonogram.schemas import shipping_address as _shipping_address
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class OrderInfo:
    """This object represents information about an order.

    Telegram documentation: https://core.telegram.org/bots/api#orderinfo"""

    email: str | None = None
    """ Optional. User email """
    name: str | None = None
    """ Optional. User name """
    phone_number: str | None = None
    """ Optional. User's phone number """
    shipping_address: _shipping_address.ShippingAddress | None = None
    """ Optional. User shipping address """

    def alter(
        self,
        email: Omittable[Alterer1[str | None]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
        phone_number: Omittable[Alterer1[str | None]] = OMIT,
        shipping_address: Omittable[
            Alterer1[_shipping_address.ShippingAddress | None]
        ] = OMIT,
    ) -> OrderInfo:
        return OrderInfo(
            email=alter1(email, self.email),
            name=alter1(name, self.name),
            phone_number=alter1(phone_number, self.phone_number),
            shipping_address=alter1(shipping_address, self.shipping_address),
        )


__all__ = ["OrderInfo"]
