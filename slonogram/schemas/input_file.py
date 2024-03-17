from __future__ import annotations
from slonogram._internal.utils import model


@model
class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    Telegram documentation: https://core.telegram.org/bots/api#inputfile"""

    def alter(self) -> InputFile:
        return InputFile()


__all__ = ["InputFile"]
