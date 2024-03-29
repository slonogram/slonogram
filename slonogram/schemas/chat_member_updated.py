"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    chat as _chat,
    user as _user,
    chat_member as _chat_member,
    chat_invite_link as _chat_invite_link,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatMemberUpdated:
    """This object represents changes in the status of a chat member.
    Telegram documentation:
    https://core.telegram.org/bots/api#chatmemberupdated"""

    chat: _chat.Chat
    """Chat the user belongs to"""
    date: int
    """Date the change was done in Unix time"""
    from_: _user.User
    """Performer of the action, which resulted in the change"""
    new_chat_member: _chat_member.ChatMember
    """New information about the chat member"""
    old_chat_member: _chat_member.ChatMember
    """Previous information about the chat member"""
    invite_link: _chat_invite_link.ChatInviteLink | None = None
    """Optional. Chat invite link, which was used by the user to join the
    chat; for joining by invite link events only."""
    via_chat_folder_invite_link: bool | None = None
    """Optional. True, if the user joined the chat via a chat folder invite
    link"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        new_chat_member: Omittable[Alterer1[_chat_member.ChatMember]] = OMIT,
        old_chat_member: Omittable[Alterer1[_chat_member.ChatMember]] = OMIT,
        invite_link: Omittable[
            Alterer1[_chat_invite_link.ChatInviteLink | None]
        ] = OMIT,
        via_chat_folder_invite_link: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> ChatMemberUpdated:
        return ChatMemberUpdated(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            from_=alter1(from_, self.from_),
            new_chat_member=alter1(new_chat_member, self.new_chat_member),
            old_chat_member=alter1(old_chat_member, self.old_chat_member),
            invite_link=alter1(invite_link, self.invite_link),
            via_chat_folder_invite_link=alter1(
                via_chat_folder_invite_link, self.via_chat_folder_invite_link
            ),
        )


__all__ = ["ChatMemberUpdated"]
