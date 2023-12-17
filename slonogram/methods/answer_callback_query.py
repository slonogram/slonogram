# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 08:56:56.806984
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class AnswerCallbackQuery:
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""

    callback_query_id: str
    """Unique identifier for the query to be answered """
    text: str | None = None
    """Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters """
    show_alert: bool | None = None
    """If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false. """
    url: str | None = None
    """URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback_game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter. """
    cache_time: int | None = None
    """The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["AnswerCallbackQuery"]
