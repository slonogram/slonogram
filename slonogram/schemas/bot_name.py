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
class BotName:
    """This object represents the bot's name.  Telegram documentation:
    https://core.telegram.org/bots/api#botname"""

    name: str
    """The bot's name"""

    def alter(self, name: Omittable[Alterer1[str]] = OMIT) -> BotName:
        return BotName(
            name=alter1(name, self.name),
        )


__all__ = ["BotName"]
