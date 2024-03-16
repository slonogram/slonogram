from __future__ import annotations
from slonogram._internal.utils import model


@model
class CallbackGame:
    def alter(self):
        return CallbackGame()


__all__ = ["CallbackGame"]
