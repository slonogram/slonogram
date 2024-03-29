"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    chat as _chat,
    user as _user,
    chat_invite_link as _chat_invite_link,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatJoinRequest:
    """Represents a join request sent to a chat.  Telegram documentation:
    https://core.telegram.org/bots/api#chatjoinrequest"""

    chat: _chat.Chat
    """Chat to which the request was sent"""
    date: int
    """Date the request was sent in Unix time"""
    from_: _user.User
    """User that sent the join request"""
    user_chat_id: int
    """Identifier of a private chat with the user who sent the join request.
    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier. The bot can use this identifier for 5 minutes to send
    messages until the join request is processed, assuming no other
    administrator contacted the user."""
    bio: str | None = None
    """Optional. Bio of the user."""
    invite_link: _chat_invite_link.ChatInviteLink | None = None
    """Optional. Chat invite link that was used by the user to send the join
    request"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        user_chat_id: Omittable[Alterer1[int]] = OMIT,
        bio: Omittable[Alterer1[str | None]] = OMIT,
        invite_link: Omittable[
            Alterer1[_chat_invite_link.ChatInviteLink | None]
        ] = OMIT,
    ) -> ChatJoinRequest:
        return ChatJoinRequest(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            from_=alter1(from_, self.from_),
            user_chat_id=alter1(user_chat_id, self.user_chat_id),
            bio=alter1(bio, self.bio),
            invite_link=alter1(invite_link, self.invite_link),
        )


__all__ = ["ChatJoinRequest"]
