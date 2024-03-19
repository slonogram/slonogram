"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class InputFile:
    """This object represents the contents of a file to be uploaded. Must be
    posted using multipart/form-data in the usual way that files are
    uploaded via the browser.  Telegram documentation:
    https://core.telegram.org/bots/api#inputfile"""

    def alter(self) -> InputFile:
        return InputFile()


__all__ = ["InputFile"]
