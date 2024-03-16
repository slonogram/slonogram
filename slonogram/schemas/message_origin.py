from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat, user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class MessageOriginChannel:
    author_signature: str
    """ Optional. Signature of the original post author """
    chat: _chat.Chat
    """ Channel chat to which the message was originally sent """
    date: int
    """ Date the message was sent originally in Unix time """
    message_id: int
    """ Unique message identifier inside the chat """
    type: str
    """ Type of the message origin, always "channel" """

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        author_signature: Omittable[Alterer1[str]] = OMIT,
    ):
        return MessageOriginChannel(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            type=alter1(type, self.type),
            author_signature=alter1(author_signature, self.author_signature),
        )


@model
class MessageOriginChat:
    author_signature: str
    """ Optional. For messages originally sent by an anonymous chat administrator, original message author signature """
    date: int
    """ Date the message was sent originally in Unix time """
    sender_chat: _chat.Chat
    """ Chat that sent the message originally """
    type: str
    """ Type of the message origin, always "chat" """

    def alter(
        self,
        date: Omittable[Alterer1[int]] = OMIT,
        sender_chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        author_signature: Omittable[Alterer1[str]] = OMIT,
    ):
        return MessageOriginChat(
            date=alter1(date, self.date),
            sender_chat=alter1(sender_chat, self.sender_chat),
            type=alter1(type, self.type),
            author_signature=alter1(author_signature, self.author_signature),
        )


@model
class MessageOriginHiddenUser:
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
    ):
        return MessageOriginHiddenUser(
            date=alter1(date, self.date),
            sender_user_name=alter1(sender_user_name, self.sender_user_name),
            type=alter1(type, self.type),
        )


@model
class MessageOriginUser:
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
    ):
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
__all__ = [
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
    "MessageOrigin",
]
