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
class GetMyName:
    """Use this method to get the current bot name for the given user language. Returns BotName on success."""

    language_code: str | None = None
    """A two-letter ISO 639-1 language code or an empty string """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["GetMyName"]
