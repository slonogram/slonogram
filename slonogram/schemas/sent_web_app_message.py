from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class SentWebAppMessage:
    """Describes an inline message sent by a Web App on behalf of a user.

    Telegram documentation: https://core.telegram.org/bots/api#sentwebappmessage"""

    inline_message_id: str | None = None
    """ Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. """

    def alter(
        self, inline_message_id: Omittable[Alterer1[str | None]] = OMIT
    ) -> SentWebAppMessage:
        return SentWebAppMessage(
            inline_message_id=alter1(inline_message_id, self.inline_message_id),
        )


__all__ = ["SentWebAppMessage"]
