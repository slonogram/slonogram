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
class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will
    remove the current custom keyboard and display the default letter-
    keyboard. By default, custom keyboards are displayed until a new
    keyboard is sent by a bot. An exception is made for one-time keyboards
    that are hidden immediately after the user presses a button (see
    ReplyKeyboardMarkup).  Telegram documentation:
    https://core.telegram.org/bots/api#replykeyboardremove"""

    remove_keyboard: bool
    """Requests clients to remove the custom keyboard (user will not be able
    to summon this keyboard; if you want to hide the keyboard from sight
    but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)"""
    selective: bool | None = None
    """Optional. Use this parameter if you want to remove the keyboard for
    specific users only. Targets: 1) users that are @mentioned in the text
    of the Message object; 2) if the bot's message is a reply to a message
    in the same chat and forum topic, sender of the original message.
    Example: A user votes in a poll, bot returns confirmation message in
    reply to the vote and removes the keyboard for that user, while still
    showing the keyboard with poll options to users who haven't voted yet."""

    def alter(
        self,
        remove_keyboard: Omittable[Alterer1[bool]] = OMIT,
        selective: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove(
            remove_keyboard=alter1(remove_keyboard, self.remove_keyboard),
            selective=alter1(selective, self.selective),
        )


__all__ = ["ReplyKeyboardRemove"]
