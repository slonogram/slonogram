from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import location as _location, user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class InlineQuery:
    chat_type: str
    """ Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat """
    from_: _user.User
    """ Sender """
    id: str
    """ Unique identifier for this query """
    location: _location.Location
    """ Optional. Sender location, only for bots that request user location """
    offset: str
    """ Offset of the results to be returned, can be controlled by the bot """
    query: str
    """ Text of the query (up to 256 characters) """

    def alter(
        self,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        offset: Omittable[Alterer1[str]] = OMIT,
        query: Omittable[Alterer1[str]] = OMIT,
        chat_type: Omittable[Alterer1[str]] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
    ):
        return InlineQuery(
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            offset=alter1(offset, self.offset),
            query=alter1(query, self.query),
            chat_type=alter1(chat_type, self.chat_type),
            location=alter1(location, self.location),
        )


__all__ = ["InlineQuery"]
