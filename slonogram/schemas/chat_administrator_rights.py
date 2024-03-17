from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatadministratorrights"""

    can_change_info: bool
    """ True, if the user is allowed to change the chat title, photo and other settings """
    can_delete_messages: bool
    """ True, if the administrator can delete messages of other users """
    can_delete_stories: bool
    """ True, if the administrator can delete stories posted by other users """
    can_edit_stories: bool
    """ True, if the administrator can edit stories posted by other users """
    can_invite_users: bool
    """ True, if the user is allowed to invite new users to the chat """
    can_manage_chat: bool
    """ True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege. """
    can_manage_video_chats: bool
    """ True, if the administrator can manage video chats """
    can_post_stories: bool
    """ True, if the administrator can post stories to the chat """
    can_promote_members: bool
    """ True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) """
    can_restrict_members: bool
    """ True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics """
    is_anonymous: bool
    """ True, if the user's presence in the chat is hidden """
    can_edit_messages: bool | None = None
    """ Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only """
    can_manage_topics: bool | None = None
    """ Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only """
    can_pin_messages: bool | None = None
    """ Optional. True, if the user is allowed to pin messages; for groups and supergroups only """
    can_post_messages: bool | None = None
    """ Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only """

    def alter(
        self,
        can_change_info: Omittable[Alterer1[bool]] = OMIT,
        can_delete_messages: Omittable[Alterer1[bool]] = OMIT,
        can_delete_stories: Omittable[Alterer1[bool]] = OMIT,
        can_edit_stories: Omittable[Alterer1[bool]] = OMIT,
        can_invite_users: Omittable[Alterer1[bool]] = OMIT,
        can_manage_chat: Omittable[Alterer1[bool]] = OMIT,
        can_manage_video_chats: Omittable[Alterer1[bool]] = OMIT,
        can_post_stories: Omittable[Alterer1[bool]] = OMIT,
        can_promote_members: Omittable[Alterer1[bool]] = OMIT,
        can_restrict_members: Omittable[Alterer1[bool]] = OMIT,
        is_anonymous: Omittable[Alterer1[bool]] = OMIT,
        can_edit_messages: Omittable[Alterer1[bool | None]] = OMIT,
        can_manage_topics: Omittable[Alterer1[bool | None]] = OMIT,
        can_pin_messages: Omittable[Alterer1[bool | None]] = OMIT,
        can_post_messages: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> ChatAdministratorRights:
        return ChatAdministratorRights(
            can_change_info=alter1(can_change_info, self.can_change_info),
            can_delete_messages=alter1(can_delete_messages, self.can_delete_messages),
            can_delete_stories=alter1(can_delete_stories, self.can_delete_stories),
            can_edit_stories=alter1(can_edit_stories, self.can_edit_stories),
            can_invite_users=alter1(can_invite_users, self.can_invite_users),
            can_manage_chat=alter1(can_manage_chat, self.can_manage_chat),
            can_manage_video_chats=alter1(
                can_manage_video_chats, self.can_manage_video_chats
            ),
            can_post_stories=alter1(can_post_stories, self.can_post_stories),
            can_promote_members=alter1(can_promote_members, self.can_promote_members),
            can_restrict_members=alter1(
                can_restrict_members, self.can_restrict_members
            ),
            is_anonymous=alter1(is_anonymous, self.is_anonymous),
            can_edit_messages=alter1(can_edit_messages, self.can_edit_messages),
            can_manage_topics=alter1(can_manage_topics, self.can_manage_topics),
            can_pin_messages=alter1(can_pin_messages, self.can_pin_messages),
            can_post_messages=alter1(can_post_messages, self.can_post_messages),
        )


__all__ = ["ChatAdministratorRights"]
