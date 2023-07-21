from typing import Awaitable, Optional, List  # noqa
import slonogram.schemas  # noqa
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps  # noqa


class QueryCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    async def answer_callback(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from
        inline keyboards. The answer will be displayed to the user as a
        notification at the top of the chat screen or as an alert. On
        success, True is returned. for more:
        https://core.telegram.org/bots/api#answercallbackquery
        :param callback_query_id: Unique identifier for the query to
                                  be answered
        :param text: Text of the notification. If not specified,
                     nothing will be shown to the user, 0-200
                     characters
        :param show_alert: If True, an alert will be shown by the
                           client instead of a notification at the
                           top of the chat screen. Defaults to
                           false.
        :param url: URL that will be opened by the user's client. If
                    you have created a Game and accepted the
                    conditions via @BotFather, specify the URL that
                    opens your game - note that this will only work
                    if the query comes from a callback_game button.
                    Otherwise, you may use links like
                    t.me/your_bot?start=XXXX that open your bot with
                    a parameter.
        :param cache_time: The maximum amount of time in seconds
                           that the result of the callback query may
                           be cached client-side. Telegram apps will
                           support caching starting in version 3.14.
                           Defaults to 0.
        :return: See link mentioned above for more information
        """
        params: dict = {"callback_query_id": callback_query_id}
        if text is not None:
            params["text"] = text

        if show_alert is not None:
            params["show_alert"] = show_alert

        if url is not None:
            params["url"] = url

        if cache_time is not None:
            params["cache_time"] = cache_time

        return await self._session.call_method(
            bool, "answerCallbackQuery", params
        )
