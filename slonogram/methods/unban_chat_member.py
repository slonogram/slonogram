# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class UnbanChatMember:
    """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername) """
    user_id: int
    """Unique identifier of the target user """
    only_if_banned: bool | None = None
    """Do nothing if the user is not banned """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["UnbanChatMember"]
