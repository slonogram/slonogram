# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import MenuButton


@dataclass(frozen=False, slots=True)
class SetChatMenuButton:
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""

    chat_id: int | None = None
    """Unique identifier for the target private chat. If not specified, default bot's menu button will be changed """
    menu_button: MenuButton | None = None
    """A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault """


__all__ = ["SetChatMenuButton"]
