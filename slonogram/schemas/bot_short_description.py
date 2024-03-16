from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class BotShortDescription:
    """This object represents the bot's short description.
    Telegram docs: https://core.telegram.org/bots/api#botshortdescription"""

    short_description: str
    """ The bot's short description """

    def alter(
        self, short_description: Omittable[Alterer1[str]] = OMIT
    ) -> BotShortDescription:
        return BotShortDescription(
            short_description=alter1(short_description, self.short_description),
        )


__all__ = ["BotShortDescription"]
