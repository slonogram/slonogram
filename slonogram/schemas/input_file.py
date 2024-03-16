from __future__ import annotations
from slonogram._internal.utils import model


@model
class InputFile:
    def alter(self):
        return InputFile()


__all__ = ["InputFile"]
