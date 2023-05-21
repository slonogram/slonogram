from typing import List, Optional
from dataclasses import dataclass

from .web import WebAppInfo, LoginUrl
from .query import SwitchInlineQueryChosenChat, CallbackGame


@dataclass
class InlineKeyboardButton:
    text: str
    url: str

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


class InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]]
