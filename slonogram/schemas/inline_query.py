"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import user as _user, location as _location
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class InlineQuery:
    """This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending
    results.  Telegram documentation:
    https://core.telegram.org/bots/api#inlinequery"""

    from_: _user.User
    """Sender"""
    id: str
    """Unique identifier for this query"""
    offset: str
    """Offset of the results to be returned, can be controlled by the bot"""
    query: str
    """Text of the query (up to 256 characters)"""
    chat_type: str | None = None
    """Optional. Type of the chat from which the inline query was sent. Can
    be either "sender" for a private chat with the inline query sender,
    "private", "group", "supergroup", or "channel". The chat type should
    be always known for requests sent from official clients and most
    third-party clients, unless the request was sent from a secret chat"""
    location: _location.Location | None = None
    """Optional. Sender location, only for bots that request user location"""

    def alter(
        self,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        offset: Omittable[Alterer1[str]] = OMIT,
        query: Omittable[Alterer1[str]] = OMIT,
        chat_type: Omittable[Alterer1[str | None]] = OMIT,
        location: Omittable[Alterer1[_location.Location | None]] = OMIT,
    ) -> InlineQuery:
        return InlineQuery(
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            offset=alter1(offset, self.offset),
            query=alter1(query, self.query),
            chat_type=alter1(chat_type, self.chat_type),
            location=alter1(location, self.location),
        )


__all__ = ["InlineQuery"]
