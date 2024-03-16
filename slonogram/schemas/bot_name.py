from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class BotName:
    name: str
    """ The bot's name """

    def alter(self, name: Omittable[Alterer1[str]] = OMIT):
        return BotName(
            name=alter1(name, self.name),
        )


__all__ = ["BotName"]
