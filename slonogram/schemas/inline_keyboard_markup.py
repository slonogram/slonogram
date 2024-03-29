"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import inline_keyboard_button as _inline_keyboard_button
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to
    the message it belongs to.  Telegram documentation:
    https://core.telegram.org/bots/api#inlinekeyboardmarkup"""

    inline_keyboard: tuple[
        tuple[_inline_keyboard_button.InlineKeyboardButton, ...], ...
    ]
    """Array of button rows, each represented by an Array of
    InlineKeyboardButton objects"""

    def alter(
        self,
        inline_keyboard: Omittable[
            Alterer1[
                tuple[tuple[_inline_keyboard_button.InlineKeyboardButton, ...], ...]
            ]
        ] = OMIT,
    ) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=alter1(inline_keyboard, self.inline_keyboard),
        )


__all__ = ["InlineKeyboardMarkup"]
