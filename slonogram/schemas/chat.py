from __future__ import annotations
from slonogram.schemas import (
    reaction_type as _reaction_type,
    chat_location as _chat_location,
    chat_permissions as _chat_permissions,
    chat_photo as _chat_photo,
    maybe_inaccessible_message as _maybe_inaccessible_message,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Chat:
    """This object represents a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chat"""

    id: int
    """ Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    type: str
    """ Type of chat, can be either "private", "group", "supergroup" or "channel" """
    accent_color_id: int | None = None
    """ Optional. Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details. Returned only in getChat. Always returned in getChat. """
    active_usernames: tuple[str, ...] | None = None
    """ Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat. """
    available_reactions: tuple[_reaction_type.ReactionType, ...] | None = None
    """ Optional. List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed. Returned only in getChat. """
    background_custom_emoji_id: str | None = None
    """ Optional. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in getChat. """
    bio: str | None = None
    """ Optional. Bio of the other party in a private chat. Returned only in getChat. """
    can_set_sticker_set: bool | None = None
    """ Optional. True, if the bot can change the group sticker set. Returned only in getChat. """
    custom_emoji_sticker_set_name: str | None = None
    """ Optional. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. Returned only in getChat. """
    description: str | None = None
    """ Optional. Description, for groups, supergroups and channel chats. Returned only in getChat. """
    emoji_status_custom_emoji_id: str | None = None
    """ Optional. Custom emoji identifier of the emoji status of the chat or the other party in a private chat. Returned only in getChat. """
    emoji_status_expiration_date: int | None = None
    """ Optional. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any. Returned only in getChat. """
    first_name: str | None = None
    """ Optional. First name of the other party in a private chat """
    has_aggressive_anti_spam_enabled: bool | None = None
    """ Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat. """
    has_hidden_members: bool | None = None
    """ Optional. True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat. """
    has_private_forwards: bool | None = None
    """ Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat. """
    has_protected_content: bool | None = None
    """ Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat. """
    has_restricted_voice_and_video_messages: bool | None = None
    """ Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat. """
    has_visible_history: bool | None = None
    """ Optional. True, if new chat members will have access to old messages; available only to chat administrators. Returned only in getChat. """
    invite_link: str | None = None
    """ Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat. """
    is_forum: bool | None = None
    """ Optional. True, if the supergroup chat is a forum (has topics enabled) """
    join_by_request: bool | None = None
    """ Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat. """
    join_to_send_messages: bool | None = None
    """ Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat. """
    last_name: str | None = None
    """ Optional. Last name of the other party in a private chat """
    linked_chat_id: int | None = None
    """ Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat. """
    location: _chat_location.ChatLocation | None = None
    """ Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat. """
    message_auto_delete_time: int | None = None
    """ Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat. """
    permissions: _chat_permissions.ChatPermissions | None = None
    """ Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat. """
    photo: _chat_photo.ChatPhoto | None = None
    """ Optional. Chat photo. Returned only in getChat. """
    pinned_message: _maybe_inaccessible_message.Message | None = None
    """ Optional. The most recent pinned message (by sending date). Returned only in getChat. """
    profile_accent_color_id: int | None = None
    """ Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details. Returned only in getChat. """
    profile_background_custom_emoji_id: str | None = None
    """ Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in getChat. """
    slow_mode_delay: int | None = None
    """ Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds. Returned only in getChat. """
    sticker_set_name: str | None = None
    """ Optional. For supergroups, name of group sticker set. Returned only in getChat. """
    title: str | None = None
    """ Optional. Title, for supergroups, channels and group chats """
    unrestrict_boost_count: int | None = None
    """ Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in getChat. """
    username: str | None = None
    """ Optional. Username, for private chats, supergroups and channels if available """

    def alter(
        self,
        id: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        accent_color_id: Omittable[Alterer1[int | None]] = OMIT,
        active_usernames: Omittable[Alterer1[tuple[str, ...] | None]] = OMIT,
        available_reactions: Omittable[
            Alterer1[tuple[_reaction_type.ReactionType, ...] | None]
        ] = OMIT,
        background_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
        bio: Omittable[Alterer1[str | None]] = OMIT,
        can_set_sticker_set: Omittable[Alterer1[bool | None]] = OMIT,
        custom_emoji_sticker_set_name: Omittable[Alterer1[str | None]] = OMIT,
        description: Omittable[Alterer1[str | None]] = OMIT,
        emoji_status_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
        emoji_status_expiration_date: Omittable[Alterer1[int | None]] = OMIT,
        first_name: Omittable[Alterer1[str | None]] = OMIT,
        has_aggressive_anti_spam_enabled: Omittable[Alterer1[bool | None]] = OMIT,
        has_hidden_members: Omittable[Alterer1[bool | None]] = OMIT,
        has_private_forwards: Omittable[Alterer1[bool | None]] = OMIT,
        has_protected_content: Omittable[Alterer1[bool | None]] = OMIT,
        has_restricted_voice_and_video_messages: Omittable[
            Alterer1[bool | None]
        ] = OMIT,
        has_visible_history: Omittable[Alterer1[bool | None]] = OMIT,
        invite_link: Omittable[Alterer1[str | None]] = OMIT,
        is_forum: Omittable[Alterer1[bool | None]] = OMIT,
        join_by_request: Omittable[Alterer1[bool | None]] = OMIT,
        join_to_send_messages: Omittable[Alterer1[bool | None]] = OMIT,
        last_name: Omittable[Alterer1[str | None]] = OMIT,
        linked_chat_id: Omittable[Alterer1[int | None]] = OMIT,
        location: Omittable[Alterer1[_chat_location.ChatLocation | None]] = OMIT,
        message_auto_delete_time: Omittable[Alterer1[int | None]] = OMIT,
        permissions: Omittable[
            Alterer1[_chat_permissions.ChatPermissions | None]
        ] = OMIT,
        photo: Omittable[Alterer1[_chat_photo.ChatPhoto | None]] = OMIT,
        pinned_message: Omittable[
            Alterer1[_maybe_inaccessible_message.Message | None]
        ] = OMIT,
        profile_accent_color_id: Omittable[Alterer1[int | None]] = OMIT,
        profile_background_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
        slow_mode_delay: Omittable[Alterer1[int | None]] = OMIT,
        sticker_set_name: Omittable[Alterer1[str | None]] = OMIT,
        title: Omittable[Alterer1[str | None]] = OMIT,
        unrestrict_boost_count: Omittable[Alterer1[int | None]] = OMIT,
        username: Omittable[Alterer1[str | None]] = OMIT,
    ) -> Chat:
        return Chat(
            id=alter1(id, self.id),
            type=alter1(type, self.type),
            accent_color_id=alter1(accent_color_id, self.accent_color_id),
            active_usernames=alter1(active_usernames, self.active_usernames),
            available_reactions=alter1(available_reactions, self.available_reactions),
            background_custom_emoji_id=alter1(
                background_custom_emoji_id, self.background_custom_emoji_id
            ),
            bio=alter1(bio, self.bio),
            can_set_sticker_set=alter1(can_set_sticker_set, self.can_set_sticker_set),
            custom_emoji_sticker_set_name=alter1(
                custom_emoji_sticker_set_name, self.custom_emoji_sticker_set_name
            ),
            description=alter1(description, self.description),
            emoji_status_custom_emoji_id=alter1(
                emoji_status_custom_emoji_id, self.emoji_status_custom_emoji_id
            ),
            emoji_status_expiration_date=alter1(
                emoji_status_expiration_date, self.emoji_status_expiration_date
            ),
            first_name=alter1(first_name, self.first_name),
            has_aggressive_anti_spam_enabled=alter1(
                has_aggressive_anti_spam_enabled, self.has_aggressive_anti_spam_enabled
            ),
            has_hidden_members=alter1(has_hidden_members, self.has_hidden_members),
            has_private_forwards=alter1(
                has_private_forwards, self.has_private_forwards
            ),
            has_protected_content=alter1(
                has_protected_content, self.has_protected_content
            ),
            has_restricted_voice_and_video_messages=alter1(
                has_restricted_voice_and_video_messages,
                self.has_restricted_voice_and_video_messages,
            ),
            has_visible_history=alter1(has_visible_history, self.has_visible_history),
            invite_link=alter1(invite_link, self.invite_link),
            is_forum=alter1(is_forum, self.is_forum),
            join_by_request=alter1(join_by_request, self.join_by_request),
            join_to_send_messages=alter1(
                join_to_send_messages, self.join_to_send_messages
            ),
            last_name=alter1(last_name, self.last_name),
            linked_chat_id=alter1(linked_chat_id, self.linked_chat_id),
            location=alter1(location, self.location),
            message_auto_delete_time=alter1(
                message_auto_delete_time, self.message_auto_delete_time
            ),
            permissions=alter1(permissions, self.permissions),
            photo=alter1(photo, self.photo),
            pinned_message=alter1(pinned_message, self.pinned_message),
            profile_accent_color_id=alter1(
                profile_accent_color_id, self.profile_accent_color_id
            ),
            profile_background_custom_emoji_id=alter1(
                profile_background_custom_emoji_id,
                self.profile_background_custom_emoji_id,
            ),
            slow_mode_delay=alter1(slow_mode_delay, self.slow_mode_delay),
            sticker_set_name=alter1(sticker_set_name, self.sticker_set_name),
            title=alter1(title, self.title),
            unrestrict_boost_count=alter1(
                unrestrict_boost_count, self.unrestrict_boost_count
            ),
            username=alter1(username, self.username),
        )


__all__ = ["Chat"]
