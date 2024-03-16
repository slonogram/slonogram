from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ChatInviteLink:
    """Represents an invite link for a chat.
    Telegram docs: https://core.telegram.org/bots/api#chatinvitelink"""

    creates_join_request: bool
    """ True, if users joining the chat via the link need to be approved by chat administrators """
    creator: _user.User
    """ Creator of the link """
    expire_date: int
    """ Optional. Point in time (Unix timestamp) when the link will expire or has been expired """
    invite_link: str
    """ The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "...". """
    is_primary: bool
    """ True, if the link is primary """
    is_revoked: bool
    """ True, if the link is revoked """
    member_limit: int
    """ Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 """
    name: str
    """ Optional. Invite link name """
    pending_join_request_count: int
    """ Optional. Number of pending join requests created using this link """

    def alter(
        self,
        creates_join_request: Omittable[Alterer1[bool]] = OMIT,
        creator: Omittable[Alterer1[_user.User]] = OMIT,
        invite_link: Omittable[Alterer1[str]] = OMIT,
        is_primary: Omittable[Alterer1[bool]] = OMIT,
        is_revoked: Omittable[Alterer1[bool]] = OMIT,
        expire_date: Omittable[Alterer1[int]] = OMIT,
        member_limit: Omittable[Alterer1[int]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        pending_join_request_count: Omittable[Alterer1[int]] = OMIT,
    ):
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
