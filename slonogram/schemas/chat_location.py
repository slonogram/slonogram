"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import location as _location
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatLocation:
    """Represents a location to which a chat is connected.  Telegram
    documentation: https://core.telegram.org/bots/api#chatlocation"""

    address: str
    """Location address; 1-64 characters, as defined by the chat owner"""
    location: _location.Location
    """The location to which the supergroup is connected. Can't be a live
    location."""

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
    ) -> ChatLocation:
        return ChatLocation(
            address=alter1(address, self.address),
            location=alter1(location, self.location),
        )


__all__ = ["ChatLocation"]
