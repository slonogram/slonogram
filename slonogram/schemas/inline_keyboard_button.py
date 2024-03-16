from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    callback_game as _callback_game,
    login_url as _login_url,
    switch_inline_query_chosen_chat as _switch_inline_query_chosen_chat,
    web_app_info as _web_app_info,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class InlineKeyboardButton:
    callback_data: str
    """ Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes """
    callback_game: _callback_game.CallbackGame
    """ Optional. Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row. """
    login_url: _login_url.LoginUrl
    """ Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget. """
    pay: bool
    """ Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages. """
    switch_inline_query: str
    """ Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. """
    switch_inline_query_chosen_chat: _switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat
    """ Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field """
    switch_inline_query_current_chat: str
    """ Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. """
    text: str
    """ Label text on the button """
    url: str
    """ Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings. """
    web_app: _web_app_info.WebAppInfo
    """ Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot. """

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        callback_data: Omittable[Alterer1[str]] = OMIT,
        callback_game: Omittable[Alterer1[_callback_game.CallbackGame]] = OMIT,
        login_url: Omittable[Alterer1[_login_url.LoginUrl]] = OMIT,
        pay: Omittable[Alterer1[bool]] = OMIT,
        switch_inline_query: Omittable[Alterer1[str]] = OMIT,
        switch_inline_query_chosen_chat: Omittable[
            Alterer1[_switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat]
        ] = OMIT,
        switch_inline_query_current_chat: Omittable[Alterer1[str]] = OMIT,
        url: Omittable[Alterer1[str]] = OMIT,
        web_app: Omittable[Alterer1[_web_app_info.WebAppInfo]] = OMIT,
    ):
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
