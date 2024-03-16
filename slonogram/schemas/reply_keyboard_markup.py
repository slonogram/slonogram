from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import keyboard_button as _keyboard_button
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
    Telegram docs: https://core.telegram.org/bots/api#replykeyboardmarkup"""

    input_field_placeholder: str
    """ Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters """
    is_persistent: bool
    """ Optional. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to false, in which case the custom keyboard can be hidden and opened with a keyboard icon. """
    keyboard: list[list[_keyboard_button.KeyboardButton]]
    """ Array of button rows, each represented by an Array of KeyboardButton objects """
    one_time_keyboard: bool
    """ Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false. """
    resize_keyboard: bool
    """ Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard. """
    selective: bool
    """ Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard. """

    def alter(
        self,
        keyboard: Omittable[
            Alterer1[list[list[_keyboard_button.KeyboardButton]]]
        ] = OMIT,
        input_field_placeholder: Omittable[Alterer1[str]] = OMIT,
        is_persistent: Omittable[Alterer1[bool]] = OMIT,
        one_time_keyboard: Omittable[Alterer1[bool]] = OMIT,
        resize_keyboard: Omittable[Alterer1[bool]] = OMIT,
        selective: Omittable[Alterer1[bool]] = OMIT,
    ) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=alter1(keyboard, self.keyboard),
            input_field_placeholder=alter1(
                input_field_placeholder, self.input_field_placeholder
            ),
            is_persistent=alter1(is_persistent, self.is_persistent),
            one_time_keyboard=alter1(one_time_keyboard, self.one_time_keyboard),
            resize_keyboard=alter1(resize_keyboard, self.resize_keyboard),
            selective=alter1(selective, self.selective),
        )


__all__ = ["ReplyKeyboardMarkup"]
