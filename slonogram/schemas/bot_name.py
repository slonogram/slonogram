from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class BotName:
    """This object represents the bot's name.

    Telegram documentation: https://core.telegram.org/bots/api#botname"""

    name: str
    """ The bot's name """

    def alter(self, name: Omittable[Alterer1[str]] = OMIT) -> BotName:
        return BotName(
            name=alter1(name, self.name),
        )


__all__ = ["BotName"]
