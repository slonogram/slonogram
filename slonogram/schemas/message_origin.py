from __future__ import annotations
from slonogram.schemas import chat as _chat, user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model
from typing import TypeAlias


@model
class MessageOriginChannel:
    """The message was originally sent to a channel chat.

    Telegram documentation: https://core.telegram.org/bots/api#messageoriginchannel"""

    chat: _chat.Chat
    """ Channel chat to which the message was originally sent """
    date: int
    """ Date the message was sent originally in Unix time """
    message_id: int
    """ Unique message identifier inside the chat """
    type: str
    """ Type of the message origin, always "channel" """
    author_signature: str | None = None
    """ Optional. Signature of the original post author """

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        author_signature: Omittable[Alterer1[str | None]] = OMIT,
    ) -> MessageOriginChannel:
        return MessageOriginChannel(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            type=alter1(type, self.type),
            author_signature=alter1(author_signature, self.author_signature),
        )


@model
class MessageOriginChat:
    """The message was originally sent on behalf of a chat to a group chat.

    Telegram documentation: https://core.telegram.org/bots/api#messageoriginchat"""

    date: int
    """ Date the message was sent originally in Unix time """
    sender_chat: _chat.Chat
    """ Chat that sent the message originally """
    type: str
    """ Type of the message origin, always "chat" """
    author_signature: str | None = None
    """ Optional. For messages originally sent by an anonymous chat administrator, original message author signature """

    def alter(
        self,
        date: Omittable[Alterer1[int]] = OMIT,
        sender_chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        author_signature: Omittable[Alterer1[str | None]] = OMIT,
    ) -> MessageOriginChat:
        return MessageOriginChat(
            date=alter1(date, self.date),
            sender_chat=alter1(sender_chat, self.sender_chat),
            type=alter1(type, self.type),
            author_signature=alter1(author_signature, self.author_signature),
        )


@model
class MessageOriginHiddenUser:
    """The message was originally sent by an unknown user.

    Telegram documentation: https://core.telegram.org/bots/api#messageoriginhiddenuser"""

    date: int
    """ Date the message was sent originally in Unix time """
    sender_user_name: str
    """ Name of the user that sent the message originally """
    type: str
    """ Type of the message origin, always "hidden_user" """

    def alter(
        self,
        date: Omittable[Alterer1[int]] = OMIT,
        sender_user_name: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> MessageOriginHiddenUser:
        return MessageOriginHiddenUser(
            date=alter1(date, self.date),
            sender_user_name=alter1(sender_user_name, self.sender_user_name),
            type=alter1(type, self.type),
        )


@model
class MessageOriginUser:
    """The message was originally sent by a known user.

    Telegram documentation: https://core.telegram.org/bots/api#messageoriginuser"""

    date: int
    """ Date the message was sent originally in Unix time """
    sender_user: _user.User
    """ User that sent the message originally """
    type: str
    """ Type of the message origin, always "user" """

    def alter(
        self,
        date: Omittable[Alterer1[int]] = OMIT,
        sender_user: Omittable[Alterer1[_user.User]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> MessageOriginUser:
        return MessageOriginUser(
            date=alter1(date, self.date),
            sender_user=alter1(sender_user, self.sender_user),
            type=alter1(type, self.type),
        )


MessageOrigin: TypeAlias = (
    MessageOriginUser
    | MessageOriginHiddenUser
    | MessageOriginChat
    | MessageOriginChannel
)
""" This object describes the origin of a message. It can be one of
- MessageOriginUser
- MessageOriginHiddenUser
- MessageOriginChat
- MessageOriginChannel

Telegram documentation: https://core.telegram.org/bots/api#messageorigin """
__all__ = [
    "MessageOrigin",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
]
