from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ChatShared:
    """This object contains information about the chat whose identifier was shared with the bot using a KeyboardButtonRequestChat button.
    Telegram docs: https://core.telegram.org/bots/api#chatshared"""

    chat_id: int
    """ Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means. """
    request_id: int
    """ Identifier of the request """

    def alter(
        self,
        chat_id: Omittable[Alterer1[int]] = OMIT,
        request_id: Omittable[Alterer1[int]] = OMIT,
    ):
        return ChatShared(
            chat_id=alter1(chat_id, self.chat_id),
            request_id=alter1(request_id, self.request_id),
        )


__all__ = ["ChatShared"]
