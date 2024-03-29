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
class WebAppData:
    """Describes data sent from a Web App to the bot.  Telegram
    documentation: https://core.telegram.org/bots/api#webappdata"""

    button_text: str
    """Text of the web_app keyboard button from which the Web App was opened.
    Be aware that a bad client can send arbitrary data in this field."""
    data: str
    """The data. Be aware that a bad client can send arbitrary data in this
    field."""

    def alter(
        self,
        button_text: Omittable[Alterer1[str]] = OMIT,
        data: Omittable[Alterer1[str]] = OMIT,
    ) -> WebAppData:
        return WebAppData(
            button_text=alter1(button_text, self.button_text),
            data=alter1(data, self.data),
        )


__all__ = ["WebAppData"]
