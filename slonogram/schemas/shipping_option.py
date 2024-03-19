"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import labeled_price as _labeled_price
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ShippingOption:
    """This object represents one shipping option.  Telegram documentation:
    https://core.telegram.org/bots/api#shippingoption"""

    id: str
    """Shipping option identifier"""
    prices: tuple[_labeled_price.LabeledPrice, ...]
    """List of price portions"""
    title: str
    """Option title"""

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        prices: Omittable[Alterer1[tuple[_labeled_price.LabeledPrice, ...]]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> ShippingOption:
        return ShippingOption(
            id=alter1(id, self.id),
            prices=alter1(prices, self.prices),
            title=alter1(title, self.title),
        )


__all__ = ["ShippingOption"]
