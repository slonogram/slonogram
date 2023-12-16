# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 17:59:35.955291
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class DeleteWebhook:
    """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""

    drop_pending_updates: bool | None = None
    """Pass True to drop all pending updates """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["DeleteWebhook"]
