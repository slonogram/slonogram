# flake8: noqa
from typing import Awaitable, Optional, List, IO
from slonogram import schemas
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps


class QueryCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    def answer_callback(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> Awaitable[bool]:
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

        return self._session.call_method(
            bool, "answerCallbackQuery", params
        )

    def answer_inline(
        self,
        inline_query_id: str,
        results: List[schemas.InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        button: Optional[schemas.InlineQueryResultsButton] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to send answers to an inline query. On success,
        True is returned. No more than 50 results per query are allowed.
        for more: https://core.telegram.org/bots/api#answerinlinequery
        :param inline_query_id: Unique identifier for the answered
                                query
        :param results: A JSON-serialized array of results for the
                        inline query
        :param cache_time: The maximum amount of time in seconds
                           that the result of the inline query may
                           be cached on the server. Defaults to 300.
        :param is_personal: Pass True if results may be cached on
                            the server side only for the user that
                            sent the query. By default, results may
                            be returned to any user who sends the
                            same query.
        :param next_offset: Pass the offset that a client should
                            send in the next query with the same
                            text to receive more results. Pass an
                            empty string if there are no more
                            results or if you don't support
                            pagination. Offset length can't exceed
                            64 bytes.
        :param button: A JSON-serialized object describing a button
                       to be shown above inline query results
        :return: See link mentioned above for more information
        """
        params: dict = {
            "inline_query_id": inline_query_id,
            "results": dumps(self._session.retort.dump(results)),
        }
        if cache_time is not None:
            params["cache_time"] = cache_time

        if is_personal is not None:
            params["is_personal"] = is_personal

        if next_offset is not None:
            params["next_offset"] = next_offset

        if button is not None:
            params["button"] = button

        return self._session.call_method(bool, "answerInlineQuery", params)
