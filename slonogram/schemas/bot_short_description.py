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
class BotShortDescription:
    """This object represents the bot's short description.  Telegram
    documentation: https://core.telegram.org/bots/api#botshortdescription"""

    short_description: str
    """The bot's short description"""

    def alter(
        self, short_description: Omittable[Alterer1[str]] = OMIT
    ) -> BotShortDescription:
        return BotShortDescription(
            short_description=alter1(short_description, self.short_description),
        )


__all__ = ["BotShortDescription"]
