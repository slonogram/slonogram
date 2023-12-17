# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 08:56:56.806984
from dataclasses import dataclass
from slonogram.schemas import BotCommandScope
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class DeleteMyCommands:
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""

    scope: BotCommandScope | None = None
    """A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["DeleteMyCommands"]
