from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import shipping_address as _shipping_address, user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ShippingQuery:
    """This object contains information about an incoming shipping query.
    Telegram docs: https://core.telegram.org/bots/api#shippingquery"""

    from_: _user.User
    """ User who sent the query """
    id: str
    """ Unique query identifier """
    invoice_payload: str
    """ Bot specified invoice payload """
    shipping_address: _shipping_address.ShippingAddress
    """ User specified shipping address """

    def alter(
        self,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        invoice_payload: Omittable[Alterer1[str]] = OMIT,
        shipping_address: Omittable[Alterer1[_shipping_address.ShippingAddress]] = OMIT,
    ):
        return ShippingQuery(
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            invoice_payload=alter1(invoice_payload, self.invoice_payload),
            shipping_address=alter1(shipping_address, self.shipping_address),
        )


__all__ = ["ShippingQuery"]
