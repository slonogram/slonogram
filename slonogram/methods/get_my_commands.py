# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import BotCommandScope


@dataclass(frozen=False, slots=True)
class GetMyCommands:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""

    scope: BotCommandScope | None = None
    """A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code or an empty string """


__all__ = ["GetMyCommands"]
