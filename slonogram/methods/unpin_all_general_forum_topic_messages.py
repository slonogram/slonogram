# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class UnpinAllGeneralForumTopicMessages:
    """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """


__all__ = ["UnpinAllGeneralForumTopicMessages"]
