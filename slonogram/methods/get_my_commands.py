# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from slonogram.schemas import BotCommandScope
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class GetMyCommands:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""

    scope: BotCommandScope | None = None
    """A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code or an empty string """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["GetMyCommands"]
