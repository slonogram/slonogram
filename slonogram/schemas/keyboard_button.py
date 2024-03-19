"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    keyboard_button_request_chat as _keyboard_button_request_chat,
    keyboard_button_poll_type as _keyboard_button_poll_type,
    keyboard_button_request_users as _keyboard_button_request_users,
    web_app_info as _web_app_info,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class KeyboardButton:
    """This object represents one button of the reply keyboard. For simple
    text buttons, String can be used instead of this object to specify the
    button text. The optional fields web_app, request_users, request_chat,
    request_contact, request_location, and request_poll are mutually
    exclusive. Note: request_users and request_chat options will only work
    in Telegram versions released after 3 February, 2023. Older clients
    will display unsupported message.  Telegram documentation:
    https://core.telegram.org/bots/api#keyboardbutton"""

    text: str
    """Text of the button. If none of the optional fields are used, it will
    be sent as a message when the button is pressed"""
    request_chat: _keyboard_button_request_chat.KeyboardButtonRequestChat | None = None
    """Optional. If specified, pressing the button will open a list of
    suitable chats. Tapping on a chat will send its identifier to the bot
    in a "chat_shared" service message. Available in private chats only."""
    request_contact: bool | None = None
    """Optional. If True, the user's phone number will be sent as a contact
    when the button is pressed. Available in private chats only."""
    request_location: bool | None = None
    """Optional. If True, the user's current location will be sent when the
    button is pressed. Available in private chats only."""
    request_poll: _keyboard_button_poll_type.KeyboardButtonPollType | None = None
    """Optional. If specified, the user will be asked to create a poll and
    send it to the bot when the button is pressed. Available in private
    chats only."""
    request_users: _keyboard_button_request_users.KeyboardButtonRequestUsers | None = (
        None
    )
    """Optional. If specified, pressing the button will open a list of
    suitable users. Identifiers of selected users will be sent to the bot
    in a "users_shared" service message. Available in private chats only."""
    web_app: _web_app_info.WebAppInfo | None = None
    """Optional. If specified, the described Web App will be launched when
    the button is pressed. The Web App will be able to send a
    "web_app_data" service message. Available in private chats only."""

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        request_chat: Omittable[
            Alterer1[_keyboard_button_request_chat.KeyboardButtonRequestChat | None]
        ] = OMIT,
        request_contact: Omittable[Alterer1[bool | None]] = OMIT,
        request_location: Omittable[Alterer1[bool | None]] = OMIT,
        request_poll: Omittable[
            Alterer1[_keyboard_button_poll_type.KeyboardButtonPollType | None]
        ] = OMIT,
        request_users: Omittable[
            Alterer1[_keyboard_button_request_users.KeyboardButtonRequestUsers | None]
        ] = OMIT,
        web_app: Omittable[Alterer1[_web_app_info.WebAppInfo | None]] = OMIT,
    ) -> KeyboardButton:
        return KeyboardButton(
            text=alter1(text, self.text),
            request_chat=alter1(request_chat, self.request_chat),
            request_contact=alter1(request_contact, self.request_contact),
            request_location=alter1(request_location, self.request_location),
            request_poll=alter1(request_poll, self.request_poll),
            request_users=alter1(request_users, self.request_users),
            web_app=alter1(web_app, self.web_app),
        )


__all__ = ["KeyboardButton"]
