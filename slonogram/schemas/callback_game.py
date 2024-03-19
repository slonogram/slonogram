"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up
    your game.  Telegram documentation:
    https://core.telegram.org/bots/api#callbackgame"""

    def alter(self) -> CallbackGame:
        return CallbackGame()


__all__ = ["CallbackGame"]
