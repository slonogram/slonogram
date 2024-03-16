from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import inline_keyboard_button as _inline_keyboard_button
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class InlineKeyboardMarkup:
    inline_keyboard: list[list[_inline_keyboard_button.InlineKeyboardButton]]
    """ Array of button rows, each represented by an Array of InlineKeyboardButton objects """

    def alter(
        self,
        inline_keyboard: Omittable[
            Alterer1[list[list[_inline_keyboard_button.InlineKeyboardButton]]]
        ] = OMIT,
    ):
        return InlineKeyboardMarkup(
            inline_keyboard=alter1(inline_keyboard, self.inline_keyboard),
        )


__all__ = ["InlineKeyboardMarkup"]
