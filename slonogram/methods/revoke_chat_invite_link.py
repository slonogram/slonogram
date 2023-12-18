# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class RevokeChatInviteLink:
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""

    chat_id: int | str
    """Unique identifier of the target chat or username of the target channel (in the format @channelusername) """
    invite_link: str
    """The invite link to revoke """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["RevokeChatInviteLink"]
