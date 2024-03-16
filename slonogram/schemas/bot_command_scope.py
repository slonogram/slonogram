from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class BotCommandScopeAllChatAdministrators:
    type: str
    """ Scope type, must be all_chat_administrators """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllChatAdministrators(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeAllGroupChats:
    type: str
    """ Scope type, must be all_group_chats """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllGroupChats(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeAllPrivateChats:
    type: str
    """ Scope type, must be all_private_chats """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT):
        return BotCommandScopeAllPrivateChats(
            type=alter1(type, self.type),
        )


@model
class BotCommandScopeChat:
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
