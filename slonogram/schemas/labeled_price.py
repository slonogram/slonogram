from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class LabeledPrice:
    amount: int
    """ Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """
    label: str
    """ Portion label """

    def alter(
        self,
        amount: Omittable[Alterer1[int]] = OMIT,
        label: Omittable[Alterer1[str]] = OMIT,
    ):
        return LabeledPrice(
            amount=alter1(amount, self.amount),
            label=alter1(label, self.label),
        )


__all__ = ["LabeledPrice"]
