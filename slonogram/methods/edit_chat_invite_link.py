# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditChatInviteLink:
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    invite_link: str
    """The invite link to edit """
    name: str | None = None
    """Invite link name; 0-32 characters """
    expire_date: int | None = None
    """Point in time (Unix timestamp) when the link will expire """
    member_limit: int | None = None
    """The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 """
    creates_join_request: bool | None = None
    """True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditChatInviteLink"]
