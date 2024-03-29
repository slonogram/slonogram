"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatInviteLink:
    """Represents an invite link for a chat.  Telegram documentation:
    https://core.telegram.org/bots/api#chatinvitelink"""

    creates_join_request: bool
    """True, if users joining the chat via the link need to be approved by
    chat administrators"""
    creator: _user.User
    """Creator of the link"""
    invite_link: str
    """The invite link. If the link was created by another chat
    administrator, then the second part of the link will be replaced with
    "..."."""
    is_primary: bool
    """True, if the link is primary"""
    is_revoked: bool
    """True, if the link is revoked"""
    expire_date: int | None = None
    """Optional. Point in time (Unix timestamp) when the link will expire or
    has been expired"""
    member_limit: int | None = None
    """Optional. The maximum number of users that can be members of the chat
    simultaneously after joining the chat via this invite link; 1-99999"""
    name: str | None = None
    """Optional. Invite link name"""
    pending_join_request_count: int | None = None
    """Optional. Number of pending join requests created using this link"""

    def alter(
        self,
        creates_join_request: Omittable[Alterer1[bool]] = OMIT,
        creator: Omittable[Alterer1[_user.User]] = OMIT,
        invite_link: Omittable[Alterer1[str]] = OMIT,
        is_primary: Omittable[Alterer1[bool]] = OMIT,
        is_revoked: Omittable[Alterer1[bool]] = OMIT,
        expire_date: Omittable[Alterer1[int | None]] = OMIT,
        member_limit: Omittable[Alterer1[int | None]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
        pending_join_request_count: Omittable[Alterer1[int | None]] = OMIT,
    ) -> ChatInviteLink:
        return ChatInviteLink(
            creates_join_request=alter1(
                creates_join_request, self.creates_join_request
            ),
            creator=alter1(creator, self.creator),
            invite_link=alter1(invite_link, self.invite_link),
            is_primary=alter1(is_primary, self.is_primary),
            is_revoked=alter1(is_revoked, self.is_revoked),
            expire_date=alter1(expire_date, self.expire_date),
            member_limit=alter1(member_limit, self.member_limit),
            name=alter1(name, self.name),
            pending_join_request_count=alter1(
                pending_join_request_count, self.pending_join_request_count
            ),
        )


__all__ = ["ChatInviteLink"]
