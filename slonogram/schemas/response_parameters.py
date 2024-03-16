from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ResponseParameters:
    """Describes why a request was unsuccessful.
    Telegram docs: https://core.telegram.org/bots/api#responseparameters"""

    migrate_to_chat_id: int
    """ Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    retry_after: int
    """ Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated """

    def alter(
        self,
        migrate_to_chat_id: Omittable[Alterer1[int]] = OMIT,
        retry_after: Omittable[Alterer1[int]] = OMIT,
    ) -> ResponseParameters:
        return ResponseParameters(
            migrate_to_chat_id=alter1(migrate_to_chat_id, self.migrate_to_chat_id),
            retry_after=alter1(retry_after, self.retry_after),
        )


__all__ = ["ResponseParameters"]
