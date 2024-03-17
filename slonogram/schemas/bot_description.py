from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class BotDescription:
    """This object represents the bot's description.

    Telegram documentation: https://core.telegram.org/bots/api#botdescription"""

    description: str
    """ The bot's description """

    def alter(self, description: Omittable[Alterer1[str]] = OMIT) -> BotDescription:
        return BotDescription(
            description=alter1(description, self.description),
        )


__all__ = ["BotDescription"]
