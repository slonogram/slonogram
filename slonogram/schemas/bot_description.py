from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class BotDescription:
    """This object represents the bot's description.
    Telegram docs: https://core.telegram.org/bots/api#botdescription"""

    description: str
    """ The bot's description """

    def alter(self, description: Omittable[Alterer1[str]] = OMIT):
        return BotDescription(
            description=alter1(description, self.description),
        )


__all__ = ["BotDescription"]