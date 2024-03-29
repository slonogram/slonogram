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
class BotCommand:
    """This object represents a bot command.  Telegram documentation:
    https://core.telegram.org/bots/api#botcommand"""

    command: str
    """Text of the command; 1-32 characters. Can contain only lowercase
    English letters, digits and underscores."""
    description: str
    """Description of the command; 1-256 characters."""

    def alter(
        self,
        command: Omittable[Alterer1[str]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
    ) -> BotCommand:
        return BotCommand(
            command=alter1(command, self.command),
            description=alter1(description, self.description),
        )


__all__ = ["BotCommand"]
