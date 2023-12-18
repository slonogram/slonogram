# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class PromoteChatMember:
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    user_id: int
    """Unique identifier of the target user """
    is_anonymous: bool | None = None
    """Pass True if the administrator's presence in the chat is hidden """
    can_manage_chat: bool | None = None
    """Pass True if the administrator can access the chat event log, boost list in channels, see channel members, report spam messages, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege """
    can_delete_messages: bool | None = None
    """Pass True if the administrator can delete messages of other users """
    can_manage_video_chats: bool | None = None
    """Pass True if the administrator can manage video chats """
    can_restrict_members: bool | None = None
    """Pass True if the administrator can restrict, ban or unban chat members, or access supergroup statistics """
    can_promote_members: bool | None = None
    """Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him) """
    can_change_info: bool | None = None
    """Pass True if the administrator can change chat title, photo and other settings """
    can_invite_users: bool | None = None
    """Pass True if the administrator can invite new users to the chat """
    can_post_messages: bool | None = None
    """Pass True if the administrator can post messages in the channel, or access channel statistics; channels only """
    can_edit_messages: bool | None = None
    """Pass True if the administrator can edit messages of other users and can pin messages; channels only """
    can_pin_messages: bool | None = None
    """Pass True if the administrator can pin messages, supergroups only """
    can_post_stories: bool | None = None
    """Pass True if the administrator can post stories in the channel; channels only """
    can_edit_stories: bool | None = None
    """Pass True if the administrator can edit stories posted by other users; channels only """
    can_delete_stories: bool | None = None
    """Pass True if the administrator can delete stories posted by other users; channels only """
    can_manage_topics: bool | None = None
    """Pass True if the user is allowed to create, rename, close, and reopen forum topics, supergroups only """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["PromoteChatMember"]
