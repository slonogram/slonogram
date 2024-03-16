from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import shipping_address as _shipping_address
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class OrderInfo:
    email: str
    """ Optional. User email """
    name: str
    """ Optional. User name """
    phone_number: str
    """ Optional. User's phone number """
    shipping_address: _shipping_address.ShippingAddress
    """ Optional. User shipping address """

    def alter(
        self,
        email: Omittable[Alterer1[str]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        phone_number: Omittable[Alterer1[str]] = OMIT,
        shipping_address: Omittable[Alterer1[_shipping_address.ShippingAddress]] = OMIT,
    ):
        return OrderInfo(
            email=alter1(email, self.email),
            name=alter1(name, self.name),
            phone_number=alter1(phone_number, self.phone_number),
            shipping_address=alter1(shipping_address, self.shipping_address),
        )


__all__ = ["OrderInfo"]
