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
class GetForumTopicIconStickers:
    """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["GetForumTopicIconStickers"]
