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
class WebAppInfo:
    """Describes a Web App.  Telegram documentation:
    https://core.telegram.org/bots/api#webappinfo"""

    url: str
    """An HTTPS URL of a Web App to be opened with additional data as
    specified in Initializing Web Apps"""

    def alter(self, url: Omittable[Alterer1[str]] = OMIT) -> WebAppInfo:
        return WebAppInfo(
            url=alter1(url, self.url),
        )


__all__ = ["WebAppInfo"]
