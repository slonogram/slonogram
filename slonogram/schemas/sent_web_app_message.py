from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class SentWebAppMessage:
    """Describes an inline message sent by a Web App on behalf of a user.
    Telegram docs: https://core.telegram.org/bots/api#sentwebappmessage"""

    inline_message_id: str
    """ Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. """

    def alter(self, inline_message_id: Omittable[Alterer1[str]] = OMIT):
        return SentWebAppMessage(
            inline_message_id=alter1(inline_message_id, self.inline_message_id),
        )


__all__ = ["SentWebAppMessage"]
