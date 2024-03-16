from __future__ import annotations
from slonogram._internal.utils import model


@model
class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up your game.
    Telegram docs: https://core.telegram.org/bots/api#callbackgame"""

    def alter(self) -> CallbackGame:
        return CallbackGame()


__all__ = ["CallbackGame"]
