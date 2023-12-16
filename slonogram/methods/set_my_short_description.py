# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetMyShortDescription:
    """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."""

    short_description: str | None = None
    """New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description. """


__all__ = ["SetMyShortDescription"]