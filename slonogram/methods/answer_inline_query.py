# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from slonogram.schemas import InlineQueryResult, InlineQueryResultsButton
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class AnswerInlineQuery:
    """Use this method to send answers to an inline query. On success, True is returned.
    No more than 50 results per query are allowed."""

    inline_query_id: str
    """Unique identifier for the answered query """
    results: list[InlineQueryResult]
    """A JSON-serialized array of results for the inline query """
    cache_time: int | None = None
    """The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. """
    is_personal: bool | None = None
    """Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query. """
    next_offset: str | None = None
    """Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes. """
    button: InlineQueryResultsButton | None = None
    """A JSON-serialized object describing a button to be shown above inline query results """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["AnswerInlineQuery"]
