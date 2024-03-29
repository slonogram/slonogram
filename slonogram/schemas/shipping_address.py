"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ShippingAddress:
    """This object represents a shipping address.  Telegram documentation:
    https://core.telegram.org/bots/api#shippingaddress"""

    city: str
    """City"""
    country_code: str
    """Two-letter ISO 3166-1 alpha-2 country code"""
    post_code: str
    """Address post code"""
    state: str
    """State, if applicable"""
    street_line1: str
    """First line for the address"""
    street_line2: str
    """Second line for the address"""

    def alter(
        self,
        city: Omittable[Alterer1[str]] = OMIT,
        country_code: Omittable[Alterer1[str]] = OMIT,
        post_code: Omittable[Alterer1[str]] = OMIT,
        state: Omittable[Alterer1[str]] = OMIT,
        street_line1: Omittable[Alterer1[str]] = OMIT,
        street_line2: Omittable[Alterer1[str]] = OMIT,
    ) -> ShippingAddress:
        return ShippingAddress(
            city=alter1(city, self.city),
            country_code=alter1(country_code, self.country_code),
            post_code=alter1(post_code, self.post_code),
            state=alter1(state, self.state),
            street_line1=alter1(street_line1, self.street_line1),
            street_line2=alter1(street_line2, self.street_line2),
        )


__all__ = ["ShippingAddress"]
