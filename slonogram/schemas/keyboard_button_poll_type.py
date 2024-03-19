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
class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed.  Telegram
    documentation:
    https://core.telegram.org/bots/api#keyboardbuttonpolltype"""

    type: str | None = None
    """Optional. If quiz is passed, the user will be allowed to create only
    polls in the quiz mode. If regular is passed, only regular polls will
    be allowed. Otherwise, the user will be allowed to create a poll of
    any type."""

    def alter(
        self, type: Omittable[Alterer1[str | None]] = OMIT
    ) -> KeyboardButtonPollType:
        return KeyboardButtonPollType(
            type=alter1(type, self.type),
        )


__all__ = ["KeyboardButtonPollType"]
