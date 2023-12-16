# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import BotCommandScope, BotCommand


@dataclass(frozen=False, slots=True)
class SetMyCommands:
    """Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success."""

    commands: list[BotCommand]
    """A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified. """
    scope: BotCommandScope | None = None
    """A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault. """
    language_code: str | None = None
    """A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands """


__all__ = ["SetMyCommands"]