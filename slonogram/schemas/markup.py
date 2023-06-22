from typing import List, Optional
from dataclasses import dataclass

from .web import WebAppInfo, LoginUrl


@dataclass(slots=True)
class SwitchInlineQueryChosenChat:
    query: Optional[str] = None

    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None


@dataclass(slots=True)
class CallbackGame:
    pass


@dataclass(slots=True)
class InlineKeyboardButton:
    text: str
    url: Optional[str] = None

    web_app: Optional[WebAppInfo] = None
    login_url: Optional[LoginUrl] = None

    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    switch_inline_query_chosen_chat: Optional[
        SwitchInlineQueryChosenChat
    ] = None
    callback_game: Optional[CallbackGame] = None
    pay: Optional[bool] = None


@dataclass(slots=True)
class InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]]


__all__ = [
    "InlineKeyboardMarkup",
    "InlineKeyboardButton",
    "CallbackGame",
    "SwitchInlineQueryChosenChat",
]
