from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators"""

    type: str
    """ Scope type, must be all_chat_administrators """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllChatAdministrators(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopeallgroupchats"""

    type: str
    """ Scope type, must be all_group_chats """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllGroupChats(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopeallprivatechats"""

    type: str
    """ Scope type, must be all_private_chats """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllPrivateChats(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopechat"""

    chat_id: int | str
    """ Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    type: str
    """ Scope type, must be chat """

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return BotCommandScopeChat(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopechatadministrators"""

    chat_id: int | str
    """ Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    type: str
    """ Scope type, must be chat_administrators """

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return BotCommandScopeChatAdministrators(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopechatmember"""

    chat_id: int | str
    """ Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    type: str
    """ Scope type, must be chat_member """
    user_id: int
    """ Unique identifier of the target user """

    def alter(
        self,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        user_id: Omittable[Alterer1[int]] = OMIT,
    ):
        return BotCommandScopeChatMember(
            chat_id=alter1(chat_id, self.chat_id),
            type=alter1(type, self.type),
            user_id=alter1(user_id, self.user_id),
        )


@model
class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
    Telegram docs: https://core.telegram.org/bots/api#botcommandscopedefault"""

    type: str
    """ Scope type, must be default """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
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
__all__ = [
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
    "BotCommandScope",
]
