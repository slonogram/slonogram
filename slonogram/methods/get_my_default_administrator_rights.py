# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetMyDefaultAdministratorRights:
    """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""

    for_channels: bool | None = None
    """Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned. """


__all__ = ["GetMyDefaultAdministratorRights"]
