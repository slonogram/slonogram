# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class CreateChatInviteLink:
    """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    name: str | None = None
    """Invite link name; 0-32 characters """
    expire_date: int | None = None
    """Point in time (Unix timestamp) when the link will expire """
    member_limit: int | None = None
    """The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 """
    creates_join_request: bool | None = None
    """True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified """


__all__ = ["CreateChatInviteLink"]