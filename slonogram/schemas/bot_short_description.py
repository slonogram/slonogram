from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class BotShortDescription:
    """This object represents the bot's short description.

    Telegram documentation: https://core.telegram.org/bots/api#botshortdescription"""

    short_description: str
    """ The bot's short description """

    def alter(
        self, short_description: Omittable[Alterer1[str]] = OMIT
    ) -> BotShortDescription:
        return BotShortDescription(
            short_description=alter1(short_description, self.short_description),
        )


__all__ = ["BotShortDescription"]
