# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 15:06:50.427429
from dataclasses import dataclass
from slonogram.schemas import InlineQueryResult
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class AnswerWebAppQuery:
    """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""

    web_app_query_id: str
    """Unique identifier for the query to be answered """
    result: InlineQueryResult
    """A JSON-serialized object describing the message to be sent """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["AnswerWebAppQuery"]
