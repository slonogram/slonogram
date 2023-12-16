# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import ChatAdministratorRights


@dataclass(frozen=False, slots=True)
class SetMyDefaultAdministratorRights:
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success."""

    rights: ChatAdministratorRights | None = None
    """A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared. """
    for_channels: bool | None = None
    """Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed. """


__all__ = ["SetMyDefaultAdministratorRights"]