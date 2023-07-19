from .group import CallsGroup
from typing import Awaitable, Optional


class QueriesCallGroup(CallsGroup):
    def answer_callback(
        self,
        query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> Awaitable[bool]:
        return self._call(
            bool,
            "answerCallbackQuery",
            {"query_id": query_id},
            (
                ("text", text),
                ("show_alert", show_alert),
                ("url", url),
                ("cache_time", cache_time),
            ),
        )
