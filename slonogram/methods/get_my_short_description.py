# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetMyShortDescription:
    """Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success."""

    language_code: str | None = None
    """A two-letter ISO 639-1 language code or an empty string """


__all__ = ["GetMyShortDescription"]
