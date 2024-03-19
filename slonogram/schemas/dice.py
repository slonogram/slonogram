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
class Dice:
    """This object represents an animated emoji that displays a random value.
    Telegram documentation: https://core.telegram.org/bots/api#dice"""

    emoji: str
    """Emoji on which the dice throw animation is based"""
    value: int
    """Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀"
    and "⚽" base emoji, 1-64 for "🎰" base emoji"""

    def alter(
        self,
        emoji: Omittable[Alterer1[str]] = OMIT,
        value: Omittable[Alterer1[int]] = OMIT,
    ) -> Dice:
        return Dice(
            emoji=alter1(emoji, self.emoji),
            value=alter1(value, self.value),
        )


__all__ = ["Dice"]
