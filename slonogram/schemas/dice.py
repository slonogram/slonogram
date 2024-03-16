from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Dice:
    emoji: str
    """ Emoji on which the dice throw animation is based """
    value: int
    """ Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji """

    def alter(
        self,
        emoji: Omittable[Alterer1[str]] = OMIT,
        value: Omittable[Alterer1[int]] = OMIT,
    ):
        return Dice(
            emoji=alter1(emoji, self.emoji),
            value=alter1(value, self.value),
        )


__all__ = ["Dice"]
