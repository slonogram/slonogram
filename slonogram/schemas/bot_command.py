from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class BotCommand:
    command: str
    """ Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores. """
    description: str
    """ Description of the command; 1-256 characters. """

    def alter(
        self,
        command: Omittable[Alterer1[str]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
    ):
        return BotCommand(
            command=alter1(command, self.command),
            description=alter1(description, self.description),
        )


__all__ = ["BotCommand"]
