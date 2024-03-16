from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
    Telegram docs: https://core.telegram.org/bots/api#keyboardbuttonpolltype"""

    type: str
    """ Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type. """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT) -> KeyboardButtonPollType:
        return KeyboardButtonPollType(
            type=alter1(type, self.type),
        )


__all__ = ["KeyboardButtonPollType"]
