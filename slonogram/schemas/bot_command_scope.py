"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass
from typing import TypeAlias


@dataclass(slots=True)
class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and
    supergroup chat administrators.  Telegram documentation: https://core.
    telegram.org/bots/api#botcommandscopeallchatadministrators"""

    type: str
    """Scope type, must be all_chat_administrators"""

    def alter(
        self, type: Omittable[Alterer1[str]] = OMIT
    ) -> BotCommandScopeAllChatAdministrators:
        return BotCommandScopeAllChatAdministrators(
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and
    supergroup chats.  Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopeallgroupchats"""

    type: str
    """Scope type, must be all_group_chats"""

    def alter(
        self, type: Omittable[Alterer1[str]] = OMIT
    ) -> BotCommandScopeAllGroupChats:
        return BotCommandScopeAllGroupChats(
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats.
    Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopeallprivatechats"""

    type: str
    """Scope type, must be all_private_chats"""

    def alter(
        self, type: Omittable[Alterer1[str]] = OMIT
    ) -> BotCommandScopeAllPrivateChats:
        return BotCommandScopeAllPrivateChats(
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat.
    Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopechat"""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""
    type: str
    """Scope type, must be chat"""

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> BotCommandScopeChat:
        return BotCommandScopeChat(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a
    specific group or supergroup chat.  Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopechatadministrators"""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""
    type: str
    """Scope type, must be chat_administrators"""

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> BotCommandScopeChatAdministrators:
        return BotCommandScopeChatAdministrators(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat.  Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopechatmember"""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""
    type: str
    """Scope type, must be chat_member"""
    user_id: int
    """Unique identifier of the target user"""

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        user_id: Omittable[Alterer1[int]] = OMIT,
    ) -> BotCommandScopeChatMember:
        return BotCommandScopeChatMember(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
            user_id=alter1(user_id, self.user_id),
        )


@dataclass(slots=True)
class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the user.
    Telegram documentation:
    https://core.telegram.org/bots/api#botcommandscopedefault"""

    type: str
    """Scope type, must be default"""

    def alter(self, type: Omittable[Alterer1[str]] = OMIT) -> BotCommandScopeDefault:
        return BotCommandScopeDefault(
            type=alter1(type, self.type),
        )


BotCommandScope: TypeAlias = (
    BotCommandScopeDefault
    | BotCommandScopeAllPrivateChats
    | BotCommandScopeAllGroupChats
    | BotCommandScopeAllChatAdministrators
    | BotCommandScopeChat
    | BotCommandScopeChatAdministrators
    | BotCommandScopeChatMember
)
""" This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
- BotCommandScopeDefault
- BotCommandScopeAllPrivateChats
- BotCommandScopeAllGroupChats
- BotCommandScopeAllChatAdministrators
- BotCommandScopeChat
- BotCommandScopeChatAdministrators
- BotCommandScopeChatMember

Telegram documentation: https://core.telegram.org/bots/api#botcommandscope """
__all__ = [
    "BotCommandScope",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
]
