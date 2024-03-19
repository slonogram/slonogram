"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class MessageId:
    """This object represents a unique message identifier.  Telegram
    documentation: https://core.telegram.org/bots/api#messageid"""

    message_id: int
    """Unique message identifier"""

    def alter(self, message_id: Omittable[Alterer1[int]] = OMIT) -> MessageId:
        return MessageId(
            message_id=alter1(message_id, self.message_id),
        )


__all__ = ["MessageId"]
