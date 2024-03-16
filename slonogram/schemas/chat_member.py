from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class ChatMemberAdministrator:
    can_be_edited: bool
    """ True, if the bot is allowed to edit administrator privileges of that user """
    can_change_info: bool
    """ True, if the user is allowed to change the chat title, photo and other settings """
    can_delete_messages: bool
    """ True, if the administrator can delete messages of other users """
    can_delete_stories: bool
    """ True, if the administrator can delete stories posted by other users """
    can_edit_messages: bool
    """ Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only """
    can_edit_stories: bool
    """ True, if the administrator can edit stories posted by other users """
    can_invite_users: bool
    """ True, if the user is allowed to invite new users to the chat """
    can_manage_chat: bool
    """ True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege. """
    can_manage_topics: bool
    """ Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only """
    can_manage_video_chats: bool
    """ True, if the administrator can manage video chats """
    can_pin_messages: bool
    """ Optional. True, if the user is allowed to pin messages; for groups and supergroups only """
    can_post_messages: bool
    """ Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only """
    can_post_stories: bool
    """ True, if the administrator can post stories to the chat """
    can_promote_members: bool
    """ True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) """
    can_restrict_members: bool
    """ True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics """
    custom_title: str
    """ Optional. Custom title for this user """
    is_anonymous: bool
    """ True, if the user's presence in the chat is hidden """
    status: str
    """ The member's status in the chat, always "administrator" """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        can_be_edited: Omittable[Alterer1[bool]] = OMIT,
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
        status: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
        can_edit_messages: Omittable[Alterer1[bool]] = OMIT,
        can_manage_topics: Omittable[Alterer1[bool]] = OMIT,
        can_pin_messages: Omittable[Alterer1[bool]] = OMIT,
        can_post_messages: Omittable[Alterer1[bool]] = OMIT,
        custom_title: Omittable[Alterer1[str]] = OMIT,
    ):
        return ChatMemberAdministrator(
            can_be_edited=alter1(can_be_edited, self.can_be_edited),
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
            status=alter1(status, self.status),
            user=alter1(user, self.user),
            can_edit_messages=alter1(can_edit_messages, self.can_edit_messages),
            can_manage_topics=alter1(can_manage_topics, self.can_manage_topics),
            can_pin_messages=alter1(can_pin_messages, self.can_pin_messages),
            can_post_messages=alter1(can_post_messages, self.can_post_messages),
            custom_title=alter1(custom_title, self.custom_title),
        )


@model
class ChatMemberBanned:
    status: str
    """ The member's status in the chat, always "kicked" """
    until_date: int
    """ Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        status: Omittable[Alterer1[str]] = OMIT,
        until_date: Omittable[Alterer1[int]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return ChatMemberBanned(
            status=alter1(status, self.status),
            until_date=alter1(until_date, self.until_date),
            user=alter1(user, self.user),
        )


@model
class ChatMemberLeft:
    status: str
    """ The member's status in the chat, always "left" """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        status: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return ChatMemberLeft(
            status=alter1(status, self.status),
            user=alter1(user, self.user),
        )


@model
class ChatMemberMember:
    status: str
    """ The member's status in the chat, always "member" """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        status: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return ChatMemberMember(
            status=alter1(status, self.status),
            user=alter1(user, self.user),
        )


@model
class ChatMemberOwner:
    custom_title: str
    """ Optional. Custom title for this user """
    is_anonymous: bool
    """ True, if the user's presence in the chat is hidden """
    status: str
    """ The member's status in the chat, always "creator" """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        is_anonymous: Omittable[Alterer1[bool]] = OMIT,
        status: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
        custom_title: Omittable[Alterer1[str]] = OMIT,
    ):
        return ChatMemberOwner(
            is_anonymous=alter1(is_anonymous, self.is_anonymous),
            status=alter1(status, self.status),
            user=alter1(user, self.user),
            custom_title=alter1(custom_title, self.custom_title),
        )


@model
class ChatMemberRestricted:
    can_add_web_page_previews: bool
    """ True, if the user is allowed to add web page previews to their messages """
    can_change_info: bool
    """ True, if the user is allowed to change the chat title, photo and other settings """
    can_invite_users: bool
    """ True, if the user is allowed to invite new users to the chat """
    can_manage_topics: bool
    """ True, if the user is allowed to create forum topics """
    can_pin_messages: bool
    """ True, if the user is allowed to pin messages """
    can_send_audios: bool
    """ True, if the user is allowed to send audios """
    can_send_documents: bool
    """ True, if the user is allowed to send documents """
    can_send_messages: bool
    """ True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues """
    can_send_other_messages: bool
    """ True, if the user is allowed to send animations, games, stickers and use inline bots """
    can_send_photos: bool
    """ True, if the user is allowed to send photos """
    can_send_polls: bool
    """ True, if the user is allowed to send polls """
    can_send_video_notes: bool
    """ True, if the user is allowed to send video notes """
    can_send_videos: bool
    """ True, if the user is allowed to send videos """
    can_send_voice_notes: bool
    """ True, if the user is allowed to send voice notes """
    is_member: bool
    """ True, if the user is a member of the chat at the moment of the request """
    status: str
    """ The member's status in the chat, always "restricted" """
    until_date: int
    """ Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever """
    user: _user.User
    """ Information about the user """

    def alter(
        self,
        can_add_web_page_previews: Omittable[Alterer1[bool]] = OMIT,
        can_change_info: Omittable[Alterer1[bool]] = OMIT,
        can_invite_users: Omittable[Alterer1[bool]] = OMIT,
        can_manage_topics: Omittable[Alterer1[bool]] = OMIT,
        can_pin_messages: Omittable[Alterer1[bool]] = OMIT,
        can_send_audios: Omittable[Alterer1[bool]] = OMIT,
        can_send_documents: Omittable[Alterer1[bool]] = OMIT,
        can_send_messages: Omittable[Alterer1[bool]] = OMIT,
        can_send_other_messages: Omittable[Alterer1[bool]] = OMIT,
        can_send_photos: Omittable[Alterer1[bool]] = OMIT,
        can_send_polls: Omittable[Alterer1[bool]] = OMIT,
        can_send_video_notes: Omittable[Alterer1[bool]] = OMIT,
        can_send_videos: Omittable[Alterer1[bool]] = OMIT,
        can_send_voice_notes: Omittable[Alterer1[bool]] = OMIT,
        is_member: Omittable[Alterer1[bool]] = OMIT,
        status: Omittable[Alterer1[str]] = OMIT,
        until_date: Omittable[Alterer1[int]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return ChatMemberRestricted(
            can_add_web_page_previews=alter1(
                can_add_web_page_previews, self.can_add_web_page_previews
            ),
            can_change_info=alter1(can_change_info, self.can_change_info),
            can_invite_users=alter1(can_invite_users, self.can_invite_users),
            can_manage_topics=alter1(can_manage_topics, self.can_manage_topics),
            can_pin_messages=alter1(can_pin_messages, self.can_pin_messages),
            can_send_audios=alter1(can_send_audios, self.can_send_audios),
            can_send_documents=alter1(can_send_documents, self.can_send_documents),
            can_send_messages=alter1(can_send_messages, self.can_send_messages),
            can_send_other_messages=alter1(
                can_send_other_messages, self.can_send_other_messages
            ),
            can_send_photos=alter1(can_send_photos, self.can_send_photos),
            can_send_polls=alter1(can_send_polls, self.can_send_polls),
            can_send_video_notes=alter1(
                can_send_video_notes, self.can_send_video_notes
            ),
            can_send_videos=alter1(can_send_videos, self.can_send_videos),
            can_send_voice_notes=alter1(
                can_send_voice_notes, self.can_send_voice_notes
            ),
            is_member=alter1(is_member, self.is_member),
            status=alter1(status, self.status),
            until_date=alter1(until_date, self.until_date),
            user=alter1(user, self.user),
        )


ChatMember: TypeAlias = (
    ChatMemberOwner
    | ChatMemberAdministrator
    | ChatMemberMember
    | ChatMemberRestricted
    | ChatMemberLeft
    | ChatMemberBanned
)
__all__ = [
    "ChatMemberAdministrator",
    "ChatMemberBanned",
    "ChatMemberLeft",
    "ChatMemberMember",
    "ChatMemberOwner",
    "ChatMemberRestricted",
    "ChatMember",
]
