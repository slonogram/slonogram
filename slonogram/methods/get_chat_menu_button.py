# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetChatMenuButton:
    """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""

    chat_id: int | None = None
    """Unique identifier for the target private chat. If not specified, default bot's menu button will be returned """


__all__ = ["GetChatMenuButton"]
