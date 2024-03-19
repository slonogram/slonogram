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
class LabeledPrice:
    """This object represents a portion of the price for goods or services.
    Telegram documentation:
    https://core.telegram.org/bots/api#labeledprice"""

    amount: int
    """Price of the product in the smallest units of the currency (integer,
    not float/double). For example, for a price of US$ 1.45 pass amount =
    145. See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""
    label: str
    """Portion label"""

    def alter(
        self,
        amount: Omittable[Alterer1[int]] = OMIT,
        label: Omittable[Alterer1[str]] = OMIT,
    ) -> LabeledPrice:
        return LabeledPrice(
            amount=alter1(amount, self.amount),
            label=alter1(label, self.label),
        )


__all__ = ["LabeledPrice"]
