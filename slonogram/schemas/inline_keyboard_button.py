"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    callback_game as _callback_game,
    login_url as _login_url,
    switch_inline_query_chosen_chat as _switch_inline_query_chosen_chat,
    web_app_info as _web_app_info,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use
    exactly one of the optional fields.  Telegram documentation:
    https://core.telegram.org/bots/api#inlinekeyboardbutton"""

    text: str
    """Label text on the button"""
    callback_data: str | None = None
    """Optional. Data to be sent in a callback query to the bot when button
    is pressed, 1-64 bytes"""
    callback_game: _callback_game.CallbackGame | None = None
    """Optional. Description of the game that will be launched when the user
    presses the button. NOTE: This type of button must always be the first
    button in the first row."""
    login_url: _login_url.LoginUrl | None = None
    """Optional. An HTTPS URL used to automatically authorize the user. Can
    be used as a replacement for the Telegram Login Widget."""
    pay: bool | None = None
    """Optional. Specify True, to send a Pay button. NOTE: This type of
    button must always be the first button in the first row and can only
    be used in invoice messages."""
    switch_inline_query: str | None = None
    """Optional. If set, pressing the button will prompt the user to select
    one of their chats, open that chat and insert the bot's username and
    the specified inline query in the input field. May be empty, in which
    case just the bot's username will be inserted."""
    switch_inline_query_chosen_chat: _switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat | None = None
    """Optional. If set, pressing the button will prompt the user to select
    one of their chats of the specified type, open that chat and insert
    the bot's username and the specified inline query in the input field"""
    switch_inline_query_current_chat: str | None = None
    """Optional. If set, pressing the button will insert the bot's username
    and the specified inline query in the current chat's input field. May
    be empty, in which case only the bot's username will be inserted. This
    offers a quick way for the user to open your bot in inline mode in the
    same chat - good for selecting something from multiple options."""
    url: str | None = None
    """Optional. HTTP or tg:// URL to be opened when the button is pressed.
    Links tg://user?id=<user_id> can be used to mention a user by their
    identifier without using a username, if this is allowed by their
    privacy settings."""
    web_app: _web_app_info.WebAppInfo | None = None
    """Optional. Description of the Web App that will be launched when the
    user presses the button. The Web App will be able to send an arbitrary
    message on behalf of the user using the method answerWebAppQuery.
    Available only in private chats between a user and the bot."""

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        callback_data: Omittable[Alterer1[str | None]] = OMIT,
        callback_game: Omittable[Alterer1[_callback_game.CallbackGame | None]] = OMIT,
        login_url: Omittable[Alterer1[_login_url.LoginUrl | None]] = OMIT,
        pay: Omittable[Alterer1[bool | None]] = OMIT,
        switch_inline_query: Omittable[Alterer1[str | None]] = OMIT,
        switch_inline_query_chosen_chat: Omittable[
            Alterer1[
                _switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat | None
            ]
        ] = OMIT,
        switch_inline_query_current_chat: Omittable[Alterer1[str | None]] = OMIT,
        url: Omittable[Alterer1[str | None]] = OMIT,
        web_app: Omittable[Alterer1[_web_app_info.WebAppInfo | None]] = OMIT,
    ) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=alter1(text, self.text),
            callback_data=alter1(callback_data, self.callback_data),
            callback_game=alter1(callback_game, self.callback_game),
            login_url=alter1(login_url, self.login_url),
            pay=alter1(pay, self.pay),
            switch_inline_query=alter1(switch_inline_query, self.switch_inline_query),
            switch_inline_query_chosen_chat=alter1(
                switch_inline_query_chosen_chat, self.switch_inline_query_chosen_chat
            ),
            switch_inline_query_current_chat=alter1(
                switch_inline_query_current_chat, self.switch_inline_query_current_chat
            ),
            url=alter1(url, self.url),
            web_app=alter1(web_app, self.web_app),
        )


__all__ = ["InlineKeyboardButton"]
