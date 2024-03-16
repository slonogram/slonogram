from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Invoice:
    """This object contains basic information about an invoice.
    Telegram docs: https://core.telegram.org/bots/api#invoice"""

    currency: str
    """ Three-letter ISO 4217 currency code """
    description: str
    """ Product description """
    start_parameter: str
    """ Unique bot deep-linking parameter that can be used to generate this invoice """
    title: str
    """ Product name """
    total_amount: int
    """ Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """

    def alter(
        self,
        currency: Omittable[Alterer1[str]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        start_parameter: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        total_amount: Omittable[Alterer1[int]] = OMIT,
    ):
        return Invoice(
            currency=alter1(currency, self.currency),
            description=alter1(description, self.description),
            start_parameter=alter1(start_parameter, self.start_parameter),
            title=alter1(title, self.title),
            total_amount=alter1(total_amount, self.total_amount),
        )


__all__ = ["Invoice"]
