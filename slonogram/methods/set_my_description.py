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
class SetMyDescription:
    """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success."""

    description: str | None = None
    """New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetMyDescription"]
