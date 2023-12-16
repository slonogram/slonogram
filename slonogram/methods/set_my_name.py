# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetMyName:
    """Use this method to change the bot's name. Returns True on success."""

    name: str | None = None
    """New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name. """


__all__ = ["SetMyName"]