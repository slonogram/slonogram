# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 08:56:56.806984
from __future__ import annotations
from slonogram._internal.utils import prefer
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import AlterFn, collect_attachs_from
from types import EllipsisType
from typing import TypeAlias


@dataclass(frozen=False, slots=True)
class Update:
    """This object represents an incoming update.
    At most one of the optional parameters can be present in any given update."""

    update_id: int
    """The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially. """
    message: Message | None = None
    """Optional. New incoming message of any kind - text, photo, sticker, etc. """
    edited_message: Message | None = None
    """Optional. New version of a message that is known to the bot and was edited """
    channel_post: Message | None = None
    """Optional. New incoming channel post of any kind - text, photo, sticker, etc. """
    edited_channel_post: Message | None = None
    """Optional. New version of a channel post that is known to the bot and was edited """
    inline_query: InlineQuery | None = None
    """Optional. New incoming inline query """
    chosen_inline_result: ChosenInlineResult | None = None
    """Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot. """
    callback_query: CallbackQuery | None = None
    """Optional. New incoming callback query """
    shipping_query: ShippingQuery | None = None
    """Optional. New incoming shipping query. Only for invoices with flexible price """
    pre_checkout_query: PreCheckoutQuery | None = None
    """Optional. New incoming pre-checkout query. Contains full information about checkout """
    poll: Poll | None = None
    """Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot """
    poll_answer: PollAnswer | None = None
    """Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself. """
    my_chat_member: ChatMemberUpdated | None = None
    """Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user. """
    chat_member: ChatMemberUpdated | None = None
    """Optional. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates. """
    chat_join_request: ChatJoinRequest | None = None
    """Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        update_id: AlterFn[int] | EllipsisType = ...,
        message: AlterFn[Message | None] | EllipsisType = ...,
        edited_message: AlterFn[Message | None] | EllipsisType = ...,
        channel_post: AlterFn[Message | None] | EllipsisType = ...,
        edited_channel_post: AlterFn[Message | None] | EllipsisType = ...,
        inline_query: AlterFn[InlineQuery | None] | EllipsisType = ...,
        chosen_inline_result: AlterFn[ChosenInlineResult | None] | EllipsisType = ...,
        callback_query: AlterFn[CallbackQuery | None] | EllipsisType = ...,
        shipping_query: AlterFn[ShippingQuery | None] | EllipsisType = ...,
        pre_checkout_query: AlterFn[PreCheckoutQuery | None] | EllipsisType = ...,
        poll: AlterFn[Poll | None] | EllipsisType = ...,
        poll_answer: AlterFn[PollAnswer | None] | EllipsisType = ...,
        my_chat_member: AlterFn[ChatMemberUpdated | None] | EllipsisType = ...,
        chat_member: AlterFn[ChatMemberUpdated | None] | EllipsisType = ...,
        chat_join_request: AlterFn[ChatJoinRequest | None] | EllipsisType = ...,
    ) -> Update:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Update(
            update_id=self.update_id
            if update_id is ...
            else prefer(update_id(self.update_id), self.update_id),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
            edited_message=self.edited_message
            if edited_message is ...
            else prefer(edited_message(self.edited_message), self.edited_message),
            channel_post=self.channel_post
            if channel_post is ...
            else prefer(channel_post(self.channel_post), self.channel_post),
            edited_channel_post=self.edited_channel_post
            if edited_channel_post is ...
            else prefer(
                edited_channel_post(self.edited_channel_post), self.edited_channel_post
            ),
            inline_query=self.inline_query
            if inline_query is ...
            else prefer(inline_query(self.inline_query), self.inline_query),
            chosen_inline_result=self.chosen_inline_result
            if chosen_inline_result is ...
            else prefer(
                chosen_inline_result(self.chosen_inline_result),
                self.chosen_inline_result,
            ),
            callback_query=self.callback_query
            if callback_query is ...
            else prefer(callback_query(self.callback_query), self.callback_query),
            shipping_query=self.shipping_query
            if shipping_query is ...
            else prefer(shipping_query(self.shipping_query), self.shipping_query),
            pre_checkout_query=self.pre_checkout_query
            if pre_checkout_query is ...
            else prefer(
                pre_checkout_query(self.pre_checkout_query), self.pre_checkout_query
            ),
            poll=self.poll if poll is ... else prefer(poll(self.poll), self.poll),
            poll_answer=self.poll_answer
            if poll_answer is ...
            else prefer(poll_answer(self.poll_answer), self.poll_answer),
            my_chat_member=self.my_chat_member
            if my_chat_member is ...
            else prefer(my_chat_member(self.my_chat_member), self.my_chat_member),
            chat_member=self.chat_member
            if chat_member is ...
            else prefer(chat_member(self.chat_member), self.chat_member),
            chat_join_request=self.chat_join_request
            if chat_join_request is ...
            else prefer(
                chat_join_request(self.chat_join_request), self.chat_join_request
            ),
        )

    def copy_with(
        self,
        update_id: int | EllipsisType = ...,
        message: Message | None | EllipsisType = ...,
        edited_message: Message | None | EllipsisType = ...,
        channel_post: Message | None | EllipsisType = ...,
        edited_channel_post: Message | None | EllipsisType = ...,
        inline_query: InlineQuery | None | EllipsisType = ...,
        chosen_inline_result: ChosenInlineResult | None | EllipsisType = ...,
        callback_query: CallbackQuery | None | EllipsisType = ...,
        shipping_query: ShippingQuery | None | EllipsisType = ...,
        pre_checkout_query: PreCheckoutQuery | None | EllipsisType = ...,
        poll: Poll | None | EllipsisType = ...,
        poll_answer: PollAnswer | None | EllipsisType = ...,
        my_chat_member: ChatMemberUpdated | None | EllipsisType = ...,
        chat_member: ChatMemberUpdated | None | EllipsisType = ...,
        chat_join_request: ChatJoinRequest | None | EllipsisType = ...,
    ) -> Update:
        """Replaces some of model's fields with provided ones"""
        return Update(
            update_id=update_id if update_id is not ... else self.update_id,
            message=message if message is not ... else self.message,
            edited_message=edited_message
            if edited_message is not ...
            else self.edited_message,
            channel_post=channel_post if channel_post is not ... else self.channel_post,
            edited_channel_post=edited_channel_post
            if edited_channel_post is not ...
            else self.edited_channel_post,
            inline_query=inline_query if inline_query is not ... else self.inline_query,
            chosen_inline_result=chosen_inline_result
            if chosen_inline_result is not ...
            else self.chosen_inline_result,
            callback_query=callback_query
            if callback_query is not ...
            else self.callback_query,
            shipping_query=shipping_query
            if shipping_query is not ...
            else self.shipping_query,
            pre_checkout_query=pre_checkout_query
            if pre_checkout_query is not ...
            else self.pre_checkout_query,
            poll=poll if poll is not ... else self.poll,
            poll_answer=poll_answer if poll_answer is not ... else self.poll_answer,
            my_chat_member=my_chat_member
            if my_chat_member is not ...
            else self.my_chat_member,
            chat_member=chat_member if chat_member is not ... else self.chat_member,
            chat_join_request=chat_join_request
            if chat_join_request is not ...
            else self.chat_join_request,
        )


@dataclass(frozen=False, slots=True)
class WebhookInfo:
    """Describes the current status of a webhook."""

    url: str
    """Webhook URL, may be empty if webhook is not set up """
    has_custom_certificate: bool
    """True, if a custom certificate was provided for webhook certificate checks """
    pending_update_count: int
    """Number of updates awaiting delivery """
    ip_address: str | None = None
    """Optional. Currently used webhook IP address """
    last_error_date: int | None = None
    """Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook """
    last_error_message: str | None = None
    """Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook """
    last_synchronization_error_date: int | None = None
    """Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters """
    max_connections: int | None = None
    """Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery """
    allowed_updates: list[str] | None = None
    """Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        url: AlterFn[str] | EllipsisType = ...,
        has_custom_certificate: AlterFn[bool] | EllipsisType = ...,
        pending_update_count: AlterFn[int] | EllipsisType = ...,
        ip_address: AlterFn[str | None] | EllipsisType = ...,
        last_error_date: AlterFn[int | None] | EllipsisType = ...,
        last_error_message: AlterFn[str | None] | EllipsisType = ...,
        last_synchronization_error_date: AlterFn[int | None] | EllipsisType = ...,
        max_connections: AlterFn[int | None] | EllipsisType = ...,
        allowed_updates: AlterFn[list[str] | None] | EllipsisType = ...,
    ) -> WebhookInfo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return WebhookInfo(
            url=self.url if url is ... else prefer(url(self.url), self.url),
            has_custom_certificate=self.has_custom_certificate
            if has_custom_certificate is ...
            else prefer(
                has_custom_certificate(self.has_custom_certificate),
                self.has_custom_certificate,
            ),
            pending_update_count=self.pending_update_count
            if pending_update_count is ...
            else prefer(
                pending_update_count(self.pending_update_count),
                self.pending_update_count,
            ),
            ip_address=self.ip_address
            if ip_address is ...
            else prefer(ip_address(self.ip_address), self.ip_address),
            last_error_date=self.last_error_date
            if last_error_date is ...
            else prefer(last_error_date(self.last_error_date), self.last_error_date),
            last_error_message=self.last_error_message
            if last_error_message is ...
            else prefer(
                last_error_message(self.last_error_message), self.last_error_message
            ),
            last_synchronization_error_date=self.last_synchronization_error_date
            if last_synchronization_error_date is ...
            else prefer(
                last_synchronization_error_date(self.last_synchronization_error_date),
                self.last_synchronization_error_date,
            ),
            max_connections=self.max_connections
            if max_connections is ...
            else prefer(max_connections(self.max_connections), self.max_connections),
            allowed_updates=self.allowed_updates
            if allowed_updates is ...
            else prefer(allowed_updates(self.allowed_updates), self.allowed_updates),
        )

    def copy_with(
        self,
        url: str | EllipsisType = ...,
        has_custom_certificate: bool | EllipsisType = ...,
        pending_update_count: int | EllipsisType = ...,
        ip_address: str | None | EllipsisType = ...,
        last_error_date: int | None | EllipsisType = ...,
        last_error_message: str | None | EllipsisType = ...,
        last_synchronization_error_date: int | None | EllipsisType = ...,
        max_connections: int | None | EllipsisType = ...,
        allowed_updates: list[str] | None | EllipsisType = ...,
    ) -> WebhookInfo:
        """Replaces some of model's fields with provided ones"""
        return WebhookInfo(
            url=url if url is not ... else self.url,
            has_custom_certificate=has_custom_certificate
            if has_custom_certificate is not ...
            else self.has_custom_certificate,
            pending_update_count=pending_update_count
            if pending_update_count is not ...
            else self.pending_update_count,
            ip_address=ip_address if ip_address is not ... else self.ip_address,
            last_error_date=last_error_date
            if last_error_date is not ...
            else self.last_error_date,
            last_error_message=last_error_message
            if last_error_message is not ...
            else self.last_error_message,
            last_synchronization_error_date=last_synchronization_error_date
            if last_synchronization_error_date is not ...
            else self.last_synchronization_error_date,
            max_connections=max_connections
            if max_connections is not ...
            else self.max_connections,
            allowed_updates=allowed_updates
            if allowed_updates is not ...
            else self.allowed_updates,
        )


@dataclass(frozen=False, slots=True)
class User:
    """This object represents a Telegram user or bot."""

    id: int
    """Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. """
    is_bot: bool
    """True, if this user is a bot """
    first_name: str
    """User's or bot's first name """
    last_name: str | None = None
    """Optional. User's or bot's last name """
    username: str | None = None
    """Optional. User's or bot's username """
    language_code: str | None = None
    """Optional. IETF language tag of the user's language """
    is_premium: bool | None = None
    """Optional. True, if this user is a Telegram Premium user """
    added_to_attachment_menu: bool | None = None
    """Optional. True, if this user added the bot to the attachment menu """
    can_join_groups: bool | None = None
    """Optional. True, if the bot can be invited to groups. Returned only in getMe. """
    can_read_all_group_messages: bool | None = None
    """Optional. True, if privacy mode is disabled for the bot. Returned only in getMe. """
    supports_inline_queries: bool | None = None
    """Optional. True, if the bot supports inline queries. Returned only in getMe. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[int] | EllipsisType = ...,
        is_bot: AlterFn[bool] | EllipsisType = ...,
        first_name: AlterFn[str] | EllipsisType = ...,
        last_name: AlterFn[str | None] | EllipsisType = ...,
        username: AlterFn[str | None] | EllipsisType = ...,
        language_code: AlterFn[str | None] | EllipsisType = ...,
        is_premium: AlterFn[bool | None] | EllipsisType = ...,
        added_to_attachment_menu: AlterFn[bool | None] | EllipsisType = ...,
        can_join_groups: AlterFn[bool | None] | EllipsisType = ...,
        can_read_all_group_messages: AlterFn[bool | None] | EllipsisType = ...,
        supports_inline_queries: AlterFn[bool | None] | EllipsisType = ...,
    ) -> User:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return User(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            is_bot=self.is_bot
            if is_bot is ...
            else prefer(is_bot(self.is_bot), self.is_bot),
            first_name=self.first_name
            if first_name is ...
            else prefer(first_name(self.first_name), self.first_name),
            last_name=self.last_name
            if last_name is ...
            else prefer(last_name(self.last_name), self.last_name),
            username=self.username
            if username is ...
            else prefer(username(self.username), self.username),
            language_code=self.language_code
            if language_code is ...
            else prefer(language_code(self.language_code), self.language_code),
            is_premium=self.is_premium
            if is_premium is ...
            else prefer(is_premium(self.is_premium), self.is_premium),
            added_to_attachment_menu=self.added_to_attachment_menu
            if added_to_attachment_menu is ...
            else prefer(
                added_to_attachment_menu(self.added_to_attachment_menu),
                self.added_to_attachment_menu,
            ),
            can_join_groups=self.can_join_groups
            if can_join_groups is ...
            else prefer(can_join_groups(self.can_join_groups), self.can_join_groups),
            can_read_all_group_messages=self.can_read_all_group_messages
            if can_read_all_group_messages is ...
            else prefer(
                can_read_all_group_messages(self.can_read_all_group_messages),
                self.can_read_all_group_messages,
            ),
            supports_inline_queries=self.supports_inline_queries
            if supports_inline_queries is ...
            else prefer(
                supports_inline_queries(self.supports_inline_queries),
                self.supports_inline_queries,
            ),
        )

    def copy_with(
        self,
        id: int | EllipsisType = ...,
        is_bot: bool | EllipsisType = ...,
        first_name: str | EllipsisType = ...,
        last_name: str | None | EllipsisType = ...,
        username: str | None | EllipsisType = ...,
        language_code: str | None | EllipsisType = ...,
        is_premium: bool | None | EllipsisType = ...,
        added_to_attachment_menu: bool | None | EllipsisType = ...,
        can_join_groups: bool | None | EllipsisType = ...,
        can_read_all_group_messages: bool | None | EllipsisType = ...,
        supports_inline_queries: bool | None | EllipsisType = ...,
    ) -> User:
        """Replaces some of model's fields with provided ones"""
        return User(
            id=id if id is not ... else self.id,
            is_bot=is_bot if is_bot is not ... else self.is_bot,
            first_name=first_name if first_name is not ... else self.first_name,
            last_name=last_name if last_name is not ... else self.last_name,
            username=username if username is not ... else self.username,
            language_code=language_code
            if language_code is not ...
            else self.language_code,
            is_premium=is_premium if is_premium is not ... else self.is_premium,
            added_to_attachment_menu=added_to_attachment_menu
            if added_to_attachment_menu is not ...
            else self.added_to_attachment_menu,
            can_join_groups=can_join_groups
            if can_join_groups is not ...
            else self.can_join_groups,
            can_read_all_group_messages=can_read_all_group_messages
            if can_read_all_group_messages is not ...
            else self.can_read_all_group_messages,
            supports_inline_queries=supports_inline_queries
            if supports_inline_queries is not ...
            else self.supports_inline_queries,
        )


@dataclass(frozen=False, slots=True)
class Chat:
    """This object represents a chat."""

    id: int
    """Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    type: str
    """Type of chat, can be either "private", "group", "supergroup" or "channel" """
    title: str | None = None
    """Optional. Title, for supergroups, channels and group chats """
    username: str | None = None
    """Optional. Username, for private chats, supergroups and channels if available """
    first_name: str | None = None
    """Optional. First name of the other party in a private chat """
    last_name: str | None = None
    """Optional. Last name of the other party in a private chat """
    is_forum: bool | None = None
    """Optional. True, if the supergroup chat is a forum (has topics enabled) """
    photo: ChatPhoto | None = None
    """Optional. Chat photo. Returned only in getChat. """
    active_usernames: list[str] | None = None
    """Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat. """
    emoji_status_custom_emoji_id: str | None = None
    """Optional. Custom emoji identifier of emoji status of the other party in a private chat. Returned only in getChat. """
    emoji_status_expiration_date: int | None = None
    """Optional. Expiration date of the emoji status of the other party in a private chat in Unix time, if any. Returned only in getChat. """
    bio: str | None = None
    """Optional. Bio of the other party in a private chat. Returned only in getChat. """
    has_private_forwards: bool | None = None
    """Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat. """
    has_restricted_voice_and_video_messages: bool | None = None
    """Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat. """
    join_to_send_messages: bool | None = None
    """Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat. """
    join_by_request: bool | None = None
    """Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat. """
    description: str | None = None
    """Optional. Description, for groups, supergroups and channel chats. Returned only in getChat. """
    invite_link: str | None = None
    """Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat. """
    pinned_message: Message | None = None
    """Optional. The most recent pinned message (by sending date). Returned only in getChat. """
    permissions: ChatPermissions | None = None
    """Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat. """
    slow_mode_delay: int | None = None
    """Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat. """
    message_auto_delete_time: int | None = None
    """Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat. """
    has_aggressive_anti_spam_enabled: bool | None = None
    """Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat. """
    has_hidden_members: bool | None = None
    """Optional. True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat. """
    has_protected_content: bool | None = None
    """Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat. """
    sticker_set_name: str | None = None
    """Optional. For supergroups, name of group sticker set. Returned only in getChat. """
    can_set_sticker_set: bool | None = None
    """Optional. True, if the bot can change the group sticker set. Returned only in getChat. """
    linked_chat_id: int | None = None
    """Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat. """
    location: ChatLocation | None = None
    """Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[int] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        username: AlterFn[str | None] | EllipsisType = ...,
        first_name: AlterFn[str | None] | EllipsisType = ...,
        last_name: AlterFn[str | None] | EllipsisType = ...,
        is_forum: AlterFn[bool | None] | EllipsisType = ...,
        photo: AlterFn[ChatPhoto | None] | EllipsisType = ...,
        active_usernames: AlterFn[list[str] | None] | EllipsisType = ...,
        emoji_status_custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
        emoji_status_expiration_date: AlterFn[int | None] | EllipsisType = ...,
        bio: AlterFn[str | None] | EllipsisType = ...,
        has_private_forwards: AlterFn[bool | None] | EllipsisType = ...,
        has_restricted_voice_and_video_messages: AlterFn[bool | None]
        | EllipsisType = ...,
        join_to_send_messages: AlterFn[bool | None] | EllipsisType = ...,
        join_by_request: AlterFn[bool | None] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        invite_link: AlterFn[str | None] | EllipsisType = ...,
        pinned_message: AlterFn[Message | None] | EllipsisType = ...,
        permissions: AlterFn[ChatPermissions | None] | EllipsisType = ...,
        slow_mode_delay: AlterFn[int | None] | EllipsisType = ...,
        message_auto_delete_time: AlterFn[int | None] | EllipsisType = ...,
        has_aggressive_anti_spam_enabled: AlterFn[bool | None] | EllipsisType = ...,
        has_hidden_members: AlterFn[bool | None] | EllipsisType = ...,
        has_protected_content: AlterFn[bool | None] | EllipsisType = ...,
        sticker_set_name: AlterFn[str | None] | EllipsisType = ...,
        can_set_sticker_set: AlterFn[bool | None] | EllipsisType = ...,
        linked_chat_id: AlterFn[int | None] | EllipsisType = ...,
        location: AlterFn[ChatLocation | None] | EllipsisType = ...,
    ) -> Chat:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Chat(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            username=self.username
            if username is ...
            else prefer(username(self.username), self.username),
            first_name=self.first_name
            if first_name is ...
            else prefer(first_name(self.first_name), self.first_name),
            last_name=self.last_name
            if last_name is ...
            else prefer(last_name(self.last_name), self.last_name),
            is_forum=self.is_forum
            if is_forum is ...
            else prefer(is_forum(self.is_forum), self.is_forum),
            photo=self.photo if photo is ... else prefer(photo(self.photo), self.photo),
            active_usernames=self.active_usernames
            if active_usernames is ...
            else prefer(active_usernames(self.active_usernames), self.active_usernames),
            emoji_status_custom_emoji_id=self.emoji_status_custom_emoji_id
            if emoji_status_custom_emoji_id is ...
            else prefer(
                emoji_status_custom_emoji_id(self.emoji_status_custom_emoji_id),
                self.emoji_status_custom_emoji_id,
            ),
            emoji_status_expiration_date=self.emoji_status_expiration_date
            if emoji_status_expiration_date is ...
            else prefer(
                emoji_status_expiration_date(self.emoji_status_expiration_date),
                self.emoji_status_expiration_date,
            ),
            bio=self.bio if bio is ... else prefer(bio(self.bio), self.bio),
            has_private_forwards=self.has_private_forwards
            if has_private_forwards is ...
            else prefer(
                has_private_forwards(self.has_private_forwards),
                self.has_private_forwards,
            ),
            has_restricted_voice_and_video_messages=self.has_restricted_voice_and_video_messages
            if has_restricted_voice_and_video_messages is ...
            else prefer(
                has_restricted_voice_and_video_messages(
                    self.has_restricted_voice_and_video_messages
                ),
                self.has_restricted_voice_and_video_messages,
            ),
            join_to_send_messages=self.join_to_send_messages
            if join_to_send_messages is ...
            else prefer(
                join_to_send_messages(self.join_to_send_messages),
                self.join_to_send_messages,
            ),
            join_by_request=self.join_by_request
            if join_by_request is ...
            else prefer(join_by_request(self.join_by_request), self.join_by_request),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            invite_link=self.invite_link
            if invite_link is ...
            else prefer(invite_link(self.invite_link), self.invite_link),
            pinned_message=self.pinned_message
            if pinned_message is ...
            else prefer(pinned_message(self.pinned_message), self.pinned_message),
            permissions=self.permissions
            if permissions is ...
            else prefer(permissions(self.permissions), self.permissions),
            slow_mode_delay=self.slow_mode_delay
            if slow_mode_delay is ...
            else prefer(slow_mode_delay(self.slow_mode_delay), self.slow_mode_delay),
            message_auto_delete_time=self.message_auto_delete_time
            if message_auto_delete_time is ...
            else prefer(
                message_auto_delete_time(self.message_auto_delete_time),
                self.message_auto_delete_time,
            ),
            has_aggressive_anti_spam_enabled=self.has_aggressive_anti_spam_enabled
            if has_aggressive_anti_spam_enabled is ...
            else prefer(
                has_aggressive_anti_spam_enabled(self.has_aggressive_anti_spam_enabled),
                self.has_aggressive_anti_spam_enabled,
            ),
            has_hidden_members=self.has_hidden_members
            if has_hidden_members is ...
            else prefer(
                has_hidden_members(self.has_hidden_members), self.has_hidden_members
            ),
            has_protected_content=self.has_protected_content
            if has_protected_content is ...
            else prefer(
                has_protected_content(self.has_protected_content),
                self.has_protected_content,
            ),
            sticker_set_name=self.sticker_set_name
            if sticker_set_name is ...
            else prefer(sticker_set_name(self.sticker_set_name), self.sticker_set_name),
            can_set_sticker_set=self.can_set_sticker_set
            if can_set_sticker_set is ...
            else prefer(
                can_set_sticker_set(self.can_set_sticker_set), self.can_set_sticker_set
            ),
            linked_chat_id=self.linked_chat_id
            if linked_chat_id is ...
            else prefer(linked_chat_id(self.linked_chat_id), self.linked_chat_id),
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
        )

    def copy_with(
        self,
        id: int | EllipsisType = ...,
        type: str | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        username: str | None | EllipsisType = ...,
        first_name: str | None | EllipsisType = ...,
        last_name: str | None | EllipsisType = ...,
        is_forum: bool | None | EllipsisType = ...,
        photo: ChatPhoto | None | EllipsisType = ...,
        active_usernames: list[str] | None | EllipsisType = ...,
        emoji_status_custom_emoji_id: str | None | EllipsisType = ...,
        emoji_status_expiration_date: int | None | EllipsisType = ...,
        bio: str | None | EllipsisType = ...,
        has_private_forwards: bool | None | EllipsisType = ...,
        has_restricted_voice_and_video_messages: bool | None | EllipsisType = ...,
        join_to_send_messages: bool | None | EllipsisType = ...,
        join_by_request: bool | None | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        invite_link: str | None | EllipsisType = ...,
        pinned_message: Message | None | EllipsisType = ...,
        permissions: ChatPermissions | None | EllipsisType = ...,
        slow_mode_delay: int | None | EllipsisType = ...,
        message_auto_delete_time: int | None | EllipsisType = ...,
        has_aggressive_anti_spam_enabled: bool | None | EllipsisType = ...,
        has_hidden_members: bool | None | EllipsisType = ...,
        has_protected_content: bool | None | EllipsisType = ...,
        sticker_set_name: str | None | EllipsisType = ...,
        can_set_sticker_set: bool | None | EllipsisType = ...,
        linked_chat_id: int | None | EllipsisType = ...,
        location: ChatLocation | None | EllipsisType = ...,
    ) -> Chat:
        """Replaces some of model's fields with provided ones"""
        return Chat(
            id=id if id is not ... else self.id,
            type=type if type is not ... else self.type,
            title=title if title is not ... else self.title,
            username=username if username is not ... else self.username,
            first_name=first_name if first_name is not ... else self.first_name,
            last_name=last_name if last_name is not ... else self.last_name,
            is_forum=is_forum if is_forum is not ... else self.is_forum,
            photo=photo if photo is not ... else self.photo,
            active_usernames=active_usernames
            if active_usernames is not ...
            else self.active_usernames,
            emoji_status_custom_emoji_id=emoji_status_custom_emoji_id
            if emoji_status_custom_emoji_id is not ...
            else self.emoji_status_custom_emoji_id,
            emoji_status_expiration_date=emoji_status_expiration_date
            if emoji_status_expiration_date is not ...
            else self.emoji_status_expiration_date,
            bio=bio if bio is not ... else self.bio,
            has_private_forwards=has_private_forwards
            if has_private_forwards is not ...
            else self.has_private_forwards,
            has_restricted_voice_and_video_messages=has_restricted_voice_and_video_messages
            if has_restricted_voice_and_video_messages is not ...
            else self.has_restricted_voice_and_video_messages,
            join_to_send_messages=join_to_send_messages
            if join_to_send_messages is not ...
            else self.join_to_send_messages,
            join_by_request=join_by_request
            if join_by_request is not ...
            else self.join_by_request,
            description=description if description is not ... else self.description,
            invite_link=invite_link if invite_link is not ... else self.invite_link,
            pinned_message=pinned_message
            if pinned_message is not ...
            else self.pinned_message,
            permissions=permissions if permissions is not ... else self.permissions,
            slow_mode_delay=slow_mode_delay
            if slow_mode_delay is not ...
            else self.slow_mode_delay,
            message_auto_delete_time=message_auto_delete_time
            if message_auto_delete_time is not ...
            else self.message_auto_delete_time,
            has_aggressive_anti_spam_enabled=has_aggressive_anti_spam_enabled
            if has_aggressive_anti_spam_enabled is not ...
            else self.has_aggressive_anti_spam_enabled,
            has_hidden_members=has_hidden_members
            if has_hidden_members is not ...
            else self.has_hidden_members,
            has_protected_content=has_protected_content
            if has_protected_content is not ...
            else self.has_protected_content,
            sticker_set_name=sticker_set_name
            if sticker_set_name is not ...
            else self.sticker_set_name,
            can_set_sticker_set=can_set_sticker_set
            if can_set_sticker_set is not ...
            else self.can_set_sticker_set,
            linked_chat_id=linked_chat_id
            if linked_chat_id is not ...
            else self.linked_chat_id,
            location=location if location is not ... else self.location,
        )


@dataclass(frozen=False, slots=True)
class Message:
    """This object represents a message."""

    message_id: int
    """Unique message identifier inside this chat """
    date: int
    """Date the message was sent in Unix time """
    chat: Chat
    """Conversation the message belongs to """
    message_thread_id: int | None = None
    """Optional. Unique identifier of a message thread to which the message belongs; for supergroups only """
    from_: User | None = None
    """Optional. Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat. """
    sender_chat: Chat | None = None
    """Optional. Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat. """
    forward_from: User | None = None
    """Optional. For forwarded messages, sender of the original message """
    forward_from_chat: Chat | None = None
    """Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat """
    forward_from_message_id: int | None = None
    """Optional. For messages forwarded from channels, identifier of the original message in the channel """
    forward_signature: str | None = None
    """Optional. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present """
    forward_sender_name: str | None = None
    """Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages """
    forward_date: int | None = None
    """Optional. For forwarded messages, date the original message was sent in Unix time """
    is_topic_message: bool | None = None
    """Optional. True, if the message is sent to a forum topic """
    is_automatic_forward: bool | None = None
    """Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group """
    reply_to_message: Message | None = None
    """Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply. """
    via_bot: User | None = None
    """Optional. Bot through which the message was sent """
    edit_date: int | None = None
    """Optional. Date the message was last edited in Unix time """
    has_protected_content: bool | None = None
    """Optional. True, if the message can't be forwarded """
    media_group_id: str | None = None
    """Optional. The unique identifier of a media message group this message belongs to """
    author_signature: str | None = None
    """Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator """
    text: str | None = None
    """Optional. For text messages, the actual UTF-8 text of the message """
    entities: list[MessageEntity] | None = None
    """Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text """
    animation: Animation | None = None
    """Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set """
    audio: Audio | None = None
    """Optional. Message is an audio file, information about the file """
    document: Document | None = None
    """Optional. Message is a general file, information about the file """
    photo: list[PhotoSize] | None = None
    """Optional. Message is a photo, available sizes of the photo """
    sticker: Sticker | None = None
    """Optional. Message is a sticker, information about the sticker """
    story: Story | None = None
    """Optional. Message is a forwarded story """
    video: Video | None = None
    """Optional. Message is a video, information about the video """
    video_note: VideoNote | None = None
    """Optional. Message is a video note, information about the video message """
    voice: Voice | None = None
    """Optional. Message is a voice message, information about the file """
    caption: str | None = None
    """Optional. Caption for the animation, audio, document, photo, video or voice """
    caption_entities: list[MessageEntity] | None = None
    """Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption """
    has_media_spoiler: bool | None = None
    """Optional. True, if the message media is covered by a spoiler animation """
    contact: Contact | None = None
    """Optional. Message is a shared contact, information about the contact """
    dice: Dice | None = None
    """Optional. Message is a dice with random value """
    game: Game | None = None
    """Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games """
    poll: Poll | None = None
    """Optional. Message is a native poll, information about the poll """
    venue: Venue | None = None
    """Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set """
    location: Location | None = None
    """Optional. Message is a shared location, information about the location """
    new_chat_members: list[User] | None = None
    """Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members) """
    left_chat_member: User | None = None
    """Optional. A member was removed from the group, information about them (this member may be the bot itself) """
    new_chat_title: str | None = None
    """Optional. A chat title was changed to this value """
    new_chat_photo: list[PhotoSize] | None = None
    """Optional. A chat photo was change to this value """
    delete_chat_photo: bool | None = None
    """Optional. Service message: the chat photo was deleted """
    group_chat_created: bool | None = None
    """Optional. Service message: the group has been created """
    supergroup_chat_created: bool | None = None
    """Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup. """
    channel_chat_created: bool | None = None
    """Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel. """
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None = None
    """Optional. Service message: auto-delete timer settings changed in the chat """
    migrate_to_chat_id: int | None = None
    """Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    migrate_from_chat_id: int | None = None
    """Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    pinned_message: Message | None = None
    """Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply. """
    invoice: Invoice | None = None
    """Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments """
    successful_payment: SuccessfulPayment | None = None
    """Optional. Message is a service message about a successful payment, information about the payment. More about payments: https://core.telegram.org/bots/api#payments """
    user_shared: UserShared | None = None
    """Optional. Service message: a user was shared with the bot """
    chat_shared: ChatShared | None = None
    """Optional. Service message: a chat was shared with the bot """
    connected_website: str | None = None
    """Optional. The domain name of the website on which the user has logged in. More about Telegram Login: https://core.telegram.org/widgets/login """
    write_access_allowed: WriteAccessAllowed | None = None
    """Optional. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess """
    passport_data: PassportData | None = None
    """Optional. Telegram Passport data """
    proximity_alert_triggered: ProximityAlertTriggered | None = None
    """Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location. """
    forum_topic_created: ForumTopicCreated | None = None
    """Optional. Service message: forum topic created """
    forum_topic_edited: ForumTopicEdited | None = None
    """Optional. Service message: forum topic edited """
    forum_topic_closed: ForumTopicClosed | None = None
    """Optional. Service message: forum topic closed """
    forum_topic_reopened: ForumTopicReopened | None = None
    """Optional. Service message: forum topic reopened """
    general_forum_topic_hidden: GeneralForumTopicHidden | None = None
    """Optional. Service message: the 'General' forum topic hidden """
    general_forum_topic_unhidden: GeneralForumTopicUnhidden | None = None
    """Optional. Service message: the 'General' forum topic unhidden """
    video_chat_scheduled: VideoChatScheduled | None = None
    """Optional. Service message: video chat scheduled """
    video_chat_started: VideoChatStarted | None = None
    """Optional. Service message: video chat started """
    video_chat_ended: VideoChatEnded | None = None
    """Optional. Service message: video chat ended """
    video_chat_participants_invited: VideoChatParticipantsInvited | None = None
    """Optional. Service message: new participants invited to a video chat """
    web_app_data: WebAppData | None = None
    """Optional. Service message: data sent by a Web App """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        message_id: AlterFn[int] | EllipsisType = ...,
        message_thread_id: AlterFn[int | None] | EllipsisType = ...,
        from_: AlterFn[User | None] | EllipsisType = ...,
        sender_chat: AlterFn[Chat | None] | EllipsisType = ...,
        date: AlterFn[int] | EllipsisType = ...,
        chat: AlterFn[Chat] | EllipsisType = ...,
        forward_from: AlterFn[User | None] | EllipsisType = ...,
        forward_from_chat: AlterFn[Chat | None] | EllipsisType = ...,
        forward_from_message_id: AlterFn[int | None] | EllipsisType = ...,
        forward_signature: AlterFn[str | None] | EllipsisType = ...,
        forward_sender_name: AlterFn[str | None] | EllipsisType = ...,
        forward_date: AlterFn[int | None] | EllipsisType = ...,
        is_topic_message: AlterFn[bool | None] | EllipsisType = ...,
        is_automatic_forward: AlterFn[bool | None] | EllipsisType = ...,
        reply_to_message: AlterFn[Message | None] | EllipsisType = ...,
        via_bot: AlterFn[User | None] | EllipsisType = ...,
        edit_date: AlterFn[int | None] | EllipsisType = ...,
        has_protected_content: AlterFn[bool | None] | EllipsisType = ...,
        media_group_id: AlterFn[str | None] | EllipsisType = ...,
        author_signature: AlterFn[str | None] | EllipsisType = ...,
        text: AlterFn[str | None] | EllipsisType = ...,
        entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        animation: AlterFn[Animation | None] | EllipsisType = ...,
        audio: AlterFn[Audio | None] | EllipsisType = ...,
        document: AlterFn[Document | None] | EllipsisType = ...,
        photo: AlterFn[list[PhotoSize] | None] | EllipsisType = ...,
        sticker: AlterFn[Sticker | None] | EllipsisType = ...,
        story: AlterFn[Story | None] | EllipsisType = ...,
        video: AlterFn[Video | None] | EllipsisType = ...,
        video_note: AlterFn[VideoNote | None] | EllipsisType = ...,
        voice: AlterFn[Voice | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        has_media_spoiler: AlterFn[bool | None] | EllipsisType = ...,
        contact: AlterFn[Contact | None] | EllipsisType = ...,
        dice: AlterFn[Dice | None] | EllipsisType = ...,
        game: AlterFn[Game | None] | EllipsisType = ...,
        poll: AlterFn[Poll | None] | EllipsisType = ...,
        venue: AlterFn[Venue | None] | EllipsisType = ...,
        location: AlterFn[Location | None] | EllipsisType = ...,
        new_chat_members: AlterFn[list[User] | None] | EllipsisType = ...,
        left_chat_member: AlterFn[User | None] | EllipsisType = ...,
        new_chat_title: AlterFn[str | None] | EllipsisType = ...,
        new_chat_photo: AlterFn[list[PhotoSize] | None] | EllipsisType = ...,
        delete_chat_photo: AlterFn[bool | None] | EllipsisType = ...,
        group_chat_created: AlterFn[bool | None] | EllipsisType = ...,
        supergroup_chat_created: AlterFn[bool | None] | EllipsisType = ...,
        channel_chat_created: AlterFn[bool | None] | EllipsisType = ...,
        message_auto_delete_timer_changed: AlterFn[MessageAutoDeleteTimerChanged | None]
        | EllipsisType = ...,
        migrate_to_chat_id: AlterFn[int | None] | EllipsisType = ...,
        migrate_from_chat_id: AlterFn[int | None] | EllipsisType = ...,
        pinned_message: AlterFn[Message | None] | EllipsisType = ...,
        invoice: AlterFn[Invoice | None] | EllipsisType = ...,
        successful_payment: AlterFn[SuccessfulPayment | None] | EllipsisType = ...,
        user_shared: AlterFn[UserShared | None] | EllipsisType = ...,
        chat_shared: AlterFn[ChatShared | None] | EllipsisType = ...,
        connected_website: AlterFn[str | None] | EllipsisType = ...,
        write_access_allowed: AlterFn[WriteAccessAllowed | None] | EllipsisType = ...,
        passport_data: AlterFn[PassportData | None] | EllipsisType = ...,
        proximity_alert_triggered: AlterFn[ProximityAlertTriggered | None]
        | EllipsisType = ...,
        forum_topic_created: AlterFn[ForumTopicCreated | None] | EllipsisType = ...,
        forum_topic_edited: AlterFn[ForumTopicEdited | None] | EllipsisType = ...,
        forum_topic_closed: AlterFn[ForumTopicClosed | None] | EllipsisType = ...,
        forum_topic_reopened: AlterFn[ForumTopicReopened | None] | EllipsisType = ...,
        general_forum_topic_hidden: AlterFn[GeneralForumTopicHidden | None]
        | EllipsisType = ...,
        general_forum_topic_unhidden: AlterFn[GeneralForumTopicUnhidden | None]
        | EllipsisType = ...,
        video_chat_scheduled: AlterFn[VideoChatScheduled | None] | EllipsisType = ...,
        video_chat_started: AlterFn[VideoChatStarted | None] | EllipsisType = ...,
        video_chat_ended: AlterFn[VideoChatEnded | None] | EllipsisType = ...,
        video_chat_participants_invited: AlterFn[VideoChatParticipantsInvited | None]
        | EllipsisType = ...,
        web_app_data: AlterFn[WebAppData | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
    ) -> Message:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Message(
            message_id=self.message_id
            if message_id is ...
            else prefer(message_id(self.message_id), self.message_id),
            message_thread_id=self.message_thread_id
            if message_thread_id is ...
            else prefer(
                message_thread_id(self.message_thread_id), self.message_thread_id
            ),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            sender_chat=self.sender_chat
            if sender_chat is ...
            else prefer(sender_chat(self.sender_chat), self.sender_chat),
            date=self.date if date is ... else prefer(date(self.date), self.date),
            chat=self.chat if chat is ... else prefer(chat(self.chat), self.chat),
            forward_from=self.forward_from
            if forward_from is ...
            else prefer(forward_from(self.forward_from), self.forward_from),
            forward_from_chat=self.forward_from_chat
            if forward_from_chat is ...
            else prefer(
                forward_from_chat(self.forward_from_chat), self.forward_from_chat
            ),
            forward_from_message_id=self.forward_from_message_id
            if forward_from_message_id is ...
            else prefer(
                forward_from_message_id(self.forward_from_message_id),
                self.forward_from_message_id,
            ),
            forward_signature=self.forward_signature
            if forward_signature is ...
            else prefer(
                forward_signature(self.forward_signature), self.forward_signature
            ),
            forward_sender_name=self.forward_sender_name
            if forward_sender_name is ...
            else prefer(
                forward_sender_name(self.forward_sender_name), self.forward_sender_name
            ),
            forward_date=self.forward_date
            if forward_date is ...
            else prefer(forward_date(self.forward_date), self.forward_date),
            is_topic_message=self.is_topic_message
            if is_topic_message is ...
            else prefer(is_topic_message(self.is_topic_message), self.is_topic_message),
            is_automatic_forward=self.is_automatic_forward
            if is_automatic_forward is ...
            else prefer(
                is_automatic_forward(self.is_automatic_forward),
                self.is_automatic_forward,
            ),
            reply_to_message=self.reply_to_message
            if reply_to_message is ...
            else prefer(reply_to_message(self.reply_to_message), self.reply_to_message),
            via_bot=self.via_bot
            if via_bot is ...
            else prefer(via_bot(self.via_bot), self.via_bot),
            edit_date=self.edit_date
            if edit_date is ...
            else prefer(edit_date(self.edit_date), self.edit_date),
            has_protected_content=self.has_protected_content
            if has_protected_content is ...
            else prefer(
                has_protected_content(self.has_protected_content),
                self.has_protected_content,
            ),
            media_group_id=self.media_group_id
            if media_group_id is ...
            else prefer(media_group_id(self.media_group_id), self.media_group_id),
            author_signature=self.author_signature
            if author_signature is ...
            else prefer(author_signature(self.author_signature), self.author_signature),
            text=self.text if text is ... else prefer(text(self.text), self.text),
            entities=self.entities
            if entities is ...
            else prefer(entities(self.entities), self.entities),
            animation=self.animation
            if animation is ...
            else prefer(animation(self.animation), self.animation),
            audio=self.audio if audio is ... else prefer(audio(self.audio), self.audio),
            document=self.document
            if document is ...
            else prefer(document(self.document), self.document),
            photo=self.photo if photo is ... else prefer(photo(self.photo), self.photo),
            sticker=self.sticker
            if sticker is ...
            else prefer(sticker(self.sticker), self.sticker),
            story=self.story if story is ... else prefer(story(self.story), self.story),
            video=self.video if video is ... else prefer(video(self.video), self.video),
            video_note=self.video_note
            if video_note is ...
            else prefer(video_note(self.video_note), self.video_note),
            voice=self.voice if voice is ... else prefer(voice(self.voice), self.voice),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            has_media_spoiler=self.has_media_spoiler
            if has_media_spoiler is ...
            else prefer(
                has_media_spoiler(self.has_media_spoiler), self.has_media_spoiler
            ),
            contact=self.contact
            if contact is ...
            else prefer(contact(self.contact), self.contact),
            dice=self.dice if dice is ... else prefer(dice(self.dice), self.dice),
            game=self.game if game is ... else prefer(game(self.game), self.game),
            poll=self.poll if poll is ... else prefer(poll(self.poll), self.poll),
            venue=self.venue if venue is ... else prefer(venue(self.venue), self.venue),
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
            new_chat_members=self.new_chat_members
            if new_chat_members is ...
            else prefer(new_chat_members(self.new_chat_members), self.new_chat_members),
            left_chat_member=self.left_chat_member
            if left_chat_member is ...
            else prefer(left_chat_member(self.left_chat_member), self.left_chat_member),
            new_chat_title=self.new_chat_title
            if new_chat_title is ...
            else prefer(new_chat_title(self.new_chat_title), self.new_chat_title),
            new_chat_photo=self.new_chat_photo
            if new_chat_photo is ...
            else prefer(new_chat_photo(self.new_chat_photo), self.new_chat_photo),
            delete_chat_photo=self.delete_chat_photo
            if delete_chat_photo is ...
            else prefer(
                delete_chat_photo(self.delete_chat_photo), self.delete_chat_photo
            ),
            group_chat_created=self.group_chat_created
            if group_chat_created is ...
            else prefer(
                group_chat_created(self.group_chat_created), self.group_chat_created
            ),
            supergroup_chat_created=self.supergroup_chat_created
            if supergroup_chat_created is ...
            else prefer(
                supergroup_chat_created(self.supergroup_chat_created),
                self.supergroup_chat_created,
            ),
            channel_chat_created=self.channel_chat_created
            if channel_chat_created is ...
            else prefer(
                channel_chat_created(self.channel_chat_created),
                self.channel_chat_created,
            ),
            message_auto_delete_timer_changed=self.message_auto_delete_timer_changed
            if message_auto_delete_timer_changed is ...
            else prefer(
                message_auto_delete_timer_changed(
                    self.message_auto_delete_timer_changed
                ),
                self.message_auto_delete_timer_changed,
            ),
            migrate_to_chat_id=self.migrate_to_chat_id
            if migrate_to_chat_id is ...
            else prefer(
                migrate_to_chat_id(self.migrate_to_chat_id), self.migrate_to_chat_id
            ),
            migrate_from_chat_id=self.migrate_from_chat_id
            if migrate_from_chat_id is ...
            else prefer(
                migrate_from_chat_id(self.migrate_from_chat_id),
                self.migrate_from_chat_id,
            ),
            pinned_message=self.pinned_message
            if pinned_message is ...
            else prefer(pinned_message(self.pinned_message), self.pinned_message),
            invoice=self.invoice
            if invoice is ...
            else prefer(invoice(self.invoice), self.invoice),
            successful_payment=self.successful_payment
            if successful_payment is ...
            else prefer(
                successful_payment(self.successful_payment), self.successful_payment
            ),
            user_shared=self.user_shared
            if user_shared is ...
            else prefer(user_shared(self.user_shared), self.user_shared),
            chat_shared=self.chat_shared
            if chat_shared is ...
            else prefer(chat_shared(self.chat_shared), self.chat_shared),
            connected_website=self.connected_website
            if connected_website is ...
            else prefer(
                connected_website(self.connected_website), self.connected_website
            ),
            write_access_allowed=self.write_access_allowed
            if write_access_allowed is ...
            else prefer(
                write_access_allowed(self.write_access_allowed),
                self.write_access_allowed,
            ),
            passport_data=self.passport_data
            if passport_data is ...
            else prefer(passport_data(self.passport_data), self.passport_data),
            proximity_alert_triggered=self.proximity_alert_triggered
            if proximity_alert_triggered is ...
            else prefer(
                proximity_alert_triggered(self.proximity_alert_triggered),
                self.proximity_alert_triggered,
            ),
            forum_topic_created=self.forum_topic_created
            if forum_topic_created is ...
            else prefer(
                forum_topic_created(self.forum_topic_created), self.forum_topic_created
            ),
            forum_topic_edited=self.forum_topic_edited
            if forum_topic_edited is ...
            else prefer(
                forum_topic_edited(self.forum_topic_edited), self.forum_topic_edited
            ),
            forum_topic_closed=self.forum_topic_closed
            if forum_topic_closed is ...
            else prefer(
                forum_topic_closed(self.forum_topic_closed), self.forum_topic_closed
            ),
            forum_topic_reopened=self.forum_topic_reopened
            if forum_topic_reopened is ...
            else prefer(
                forum_topic_reopened(self.forum_topic_reopened),
                self.forum_topic_reopened,
            ),
            general_forum_topic_hidden=self.general_forum_topic_hidden
            if general_forum_topic_hidden is ...
            else prefer(
                general_forum_topic_hidden(self.general_forum_topic_hidden),
                self.general_forum_topic_hidden,
            ),
            general_forum_topic_unhidden=self.general_forum_topic_unhidden
            if general_forum_topic_unhidden is ...
            else prefer(
                general_forum_topic_unhidden(self.general_forum_topic_unhidden),
                self.general_forum_topic_unhidden,
            ),
            video_chat_scheduled=self.video_chat_scheduled
            if video_chat_scheduled is ...
            else prefer(
                video_chat_scheduled(self.video_chat_scheduled),
                self.video_chat_scheduled,
            ),
            video_chat_started=self.video_chat_started
            if video_chat_started is ...
            else prefer(
                video_chat_started(self.video_chat_started), self.video_chat_started
            ),
            video_chat_ended=self.video_chat_ended
            if video_chat_ended is ...
            else prefer(video_chat_ended(self.video_chat_ended), self.video_chat_ended),
            video_chat_participants_invited=self.video_chat_participants_invited
            if video_chat_participants_invited is ...
            else prefer(
                video_chat_participants_invited(self.video_chat_participants_invited),
                self.video_chat_participants_invited,
            ),
            web_app_data=self.web_app_data
            if web_app_data is ...
            else prefer(web_app_data(self.web_app_data), self.web_app_data),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
        )

    def copy_with(
        self,
        message_id: int | EllipsisType = ...,
        message_thread_id: int | None | EllipsisType = ...,
        from_: User | None | EllipsisType = ...,
        sender_chat: Chat | None | EllipsisType = ...,
        date: int | EllipsisType = ...,
        chat: Chat | EllipsisType = ...,
        forward_from: User | None | EllipsisType = ...,
        forward_from_chat: Chat | None | EllipsisType = ...,
        forward_from_message_id: int | None | EllipsisType = ...,
        forward_signature: str | None | EllipsisType = ...,
        forward_sender_name: str | None | EllipsisType = ...,
        forward_date: int | None | EllipsisType = ...,
        is_topic_message: bool | None | EllipsisType = ...,
        is_automatic_forward: bool | None | EllipsisType = ...,
        reply_to_message: Message | None | EllipsisType = ...,
        via_bot: User | None | EllipsisType = ...,
        edit_date: int | None | EllipsisType = ...,
        has_protected_content: bool | None | EllipsisType = ...,
        media_group_id: str | None | EllipsisType = ...,
        author_signature: str | None | EllipsisType = ...,
        text: str | None | EllipsisType = ...,
        entities: list[MessageEntity] | None | EllipsisType = ...,
        animation: Animation | None | EllipsisType = ...,
        audio: Audio | None | EllipsisType = ...,
        document: Document | None | EllipsisType = ...,
        photo: list[PhotoSize] | None | EllipsisType = ...,
        sticker: Sticker | None | EllipsisType = ...,
        story: Story | None | EllipsisType = ...,
        video: Video | None | EllipsisType = ...,
        video_note: VideoNote | None | EllipsisType = ...,
        voice: Voice | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        has_media_spoiler: bool | None | EllipsisType = ...,
        contact: Contact | None | EllipsisType = ...,
        dice: Dice | None | EllipsisType = ...,
        game: Game | None | EllipsisType = ...,
        poll: Poll | None | EllipsisType = ...,
        venue: Venue | None | EllipsisType = ...,
        location: Location | None | EllipsisType = ...,
        new_chat_members: list[User] | None | EllipsisType = ...,
        left_chat_member: User | None | EllipsisType = ...,
        new_chat_title: str | None | EllipsisType = ...,
        new_chat_photo: list[PhotoSize] | None | EllipsisType = ...,
        delete_chat_photo: bool | None | EllipsisType = ...,
        group_chat_created: bool | None | EllipsisType = ...,
        supergroup_chat_created: bool | None | EllipsisType = ...,
        channel_chat_created: bool | None | EllipsisType = ...,
        message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
        | None
        | EllipsisType = ...,
        migrate_to_chat_id: int | None | EllipsisType = ...,
        migrate_from_chat_id: int | None | EllipsisType = ...,
        pinned_message: Message | None | EllipsisType = ...,
        invoice: Invoice | None | EllipsisType = ...,
        successful_payment: SuccessfulPayment | None | EllipsisType = ...,
        user_shared: UserShared | None | EllipsisType = ...,
        chat_shared: ChatShared | None | EllipsisType = ...,
        connected_website: str | None | EllipsisType = ...,
        write_access_allowed: WriteAccessAllowed | None | EllipsisType = ...,
        passport_data: PassportData | None | EllipsisType = ...,
        proximity_alert_triggered: ProximityAlertTriggered | None | EllipsisType = ...,
        forum_topic_created: ForumTopicCreated | None | EllipsisType = ...,
        forum_topic_edited: ForumTopicEdited | None | EllipsisType = ...,
        forum_topic_closed: ForumTopicClosed | None | EllipsisType = ...,
        forum_topic_reopened: ForumTopicReopened | None | EllipsisType = ...,
        general_forum_topic_hidden: GeneralForumTopicHidden | None | EllipsisType = ...,
        general_forum_topic_unhidden: GeneralForumTopicUnhidden
        | None
        | EllipsisType = ...,
        video_chat_scheduled: VideoChatScheduled | None | EllipsisType = ...,
        video_chat_started: VideoChatStarted | None | EllipsisType = ...,
        video_chat_ended: VideoChatEnded | None | EllipsisType = ...,
        video_chat_participants_invited: VideoChatParticipantsInvited
        | None
        | EllipsisType = ...,
        web_app_data: WebAppData | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
    ) -> Message:
        """Replaces some of model's fields with provided ones"""
        return Message(
            message_id=message_id if message_id is not ... else self.message_id,
            message_thread_id=message_thread_id
            if message_thread_id is not ...
            else self.message_thread_id,
            from_=from_ if from_ is not ... else self.from_,
            sender_chat=sender_chat if sender_chat is not ... else self.sender_chat,
            date=date if date is not ... else self.date,
            chat=chat if chat is not ... else self.chat,
            forward_from=forward_from if forward_from is not ... else self.forward_from,
            forward_from_chat=forward_from_chat
            if forward_from_chat is not ...
            else self.forward_from_chat,
            forward_from_message_id=forward_from_message_id
            if forward_from_message_id is not ...
            else self.forward_from_message_id,
            forward_signature=forward_signature
            if forward_signature is not ...
            else self.forward_signature,
            forward_sender_name=forward_sender_name
            if forward_sender_name is not ...
            else self.forward_sender_name,
            forward_date=forward_date if forward_date is not ... else self.forward_date,
            is_topic_message=is_topic_message
            if is_topic_message is not ...
            else self.is_topic_message,
            is_automatic_forward=is_automatic_forward
            if is_automatic_forward is not ...
            else self.is_automatic_forward,
            reply_to_message=reply_to_message
            if reply_to_message is not ...
            else self.reply_to_message,
            via_bot=via_bot if via_bot is not ... else self.via_bot,
            edit_date=edit_date if edit_date is not ... else self.edit_date,
            has_protected_content=has_protected_content
            if has_protected_content is not ...
            else self.has_protected_content,
            media_group_id=media_group_id
            if media_group_id is not ...
            else self.media_group_id,
            author_signature=author_signature
            if author_signature is not ...
            else self.author_signature,
            text=text if text is not ... else self.text,
            entities=entities if entities is not ... else self.entities,
            animation=animation if animation is not ... else self.animation,
            audio=audio if audio is not ... else self.audio,
            document=document if document is not ... else self.document,
            photo=photo if photo is not ... else self.photo,
            sticker=sticker if sticker is not ... else self.sticker,
            story=story if story is not ... else self.story,
            video=video if video is not ... else self.video,
            video_note=video_note if video_note is not ... else self.video_note,
            voice=voice if voice is not ... else self.voice,
            caption=caption if caption is not ... else self.caption,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            has_media_spoiler=has_media_spoiler
            if has_media_spoiler is not ...
            else self.has_media_spoiler,
            contact=contact if contact is not ... else self.contact,
            dice=dice if dice is not ... else self.dice,
            game=game if game is not ... else self.game,
            poll=poll if poll is not ... else self.poll,
            venue=venue if venue is not ... else self.venue,
            location=location if location is not ... else self.location,
            new_chat_members=new_chat_members
            if new_chat_members is not ...
            else self.new_chat_members,
            left_chat_member=left_chat_member
            if left_chat_member is not ...
            else self.left_chat_member,
            new_chat_title=new_chat_title
            if new_chat_title is not ...
            else self.new_chat_title,
            new_chat_photo=new_chat_photo
            if new_chat_photo is not ...
            else self.new_chat_photo,
            delete_chat_photo=delete_chat_photo
            if delete_chat_photo is not ...
            else self.delete_chat_photo,
            group_chat_created=group_chat_created
            if group_chat_created is not ...
            else self.group_chat_created,
            supergroup_chat_created=supergroup_chat_created
            if supergroup_chat_created is not ...
            else self.supergroup_chat_created,
            channel_chat_created=channel_chat_created
            if channel_chat_created is not ...
            else self.channel_chat_created,
            message_auto_delete_timer_changed=message_auto_delete_timer_changed
            if message_auto_delete_timer_changed is not ...
            else self.message_auto_delete_timer_changed,
            migrate_to_chat_id=migrate_to_chat_id
            if migrate_to_chat_id is not ...
            else self.migrate_to_chat_id,
            migrate_from_chat_id=migrate_from_chat_id
            if migrate_from_chat_id is not ...
            else self.migrate_from_chat_id,
            pinned_message=pinned_message
            if pinned_message is not ...
            else self.pinned_message,
            invoice=invoice if invoice is not ... else self.invoice,
            successful_payment=successful_payment
            if successful_payment is not ...
            else self.successful_payment,
            user_shared=user_shared if user_shared is not ... else self.user_shared,
            chat_shared=chat_shared if chat_shared is not ... else self.chat_shared,
            connected_website=connected_website
            if connected_website is not ...
            else self.connected_website,
            write_access_allowed=write_access_allowed
            if write_access_allowed is not ...
            else self.write_access_allowed,
            passport_data=passport_data
            if passport_data is not ...
            else self.passport_data,
            proximity_alert_triggered=proximity_alert_triggered
            if proximity_alert_triggered is not ...
            else self.proximity_alert_triggered,
            forum_topic_created=forum_topic_created
            if forum_topic_created is not ...
            else self.forum_topic_created,
            forum_topic_edited=forum_topic_edited
            if forum_topic_edited is not ...
            else self.forum_topic_edited,
            forum_topic_closed=forum_topic_closed
            if forum_topic_closed is not ...
            else self.forum_topic_closed,
            forum_topic_reopened=forum_topic_reopened
            if forum_topic_reopened is not ...
            else self.forum_topic_reopened,
            general_forum_topic_hidden=general_forum_topic_hidden
            if general_forum_topic_hidden is not ...
            else self.general_forum_topic_hidden,
            general_forum_topic_unhidden=general_forum_topic_unhidden
            if general_forum_topic_unhidden is not ...
            else self.general_forum_topic_unhidden,
            video_chat_scheduled=video_chat_scheduled
            if video_chat_scheduled is not ...
            else self.video_chat_scheduled,
            video_chat_started=video_chat_started
            if video_chat_started is not ...
            else self.video_chat_started,
            video_chat_ended=video_chat_ended
            if video_chat_ended is not ...
            else self.video_chat_ended,
            video_chat_participants_invited=video_chat_participants_invited
            if video_chat_participants_invited is not ...
            else self.video_chat_participants_invited,
            web_app_data=web_app_data if web_app_data is not ... else self.web_app_data,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
        )


@dataclass(frozen=False, slots=True)
class MessageId:
    """This object represents a unique message identifier."""

    message_id: int
    """Unique message identifier """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        message_id: AlterFn[int] | EllipsisType = ...,
    ) -> MessageId:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MessageId(
            message_id=self.message_id
            if message_id is ...
            else prefer(message_id(self.message_id), self.message_id)
        )

    def copy_with(
        self,
        message_id: int | EllipsisType = ...,
    ) -> MessageId:
        """Replaces some of model's fields with provided ones"""
        return MessageId(
            message_id=message_id if message_id is not ... else self.message_id
        )


@dataclass(frozen=False, slots=True)
class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc."""

    type: str
    """Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames), "custom_emoji" (for inline custom emoji stickers) """
    offset: int
    """Offset in UTF-16 code units to the start of the entity """
    length: int
    """Length of the entity in UTF-16 code units """
    url: str | None = None
    """Optional. For "text_link" only, URL that will be opened after user taps on the text """
    user: User | None = None
    """Optional. For "text_mention" only, the mentioned user """
    language: str | None = None
    """Optional. For "pre" only, the programming language of the entity text """
    custom_emoji_id: str | None = None
    """Optional. For "custom_emoji" only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        offset: AlterFn[int] | EllipsisType = ...,
        length: AlterFn[int] | EllipsisType = ...,
        url: AlterFn[str | None] | EllipsisType = ...,
        user: AlterFn[User | None] | EllipsisType = ...,
        language: AlterFn[str | None] | EllipsisType = ...,
        custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
    ) -> MessageEntity:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MessageEntity(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            offset=self.offset
            if offset is ...
            else prefer(offset(self.offset), self.offset),
            length=self.length
            if length is ...
            else prefer(length(self.length), self.length),
            url=self.url if url is ... else prefer(url(self.url), self.url),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            language=self.language
            if language is ...
            else prefer(language(self.language), self.language),
            custom_emoji_id=self.custom_emoji_id
            if custom_emoji_id is ...
            else prefer(custom_emoji_id(self.custom_emoji_id), self.custom_emoji_id),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        offset: int | EllipsisType = ...,
        length: int | EllipsisType = ...,
        url: str | None | EllipsisType = ...,
        user: User | None | EllipsisType = ...,
        language: str | None | EllipsisType = ...,
        custom_emoji_id: str | None | EllipsisType = ...,
    ) -> MessageEntity:
        """Replaces some of model's fields with provided ones"""
        return MessageEntity(
            type=type if type is not ... else self.type,
            offset=offset if offset is not ... else self.offset,
            length=length if length is not ... else self.length,
            url=url if url is not ... else self.url,
            user=user if user is not ... else self.user,
            language=language if language is not ... else self.language,
            custom_emoji_id=custom_emoji_id
            if custom_emoji_id is not ...
            else self.custom_emoji_id,
        )


@dataclass(frozen=False, slots=True)
class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    width: int
    """Photo width """
    height: int
    """Photo height """
    file_size: int | None = None
    """Optional. File size in bytes """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        width: AlterFn[int] | EllipsisType = ...,
        height: AlterFn[int] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> PhotoSize:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PhotoSize(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        width: int | EllipsisType = ...,
        height: int | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> PhotoSize:
        """Replaces some of model's fields with provided ones"""
        return PhotoSize(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    width: int
    """Video width as defined by sender """
    height: int
    """Video height as defined by sender """
    duration: int
    """Duration of the video in seconds as defined by sender """
    thumbnail: PhotoSize | None = None
    """Optional. Animation thumbnail as defined by sender """
    file_name: str | None = None
    """Optional. Original animation filename as defined by sender """
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        width: AlterFn[int] | EllipsisType = ...,
        height: AlterFn[int] | EllipsisType = ...,
        duration: AlterFn[int] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
        file_name: AlterFn[str | None] | EllipsisType = ...,
        mime_type: AlterFn[str | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> Animation:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Animation(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            file_name=self.file_name
            if file_name is ...
            else prefer(file_name(self.file_name), self.file_name),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        width: int | EllipsisType = ...,
        height: int | EllipsisType = ...,
        duration: int | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
        file_name: str | None | EllipsisType = ...,
        mime_type: str | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> Animation:
        """Replaces some of model's fields with provided ones"""
        return Animation(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            duration=duration if duration is not ... else self.duration,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            file_name=file_name if file_name is not ... else self.file_name,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    duration: int
    """Duration of the audio in seconds as defined by sender """
    performer: str | None = None
    """Optional. Performer of the audio as defined by sender or by audio tags """
    title: str | None = None
    """Optional. Title of the audio as defined by sender or by audio tags """
    file_name: str | None = None
    """Optional. Original filename as defined by sender """
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """
    thumbnail: PhotoSize | None = None
    """Optional. Thumbnail of the album cover to which the music file belongs """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        duration: AlterFn[int] | EllipsisType = ...,
        performer: AlterFn[str | None] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        file_name: AlterFn[str | None] | EllipsisType = ...,
        mime_type: AlterFn[str | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
    ) -> Audio:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Audio(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            performer=self.performer
            if performer is ...
            else prefer(performer(self.performer), self.performer),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            file_name=self.file_name
            if file_name is ...
            else prefer(file_name(self.file_name), self.file_name),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        duration: int | EllipsisType = ...,
        performer: str | None | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        file_name: str | None | EllipsisType = ...,
        mime_type: str | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
    ) -> Audio:
        """Replaces some of model's fields with provided ones"""
        return Audio(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            duration=duration if duration is not ... else self.duration,
            performer=performer if performer is not ... else self.performer,
            title=title if title is not ... else self.title,
            file_name=file_name if file_name is not ... else self.file_name,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            file_size=file_size if file_size is not ... else self.file_size,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
        )


@dataclass(frozen=False, slots=True)
class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    thumbnail: PhotoSize | None = None
    """Optional. Document thumbnail as defined by sender """
    file_name: str | None = None
    """Optional. Original filename as defined by sender """
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
        file_name: AlterFn[str | None] | EllipsisType = ...,
        mime_type: AlterFn[str | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> Document:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Document(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            file_name=self.file_name
            if file_name is ...
            else prefer(file_name(self.file_name), self.file_name),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
        file_name: str | None | EllipsisType = ...,
        mime_type: str | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> Document:
        """Replaces some of model's fields with provided ones"""
        return Document(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            file_name=file_name if file_name is not ... else self.file_name,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class Story:
    """This object represents a message about a forwarded story in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> Story:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Story()

    def copy_with(
        self,
    ) -> Story:
        """Replaces some of model's fields with provided ones"""
        return Story()


@dataclass(frozen=False, slots=True)
class Video:
    """This object represents a video file."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    width: int
    """Video width as defined by sender """
    height: int
    """Video height as defined by sender """
    duration: int
    """Duration of the video in seconds as defined by sender """
    thumbnail: PhotoSize | None = None
    """Optional. Video thumbnail """
    file_name: str | None = None
    """Optional. Original filename as defined by sender """
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        width: AlterFn[int] | EllipsisType = ...,
        height: AlterFn[int] | EllipsisType = ...,
        duration: AlterFn[int] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
        file_name: AlterFn[str | None] | EllipsisType = ...,
        mime_type: AlterFn[str | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> Video:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Video(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            file_name=self.file_name
            if file_name is ...
            else prefer(file_name(self.file_name), self.file_name),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        width: int | EllipsisType = ...,
        height: int | EllipsisType = ...,
        duration: int | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
        file_name: str | None | EllipsisType = ...,
        mime_type: str | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> Video:
        """Replaces some of model's fields with provided ones"""
        return Video(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            duration=duration if duration is not ... else self.duration,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            file_name=file_name if file_name is not ... else self.file_name,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0)."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    length: int
    """Video width and height (diameter of the video message) as defined by sender """
    duration: int
    """Duration of the video in seconds as defined by sender """
    thumbnail: PhotoSize | None = None
    """Optional. Video thumbnail """
    file_size: int | None = None
    """Optional. File size in bytes """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        length: AlterFn[int] | EllipsisType = ...,
        duration: AlterFn[int] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> VideoNote:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return VideoNote(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            length=self.length
            if length is ...
            else prefer(length(self.length), self.length),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        length: int | EllipsisType = ...,
        duration: int | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> VideoNote:
        """Replaces some of model's fields with provided ones"""
        return VideoNote(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            length=length if length is not ... else self.length,
            duration=duration if duration is not ... else self.duration,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class Voice:
    """This object represents a voice note."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    duration: int
    """Duration of the audio in seconds as defined by sender """
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        duration: AlterFn[int] | EllipsisType = ...,
        mime_type: AlterFn[str | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> Voice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Voice(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        duration: int | EllipsisType = ...,
        mime_type: str | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> Voice:
        """Replaces some of model's fields with provided ones"""
        return Voice(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            duration=duration if duration is not ... else self.duration,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class Contact:
    """This object represents a phone contact."""

    phone_number: str
    """Contact's phone number """
    first_name: str
    """Contact's first name """
    last_name: str | None = None
    """Optional. Contact's last name """
    user_id: int | None = None
    """Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. """
    vcard: str | None = None
    """Optional. Additional data about the contact in the form of a vCard """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        phone_number: AlterFn[str] | EllipsisType = ...,
        first_name: AlterFn[str] | EllipsisType = ...,
        last_name: AlterFn[str | None] | EllipsisType = ...,
        user_id: AlterFn[int | None] | EllipsisType = ...,
        vcard: AlterFn[str | None] | EllipsisType = ...,
    ) -> Contact:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Contact(
            phone_number=self.phone_number
            if phone_number is ...
            else prefer(phone_number(self.phone_number), self.phone_number),
            first_name=self.first_name
            if first_name is ...
            else prefer(first_name(self.first_name), self.first_name),
            last_name=self.last_name
            if last_name is ...
            else prefer(last_name(self.last_name), self.last_name),
            user_id=self.user_id
            if user_id is ...
            else prefer(user_id(self.user_id), self.user_id),
            vcard=self.vcard if vcard is ... else prefer(vcard(self.vcard), self.vcard),
        )

    def copy_with(
        self,
        phone_number: str | EllipsisType = ...,
        first_name: str | EllipsisType = ...,
        last_name: str | None | EllipsisType = ...,
        user_id: int | None | EllipsisType = ...,
        vcard: str | None | EllipsisType = ...,
    ) -> Contact:
        """Replaces some of model's fields with provided ones"""
        return Contact(
            phone_number=phone_number if phone_number is not ... else self.phone_number,
            first_name=first_name if first_name is not ... else self.first_name,
            last_name=last_name if last_name is not ... else self.last_name,
            user_id=user_id if user_id is not ... else self.user_id,
            vcard=vcard if vcard is not ... else self.vcard,
        )


@dataclass(frozen=False, slots=True)
class Dice:
    """This object represents an animated emoji that displays a random value."""

    emoji: str
    """Emoji on which the dice throw animation is based """
    value: int
    """Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        emoji: AlterFn[str] | EllipsisType = ...,
        value: AlterFn[int] | EllipsisType = ...,
    ) -> Dice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Dice(
            emoji=self.emoji if emoji is ... else prefer(emoji(self.emoji), self.emoji),
            value=self.value if value is ... else prefer(value(self.value), self.value),
        )

    def copy_with(
        self,
        emoji: str | EllipsisType = ...,
        value: int | EllipsisType = ...,
    ) -> Dice:
        """Replaces some of model's fields with provided ones"""
        return Dice(
            emoji=emoji if emoji is not ... else self.emoji,
            value=value if value is not ... else self.value,
        )


@dataclass(frozen=False, slots=True)
class PollOption:
    """This object contains information about one answer option in a poll."""

    text: str
    """Option text, 1-100 characters """
    voter_count: int
    """Number of users that voted for this option """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        text: AlterFn[str] | EllipsisType = ...,
        voter_count: AlterFn[int] | EllipsisType = ...,
    ) -> PollOption:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PollOption(
            text=self.text if text is ... else prefer(text(self.text), self.text),
            voter_count=self.voter_count
            if voter_count is ...
            else prefer(voter_count(self.voter_count), self.voter_count),
        )

    def copy_with(
        self,
        text: str | EllipsisType = ...,
        voter_count: int | EllipsisType = ...,
    ) -> PollOption:
        """Replaces some of model's fields with provided ones"""
        return PollOption(
            text=text if text is not ... else self.text,
            voter_count=voter_count if voter_count is not ... else self.voter_count,
        )


@dataclass(frozen=False, slots=True)
class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll."""

    poll_id: str
    """Unique poll identifier """
    option_ids: list[int]
    """0-based identifiers of chosen answer options. May be empty if the vote was retracted. """
    voter_chat: Chat | None = None
    """Optional. The chat that changed the answer to the poll, if the voter is anonymous """
    user: User | None = None
    """Optional. The user that changed the answer to the poll, if the voter isn't anonymous """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        poll_id: AlterFn[str] | EllipsisType = ...,
        voter_chat: AlterFn[Chat | None] | EllipsisType = ...,
        user: AlterFn[User | None] | EllipsisType = ...,
        option_ids: AlterFn[list[int]] | EllipsisType = ...,
    ) -> PollAnswer:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PollAnswer(
            poll_id=self.poll_id
            if poll_id is ...
            else prefer(poll_id(self.poll_id), self.poll_id),
            voter_chat=self.voter_chat
            if voter_chat is ...
            else prefer(voter_chat(self.voter_chat), self.voter_chat),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            option_ids=self.option_ids
            if option_ids is ...
            else prefer(option_ids(self.option_ids), self.option_ids),
        )

    def copy_with(
        self,
        poll_id: str | EllipsisType = ...,
        voter_chat: Chat | None | EllipsisType = ...,
        user: User | None | EllipsisType = ...,
        option_ids: list[int] | EllipsisType = ...,
    ) -> PollAnswer:
        """Replaces some of model's fields with provided ones"""
        return PollAnswer(
            poll_id=poll_id if poll_id is not ... else self.poll_id,
            voter_chat=voter_chat if voter_chat is not ... else self.voter_chat,
            user=user if user is not ... else self.user,
            option_ids=option_ids if option_ids is not ... else self.option_ids,
        )


@dataclass(frozen=False, slots=True)
class Poll:
    """This object contains information about a poll."""

    id: str
    """Unique poll identifier """
    question: str
    """Poll question, 1-300 characters """
    options: list[PollOption]
    """List of poll options """
    total_voter_count: int
    """Total number of users that voted in the poll """
    is_closed: bool
    """True, if the poll is closed """
    is_anonymous: bool
    """True, if the poll is anonymous """
    type: str
    """Poll type, currently can be "regular" or "quiz" """
    allows_multiple_answers: bool
    """True, if the poll allows multiple answers """
    correct_option_id: int | None = None
    """Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot. """
    explanation: str | None = None
    """Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters """
    explanation_entities: list[MessageEntity] | None = None
    """Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation """
    open_period: int | None = None
    """Optional. Amount of time in seconds the poll will be active after creation """
    close_date: int | None = None
    """Optional. Point in time (Unix timestamp) when the poll will be automatically closed """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        question: AlterFn[str] | EllipsisType = ...,
        options: AlterFn[list[PollOption]] | EllipsisType = ...,
        total_voter_count: AlterFn[int] | EllipsisType = ...,
        is_closed: AlterFn[bool] | EllipsisType = ...,
        is_anonymous: AlterFn[bool] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        allows_multiple_answers: AlterFn[bool] | EllipsisType = ...,
        correct_option_id: AlterFn[int | None] | EllipsisType = ...,
        explanation: AlterFn[str | None] | EllipsisType = ...,
        explanation_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        open_period: AlterFn[int | None] | EllipsisType = ...,
        close_date: AlterFn[int | None] | EllipsisType = ...,
    ) -> Poll:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Poll(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            question=self.question
            if question is ...
            else prefer(question(self.question), self.question),
            options=self.options
            if options is ...
            else prefer(options(self.options), self.options),
            total_voter_count=self.total_voter_count
            if total_voter_count is ...
            else prefer(
                total_voter_count(self.total_voter_count), self.total_voter_count
            ),
            is_closed=self.is_closed
            if is_closed is ...
            else prefer(is_closed(self.is_closed), self.is_closed),
            is_anonymous=self.is_anonymous
            if is_anonymous is ...
            else prefer(is_anonymous(self.is_anonymous), self.is_anonymous),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            allows_multiple_answers=self.allows_multiple_answers
            if allows_multiple_answers is ...
            else prefer(
                allows_multiple_answers(self.allows_multiple_answers),
                self.allows_multiple_answers,
            ),
            correct_option_id=self.correct_option_id
            if correct_option_id is ...
            else prefer(
                correct_option_id(self.correct_option_id), self.correct_option_id
            ),
            explanation=self.explanation
            if explanation is ...
            else prefer(explanation(self.explanation), self.explanation),
            explanation_entities=self.explanation_entities
            if explanation_entities is ...
            else prefer(
                explanation_entities(self.explanation_entities),
                self.explanation_entities,
            ),
            open_period=self.open_period
            if open_period is ...
            else prefer(open_period(self.open_period), self.open_period),
            close_date=self.close_date
            if close_date is ...
            else prefer(close_date(self.close_date), self.close_date),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        question: str | EllipsisType = ...,
        options: list[PollOption] | EllipsisType = ...,
        total_voter_count: int | EllipsisType = ...,
        is_closed: bool | EllipsisType = ...,
        is_anonymous: bool | EllipsisType = ...,
        type: str | EllipsisType = ...,
        allows_multiple_answers: bool | EllipsisType = ...,
        correct_option_id: int | None | EllipsisType = ...,
        explanation: str | None | EllipsisType = ...,
        explanation_entities: list[MessageEntity] | None | EllipsisType = ...,
        open_period: int | None | EllipsisType = ...,
        close_date: int | None | EllipsisType = ...,
    ) -> Poll:
        """Replaces some of model's fields with provided ones"""
        return Poll(
            id=id if id is not ... else self.id,
            question=question if question is not ... else self.question,
            options=options if options is not ... else self.options,
            total_voter_count=total_voter_count
            if total_voter_count is not ...
            else self.total_voter_count,
            is_closed=is_closed if is_closed is not ... else self.is_closed,
            is_anonymous=is_anonymous if is_anonymous is not ... else self.is_anonymous,
            type=type if type is not ... else self.type,
            allows_multiple_answers=allows_multiple_answers
            if allows_multiple_answers is not ...
            else self.allows_multiple_answers,
            correct_option_id=correct_option_id
            if correct_option_id is not ...
            else self.correct_option_id,
            explanation=explanation if explanation is not ... else self.explanation,
            explanation_entities=explanation_entities
            if explanation_entities is not ...
            else self.explanation_entities,
            open_period=open_period if open_period is not ... else self.open_period,
            close_date=close_date if close_date is not ... else self.close_date,
        )


@dataclass(frozen=False, slots=True)
class Location:
    """This object represents a point on the map."""

    longitude: float
    """Longitude as defined by sender """
    latitude: float
    """Latitude as defined by sender """
    horizontal_accuracy: float | None = None
    """Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    live_period: int | None = None
    """Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only. """
    heading: int | None = None
    """Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only. """
    proximity_alert_radius: int | None = None
    """Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        longitude: AlterFn[float] | EllipsisType = ...,
        latitude: AlterFn[float] | EllipsisType = ...,
        horizontal_accuracy: AlterFn[float | None] | EllipsisType = ...,
        live_period: AlterFn[int | None] | EllipsisType = ...,
        heading: AlterFn[int | None] | EllipsisType = ...,
        proximity_alert_radius: AlterFn[int | None] | EllipsisType = ...,
    ) -> Location:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Location(
            longitude=self.longitude
            if longitude is ...
            else prefer(longitude(self.longitude), self.longitude),
            latitude=self.latitude
            if latitude is ...
            else prefer(latitude(self.latitude), self.latitude),
            horizontal_accuracy=self.horizontal_accuracy
            if horizontal_accuracy is ...
            else prefer(
                horizontal_accuracy(self.horizontal_accuracy), self.horizontal_accuracy
            ),
            live_period=self.live_period
            if live_period is ...
            else prefer(live_period(self.live_period), self.live_period),
            heading=self.heading
            if heading is ...
            else prefer(heading(self.heading), self.heading),
            proximity_alert_radius=self.proximity_alert_radius
            if proximity_alert_radius is ...
            else prefer(
                proximity_alert_radius(self.proximity_alert_radius),
                self.proximity_alert_radius,
            ),
        )

    def copy_with(
        self,
        longitude: float | EllipsisType = ...,
        latitude: float | EllipsisType = ...,
        horizontal_accuracy: float | None | EllipsisType = ...,
        live_period: int | None | EllipsisType = ...,
        heading: int | None | EllipsisType = ...,
        proximity_alert_radius: int | None | EllipsisType = ...,
    ) -> Location:
        """Replaces some of model's fields with provided ones"""
        return Location(
            longitude=longitude if longitude is not ... else self.longitude,
            latitude=latitude if latitude is not ... else self.latitude,
            horizontal_accuracy=horizontal_accuracy
            if horizontal_accuracy is not ...
            else self.horizontal_accuracy,
            live_period=live_period if live_period is not ... else self.live_period,
            heading=heading if heading is not ... else self.heading,
            proximity_alert_radius=proximity_alert_radius
            if proximity_alert_radius is not ...
            else self.proximity_alert_radius,
        )


@dataclass(frozen=False, slots=True)
class Venue:
    """This object represents a venue."""

    location: Location
    """Venue location. Can't be a live location """
    title: str
    """Name of the venue """
    address: str
    """Address of the venue """
    foursquare_id: str | None = None
    """Optional. Foursquare identifier of the venue """
    foursquare_type: str | None = None
    """Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str | None = None
    """Optional. Google Places identifier of the venue """
    google_place_type: str | None = None
    """Optional. Google Places type of the venue. (See supported types.) """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        location: AlterFn[Location] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        address: AlterFn[str] | EllipsisType = ...,
        foursquare_id: AlterFn[str | None] | EllipsisType = ...,
        foursquare_type: AlterFn[str | None] | EllipsisType = ...,
        google_place_id: AlterFn[str | None] | EllipsisType = ...,
        google_place_type: AlterFn[str | None] | EllipsisType = ...,
    ) -> Venue:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Venue(
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            address=self.address
            if address is ...
            else prefer(address(self.address), self.address),
            foursquare_id=self.foursquare_id
            if foursquare_id is ...
            else prefer(foursquare_id(self.foursquare_id), self.foursquare_id),
            foursquare_type=self.foursquare_type
            if foursquare_type is ...
            else prefer(foursquare_type(self.foursquare_type), self.foursquare_type),
            google_place_id=self.google_place_id
            if google_place_id is ...
            else prefer(google_place_id(self.google_place_id), self.google_place_id),
            google_place_type=self.google_place_type
            if google_place_type is ...
            else prefer(
                google_place_type(self.google_place_type), self.google_place_type
            ),
        )

    def copy_with(
        self,
        location: Location | EllipsisType = ...,
        title: str | EllipsisType = ...,
        address: str | EllipsisType = ...,
        foursquare_id: str | None | EllipsisType = ...,
        foursquare_type: str | None | EllipsisType = ...,
        google_place_id: str | None | EllipsisType = ...,
        google_place_type: str | None | EllipsisType = ...,
    ) -> Venue:
        """Replaces some of model's fields with provided ones"""
        return Venue(
            location=location if location is not ... else self.location,
            title=title if title is not ... else self.title,
            address=address if address is not ... else self.address,
            foursquare_id=foursquare_id
            if foursquare_id is not ...
            else self.foursquare_id,
            foursquare_type=foursquare_type
            if foursquare_type is not ...
            else self.foursquare_type,
            google_place_id=google_place_id
            if google_place_id is not ...
            else self.google_place_id,
            google_place_type=google_place_type
            if google_place_type is not ...
            else self.google_place_type,
        )


@dataclass(frozen=False, slots=True)
class WebAppData:
    """Describes data sent from a Web App to the bot."""

    data: str
    """The data. Be aware that a bad client can send arbitrary data in this field. """
    button_text: str
    """Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        data: AlterFn[str] | EllipsisType = ...,
        button_text: AlterFn[str] | EllipsisType = ...,
    ) -> WebAppData:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return WebAppData(
            data=self.data if data is ... else prefer(data(self.data), self.data),
            button_text=self.button_text
            if button_text is ...
            else prefer(button_text(self.button_text), self.button_text),
        )

    def copy_with(
        self,
        data: str | EllipsisType = ...,
        button_text: str | EllipsisType = ...,
    ) -> WebAppData:
        """Replaces some of model's fields with provided ones"""
        return WebAppData(
            data=data if data is not ... else self.data,
            button_text=button_text if button_text is not ... else self.button_text,
        )


@dataclass(frozen=False, slots=True)
class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user."""

    traveler: User
    """User that triggered the alert """
    watcher: User
    """User that set the alert """
    distance: int
    """The distance between the users """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        traveler: AlterFn[User] | EllipsisType = ...,
        watcher: AlterFn[User] | EllipsisType = ...,
        distance: AlterFn[int] | EllipsisType = ...,
    ) -> ProximityAlertTriggered:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ProximityAlertTriggered(
            traveler=self.traveler
            if traveler is ...
            else prefer(traveler(self.traveler), self.traveler),
            watcher=self.watcher
            if watcher is ...
            else prefer(watcher(self.watcher), self.watcher),
            distance=self.distance
            if distance is ...
            else prefer(distance(self.distance), self.distance),
        )

    def copy_with(
        self,
        traveler: User | EllipsisType = ...,
        watcher: User | EllipsisType = ...,
        distance: int | EllipsisType = ...,
    ) -> ProximityAlertTriggered:
        """Replaces some of model's fields with provided ones"""
        return ProximityAlertTriggered(
            traveler=traveler if traveler is not ... else self.traveler,
            watcher=watcher if watcher is not ... else self.watcher,
            distance=distance if distance is not ... else self.distance,
        )


@dataclass(frozen=False, slots=True)
class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings."""

    message_auto_delete_time: int
    """New auto-delete time for messages in the chat; in seconds """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        message_auto_delete_time: AlterFn[int] | EllipsisType = ...,
    ) -> MessageAutoDeleteTimerChanged:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MessageAutoDeleteTimerChanged(
            message_auto_delete_time=self.message_auto_delete_time
            if message_auto_delete_time is ...
            else prefer(
                message_auto_delete_time(self.message_auto_delete_time),
                self.message_auto_delete_time,
            )
        )

    def copy_with(
        self,
        message_auto_delete_time: int | EllipsisType = ...,
    ) -> MessageAutoDeleteTimerChanged:
        """Replaces some of model's fields with provided ones"""
        return MessageAutoDeleteTimerChanged(
            message_auto_delete_time=message_auto_delete_time
            if message_auto_delete_time is not ...
            else self.message_auto_delete_time
        )


@dataclass(frozen=False, slots=True)
class ForumTopicCreated:
    """This object represents a service message about a new forum topic created in the chat."""

    name: str
    """Name of the topic """
    icon_color: int
    """Color of the topic icon in RGB format """
    icon_custom_emoji_id: str | None = None
    """Optional. Unique identifier of the custom emoji shown as the topic icon """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        name: AlterFn[str] | EllipsisType = ...,
        icon_color: AlterFn[int] | EllipsisType = ...,
        icon_custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
    ) -> ForumTopicCreated:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForumTopicCreated(
            name=self.name if name is ... else prefer(name(self.name), self.name),
            icon_color=self.icon_color
            if icon_color is ...
            else prefer(icon_color(self.icon_color), self.icon_color),
            icon_custom_emoji_id=self.icon_custom_emoji_id
            if icon_custom_emoji_id is ...
            else prefer(
                icon_custom_emoji_id(self.icon_custom_emoji_id),
                self.icon_custom_emoji_id,
            ),
        )

    def copy_with(
        self,
        name: str | EllipsisType = ...,
        icon_color: int | EllipsisType = ...,
        icon_custom_emoji_id: str | None | EllipsisType = ...,
    ) -> ForumTopicCreated:
        """Replaces some of model's fields with provided ones"""
        return ForumTopicCreated(
            name=name if name is not ... else self.name,
            icon_color=icon_color if icon_color is not ... else self.icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id
            if icon_custom_emoji_id is not ...
            else self.icon_custom_emoji_id,
        )


@dataclass(frozen=False, slots=True)
class ForumTopicClosed:
    """This object represents a service message about a forum topic closed in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> ForumTopicClosed:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForumTopicClosed()

    def copy_with(
        self,
    ) -> ForumTopicClosed:
        """Replaces some of model's fields with provided ones"""
        return ForumTopicClosed()


@dataclass(frozen=False, slots=True)
class ForumTopicEdited:
    """This object represents a service message about an edited forum topic."""

    name: str | None = None
    """Optional. New name of the topic, if it was edited """
    icon_custom_emoji_id: str | None = None
    """Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        name: AlterFn[str | None] | EllipsisType = ...,
        icon_custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
    ) -> ForumTopicEdited:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForumTopicEdited(
            name=self.name if name is ... else prefer(name(self.name), self.name),
            icon_custom_emoji_id=self.icon_custom_emoji_id
            if icon_custom_emoji_id is ...
            else prefer(
                icon_custom_emoji_id(self.icon_custom_emoji_id),
                self.icon_custom_emoji_id,
            ),
        )

    def copy_with(
        self,
        name: str | None | EllipsisType = ...,
        icon_custom_emoji_id: str | None | EllipsisType = ...,
    ) -> ForumTopicEdited:
        """Replaces some of model's fields with provided ones"""
        return ForumTopicEdited(
            name=name if name is not ... else self.name,
            icon_custom_emoji_id=icon_custom_emoji_id
            if icon_custom_emoji_id is not ...
            else self.icon_custom_emoji_id,
        )


@dataclass(frozen=False, slots=True)
class ForumTopicReopened:
    """This object represents a service message about a forum topic reopened in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> ForumTopicReopened:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForumTopicReopened()

    def copy_with(
        self,
    ) -> ForumTopicReopened:
        """Replaces some of model's fields with provided ones"""
        return ForumTopicReopened()


@dataclass(frozen=False, slots=True)
class GeneralForumTopicHidden:
    """This object represents a service message about General forum topic hidden in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> GeneralForumTopicHidden:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return GeneralForumTopicHidden()

    def copy_with(
        self,
    ) -> GeneralForumTopicHidden:
        """Replaces some of model's fields with provided ones"""
        return GeneralForumTopicHidden()


@dataclass(frozen=False, slots=True)
class GeneralForumTopicUnhidden:
    """This object represents a service message about General forum topic unhidden in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> GeneralForumTopicUnhidden:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return GeneralForumTopicUnhidden()

    def copy_with(
        self,
    ) -> GeneralForumTopicUnhidden:
        """Replaces some of model's fields with provided ones"""
        return GeneralForumTopicUnhidden()


@dataclass(frozen=False, slots=True)
class UserShared:
    """This object contains information about the user whose identifier was shared with the bot using a KeyboardButtonRequestUser button."""

    request_id: int
    """Identifier of the request """
    user_id: int
    """Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        request_id: AlterFn[int] | EllipsisType = ...,
        user_id: AlterFn[int] | EllipsisType = ...,
    ) -> UserShared:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return UserShared(
            request_id=self.request_id
            if request_id is ...
            else prefer(request_id(self.request_id), self.request_id),
            user_id=self.user_id
            if user_id is ...
            else prefer(user_id(self.user_id), self.user_id),
        )

    def copy_with(
        self,
        request_id: int | EllipsisType = ...,
        user_id: int | EllipsisType = ...,
    ) -> UserShared:
        """Replaces some of model's fields with provided ones"""
        return UserShared(
            request_id=request_id if request_id is not ... else self.request_id,
            user_id=user_id if user_id is not ... else self.user_id,
        )


@dataclass(frozen=False, slots=True)
class ChatShared:
    """This object contains information about the chat whose identifier was shared with the bot using a KeyboardButtonRequestChat button."""

    request_id: int
    """Identifier of the request """
    chat_id: int
    """Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        request_id: AlterFn[int] | EllipsisType = ...,
        chat_id: AlterFn[int] | EllipsisType = ...,
    ) -> ChatShared:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatShared(
            request_id=self.request_id
            if request_id is ...
            else prefer(request_id(self.request_id), self.request_id),
            chat_id=self.chat_id
            if chat_id is ...
            else prefer(chat_id(self.chat_id), self.chat_id),
        )

    def copy_with(
        self,
        request_id: int | EllipsisType = ...,
        chat_id: int | EllipsisType = ...,
    ) -> ChatShared:
        """Replaces some of model's fields with provided ones"""
        return ChatShared(
            request_id=request_id if request_id is not ... else self.request_id,
            chat_id=chat_id if chat_id is not ... else self.chat_id,
        )


@dataclass(frozen=False, slots=True)
class WriteAccessAllowed:
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess."""

    from_request: bool | None = None
    """Optional. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess """
    web_app_name: str | None = None
    """Optional. Name of the Web App, if the access was granted when the Web App was launched from a link """
    from_attachment_menu: bool | None = None
    """Optional. True, if the access was granted when the bot was added to the attachment or side menu """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        from_request: AlterFn[bool | None] | EllipsisType = ...,
        web_app_name: AlterFn[str | None] | EllipsisType = ...,
        from_attachment_menu: AlterFn[bool | None] | EllipsisType = ...,
    ) -> WriteAccessAllowed:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return WriteAccessAllowed(
            from_request=self.from_request
            if from_request is ...
            else prefer(from_request(self.from_request), self.from_request),
            web_app_name=self.web_app_name
            if web_app_name is ...
            else prefer(web_app_name(self.web_app_name), self.web_app_name),
            from_attachment_menu=self.from_attachment_menu
            if from_attachment_menu is ...
            else prefer(
                from_attachment_menu(self.from_attachment_menu),
                self.from_attachment_menu,
            ),
        )

    def copy_with(
        self,
        from_request: bool | None | EllipsisType = ...,
        web_app_name: str | None | EllipsisType = ...,
        from_attachment_menu: bool | None | EllipsisType = ...,
    ) -> WriteAccessAllowed:
        """Replaces some of model's fields with provided ones"""
        return WriteAccessAllowed(
            from_request=from_request if from_request is not ... else self.from_request,
            web_app_name=web_app_name if web_app_name is not ... else self.web_app_name,
            from_attachment_menu=from_attachment_menu
            if from_attachment_menu is not ...
            else self.from_attachment_menu,
        )


@dataclass(frozen=False, slots=True)
class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat."""

    start_date: int
    """Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        start_date: AlterFn[int] | EllipsisType = ...,
    ) -> VideoChatScheduled:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return VideoChatScheduled(
            start_date=self.start_date
            if start_date is ...
            else prefer(start_date(self.start_date), self.start_date)
        )

    def copy_with(
        self,
        start_date: int | EllipsisType = ...,
    ) -> VideoChatScheduled:
        """Replaces some of model's fields with provided ones"""
        return VideoChatScheduled(
            start_date=start_date if start_date is not ... else self.start_date
        )


@dataclass(frozen=False, slots=True)
class VideoChatStarted:
    """This object represents a service message about a video chat started in the chat. Currently holds no information."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> VideoChatStarted:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return VideoChatStarted()

    def copy_with(
        self,
    ) -> VideoChatStarted:
        """Replaces some of model's fields with provided ones"""
        return VideoChatStarted()


@dataclass(frozen=False, slots=True)
class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat."""

    duration: int
    """Video chat duration in seconds """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        duration: AlterFn[int] | EllipsisType = ...,
    ) -> VideoChatEnded:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return VideoChatEnded(
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration)
        )

    def copy_with(
        self,
        duration: int | EllipsisType = ...,
    ) -> VideoChatEnded:
        """Replaces some of model's fields with provided ones"""
        return VideoChatEnded(
            duration=duration if duration is not ... else self.duration
        )


@dataclass(frozen=False, slots=True)
class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat."""

    users: list[User]
    """New members that were invited to the video chat """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        users: AlterFn[list[User]] | EllipsisType = ...,
    ) -> VideoChatParticipantsInvited:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return VideoChatParticipantsInvited(
            users=self.users if users is ... else prefer(users(self.users), self.users)
        )

    def copy_with(
        self,
        users: list[User] | EllipsisType = ...,
    ) -> VideoChatParticipantsInvited:
        """Replaces some of model's fields with provided ones"""
        return VideoChatParticipantsInvited(
            users=users if users is not ... else self.users
        )


@dataclass(frozen=False, slots=True)
class UserProfilePhotos:
    """This object represent a user's profile pictures."""

    total_count: int
    """Total number of profile pictures the target user has """
    photos: list[list[PhotoSize]]
    """Requested profile pictures (in up to 4 sizes each) """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        total_count: AlterFn[int] | EllipsisType = ...,
        photos: AlterFn[list[list[PhotoSize]]] | EllipsisType = ...,
    ) -> UserProfilePhotos:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return UserProfilePhotos(
            total_count=self.total_count
            if total_count is ...
            else prefer(total_count(self.total_count), self.total_count),
            photos=self.photos
            if photos is ...
            else prefer(photos(self.photos), self.photos),
        )

    def copy_with(
        self,
        total_count: int | EllipsisType = ...,
        photos: list[list[PhotoSize]] | EllipsisType = ...,
    ) -> UserProfilePhotos:
        """Replaces some of model's fields with provided ones"""
        return UserProfilePhotos(
            total_count=total_count if total_count is not ... else self.total_count,
            photos=photos if photos is not ... else self.photos,
        )


@dataclass(frozen=False, slots=True)
class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """
    file_path: str | None = None
    """Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
        file_path: AlterFn[str | None] | EllipsisType = ...,
    ) -> File:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return File(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
            file_path=self.file_path
            if file_path is ...
            else prefer(file_path(self.file_path), self.file_path),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
        file_path: str | None | EllipsisType = ...,
    ) -> File:
        """Replaces some of model's fields with provided ones"""
        return File(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            file_size=file_size if file_size is not ... else self.file_size,
            file_path=file_path if file_path is not ... else self.file_path,
        )


@dataclass(frozen=False, slots=True)
class WebAppInfo:
    """Describes a Web App."""

    url: str
    """An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        url: AlterFn[str] | EllipsisType = ...,
    ) -> WebAppInfo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return WebAppInfo(
            url=self.url if url is ... else prefer(url(self.url), self.url)
        )

    def copy_with(
        self,
        url: str | EllipsisType = ...,
    ) -> WebAppInfo:
        """Replaces some of model's fields with provided ones"""
        return WebAppInfo(url=url if url is not ... else self.url)


@dataclass(frozen=False, slots=True)
class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples)."""

    keyboard: list[list[KeyboardButton]]
    """Array of button rows, each represented by an Array of KeyboardButton objects """
    is_persistent: bool | None = None
    """Optional. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to false, in which case the custom keyboard can be hidden and opened with a keyboard icon. """
    resize_keyboard: bool | None = None
    """Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard. """
    one_time_keyboard: bool | None = None
    """Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false. """
    input_field_placeholder: str | None = None
    """Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters """
    selective: bool | None = None
    """Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        keyboard: AlterFn[list[list[KeyboardButton]]] | EllipsisType = ...,
        is_persistent: AlterFn[bool | None] | EllipsisType = ...,
        resize_keyboard: AlterFn[bool | None] | EllipsisType = ...,
        one_time_keyboard: AlterFn[bool | None] | EllipsisType = ...,
        input_field_placeholder: AlterFn[str | None] | EllipsisType = ...,
        selective: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ReplyKeyboardMarkup:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ReplyKeyboardMarkup(
            keyboard=self.keyboard
            if keyboard is ...
            else prefer(keyboard(self.keyboard), self.keyboard),
            is_persistent=self.is_persistent
            if is_persistent is ...
            else prefer(is_persistent(self.is_persistent), self.is_persistent),
            resize_keyboard=self.resize_keyboard
            if resize_keyboard is ...
            else prefer(resize_keyboard(self.resize_keyboard), self.resize_keyboard),
            one_time_keyboard=self.one_time_keyboard
            if one_time_keyboard is ...
            else prefer(
                one_time_keyboard(self.one_time_keyboard), self.one_time_keyboard
            ),
            input_field_placeholder=self.input_field_placeholder
            if input_field_placeholder is ...
            else prefer(
                input_field_placeholder(self.input_field_placeholder),
                self.input_field_placeholder,
            ),
            selective=self.selective
            if selective is ...
            else prefer(selective(self.selective), self.selective),
        )

    def copy_with(
        self,
        keyboard: list[list[KeyboardButton]] | EllipsisType = ...,
        is_persistent: bool | None | EllipsisType = ...,
        resize_keyboard: bool | None | EllipsisType = ...,
        one_time_keyboard: bool | None | EllipsisType = ...,
        input_field_placeholder: str | None | EllipsisType = ...,
        selective: bool | None | EllipsisType = ...,
    ) -> ReplyKeyboardMarkup:
        """Replaces some of model's fields with provided ones"""
        return ReplyKeyboardMarkup(
            keyboard=keyboard if keyboard is not ... else self.keyboard,
            is_persistent=is_persistent
            if is_persistent is not ...
            else self.is_persistent,
            resize_keyboard=resize_keyboard
            if resize_keyboard is not ...
            else self.resize_keyboard,
            one_time_keyboard=one_time_keyboard
            if one_time_keyboard is not ...
            else self.one_time_keyboard,
            input_field_placeholder=input_field_placeholder
            if input_field_placeholder is not ...
            else self.input_field_placeholder,
            selective=selective if selective is not ... else self.selective,
        )


@dataclass(frozen=False, slots=True)
class KeyboardButton:
    """This object represents one button of the reply keyboard. For simple text buttons, String can be used instead of this object to specify the button text. The optional fields web_app, request_user, request_chat, request_contact, request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
    Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.
    Note: web_app option will only work in Telegram versions released after 16 April, 2022. Older clients will display unsupported message.
    Note: request_user and request_chat options will only work in Telegram versions released after 3 February, 2023. Older clients will display unsupported message.
    """

    text: str
    """Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed """
    request_user: KeyboardButtonRequestUser | None = None
    """Optional. If specified, pressing the button will open a list of suitable users. Tapping on any user will send their identifier to the bot in a "user_shared" service message. Available in private chats only. """
    request_chat: KeyboardButtonRequestChat | None = None
    """Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a "chat_shared" service message. Available in private chats only. """
    request_contact: bool | None = None
    """Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only. """
    request_location: bool | None = None
    """Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only. """
    request_poll: KeyboardButtonPollType | None = None
    """Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only. """
    web_app: WebAppInfo | None = None
    """Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private chats only. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        text: AlterFn[str] | EllipsisType = ...,
        request_user: AlterFn[KeyboardButtonRequestUser | None] | EllipsisType = ...,
        request_chat: AlterFn[KeyboardButtonRequestChat | None] | EllipsisType = ...,
        request_contact: AlterFn[bool | None] | EllipsisType = ...,
        request_location: AlterFn[bool | None] | EllipsisType = ...,
        request_poll: AlterFn[KeyboardButtonPollType | None] | EllipsisType = ...,
        web_app: AlterFn[WebAppInfo | None] | EllipsisType = ...,
    ) -> KeyboardButton:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return KeyboardButton(
            text=self.text if text is ... else prefer(text(self.text), self.text),
            request_user=self.request_user
            if request_user is ...
            else prefer(request_user(self.request_user), self.request_user),
            request_chat=self.request_chat
            if request_chat is ...
            else prefer(request_chat(self.request_chat), self.request_chat),
            request_contact=self.request_contact
            if request_contact is ...
            else prefer(request_contact(self.request_contact), self.request_contact),
            request_location=self.request_location
            if request_location is ...
            else prefer(request_location(self.request_location), self.request_location),
            request_poll=self.request_poll
            if request_poll is ...
            else prefer(request_poll(self.request_poll), self.request_poll),
            web_app=self.web_app
            if web_app is ...
            else prefer(web_app(self.web_app), self.web_app),
        )

    def copy_with(
        self,
        text: str | EllipsisType = ...,
        request_user: KeyboardButtonRequestUser | None | EllipsisType = ...,
        request_chat: KeyboardButtonRequestChat | None | EllipsisType = ...,
        request_contact: bool | None | EllipsisType = ...,
        request_location: bool | None | EllipsisType = ...,
        request_poll: KeyboardButtonPollType | None | EllipsisType = ...,
        web_app: WebAppInfo | None | EllipsisType = ...,
    ) -> KeyboardButton:
        """Replaces some of model's fields with provided ones"""
        return KeyboardButton(
            text=text if text is not ... else self.text,
            request_user=request_user if request_user is not ... else self.request_user,
            request_chat=request_chat if request_chat is not ... else self.request_chat,
            request_contact=request_contact
            if request_contact is not ...
            else self.request_contact,
            request_location=request_location
            if request_location is not ...
            else self.request_location,
            request_poll=request_poll if request_poll is not ... else self.request_poll,
            web_app=web_app if web_app is not ... else self.web_app,
        )


@dataclass(frozen=False, slots=True)
class KeyboardButtonRequestUser:
    """This object defines the criteria used to request a suitable user. The identifier of the selected user will be shared with the bot when the corresponding button is pressed. More about requesting users: https://core.telegram.org/bots/features#chat-and-user-selection"""

    request_id: int
    """Signed 32-bit identifier of the request, which will be received back in the UserShared object. Must be unique within the message """
    user_is_bot: bool | None = None
    """Optional. Pass True to request a bot, pass False to request a regular user. If not specified, no additional restrictions are applied. """
    user_is_premium: bool | None = None
    """Optional. Pass True to request a premium user, pass False to request a non-premium user. If not specified, no additional restrictions are applied. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        request_id: AlterFn[int] | EllipsisType = ...,
        user_is_bot: AlterFn[bool | None] | EllipsisType = ...,
        user_is_premium: AlterFn[bool | None] | EllipsisType = ...,
    ) -> KeyboardButtonRequestUser:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return KeyboardButtonRequestUser(
            request_id=self.request_id
            if request_id is ...
            else prefer(request_id(self.request_id), self.request_id),
            user_is_bot=self.user_is_bot
            if user_is_bot is ...
            else prefer(user_is_bot(self.user_is_bot), self.user_is_bot),
            user_is_premium=self.user_is_premium
            if user_is_premium is ...
            else prefer(user_is_premium(self.user_is_premium), self.user_is_premium),
        )

    def copy_with(
        self,
        request_id: int | EllipsisType = ...,
        user_is_bot: bool | None | EllipsisType = ...,
        user_is_premium: bool | None | EllipsisType = ...,
    ) -> KeyboardButtonRequestUser:
        """Replaces some of model's fields with provided ones"""
        return KeyboardButtonRequestUser(
            request_id=request_id if request_id is not ... else self.request_id,
            user_is_bot=user_is_bot if user_is_bot is not ... else self.user_is_bot,
            user_is_premium=user_is_premium
            if user_is_premium is not ...
            else self.user_is_premium,
        )


@dataclass(frozen=False, slots=True)
class KeyboardButtonRequestChat:
    """This object defines the criteria used to request a suitable chat. The identifier of the selected chat will be shared with the bot when the corresponding button is pressed. More about requesting chats: https://core.telegram.org/bots/features#chat-and-user-selection"""

    request_id: int
    """Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message """
    chat_is_channel: bool
    """Pass True to request a channel chat, pass False to request a group or a supergroup chat. """
    chat_is_forum: bool | None = None
    """Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied. """
    chat_has_username: bool | None = None
    """Optional. Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied. """
    chat_is_created: bool | None = None
    """Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied. """
    user_administrator_rights: ChatAdministratorRights | None = None
    """Optional. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied. """
    bot_administrator_rights: ChatAdministratorRights | None = None
    """Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied. """
    bot_is_member: bool | None = None
    """Optional. Pass True to request a chat with the bot as a member. Otherwise, no additional restrictions are applied. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        request_id: AlterFn[int] | EllipsisType = ...,
        chat_is_channel: AlterFn[bool] | EllipsisType = ...,
        chat_is_forum: AlterFn[bool | None] | EllipsisType = ...,
        chat_has_username: AlterFn[bool | None] | EllipsisType = ...,
        chat_is_created: AlterFn[bool | None] | EllipsisType = ...,
        user_administrator_rights: AlterFn[ChatAdministratorRights | None]
        | EllipsisType = ...,
        bot_administrator_rights: AlterFn[ChatAdministratorRights | None]
        | EllipsisType = ...,
        bot_is_member: AlterFn[bool | None] | EllipsisType = ...,
    ) -> KeyboardButtonRequestChat:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return KeyboardButtonRequestChat(
            request_id=self.request_id
            if request_id is ...
            else prefer(request_id(self.request_id), self.request_id),
            chat_is_channel=self.chat_is_channel
            if chat_is_channel is ...
            else prefer(chat_is_channel(self.chat_is_channel), self.chat_is_channel),
            chat_is_forum=self.chat_is_forum
            if chat_is_forum is ...
            else prefer(chat_is_forum(self.chat_is_forum), self.chat_is_forum),
            chat_has_username=self.chat_has_username
            if chat_has_username is ...
            else prefer(
                chat_has_username(self.chat_has_username), self.chat_has_username
            ),
            chat_is_created=self.chat_is_created
            if chat_is_created is ...
            else prefer(chat_is_created(self.chat_is_created), self.chat_is_created),
            user_administrator_rights=self.user_administrator_rights
            if user_administrator_rights is ...
            else prefer(
                user_administrator_rights(self.user_administrator_rights),
                self.user_administrator_rights,
            ),
            bot_administrator_rights=self.bot_administrator_rights
            if bot_administrator_rights is ...
            else prefer(
                bot_administrator_rights(self.bot_administrator_rights),
                self.bot_administrator_rights,
            ),
            bot_is_member=self.bot_is_member
            if bot_is_member is ...
            else prefer(bot_is_member(self.bot_is_member), self.bot_is_member),
        )

    def copy_with(
        self,
        request_id: int | EllipsisType = ...,
        chat_is_channel: bool | EllipsisType = ...,
        chat_is_forum: bool | None | EllipsisType = ...,
        chat_has_username: bool | None | EllipsisType = ...,
        chat_is_created: bool | None | EllipsisType = ...,
        user_administrator_rights: ChatAdministratorRights | None | EllipsisType = ...,
        bot_administrator_rights: ChatAdministratorRights | None | EllipsisType = ...,
        bot_is_member: bool | None | EllipsisType = ...,
    ) -> KeyboardButtonRequestChat:
        """Replaces some of model's fields with provided ones"""
        return KeyboardButtonRequestChat(
            request_id=request_id if request_id is not ... else self.request_id,
            chat_is_channel=chat_is_channel
            if chat_is_channel is not ...
            else self.chat_is_channel,
            chat_is_forum=chat_is_forum
            if chat_is_forum is not ...
            else self.chat_is_forum,
            chat_has_username=chat_has_username
            if chat_has_username is not ...
            else self.chat_has_username,
            chat_is_created=chat_is_created
            if chat_is_created is not ...
            else self.chat_is_created,
            user_administrator_rights=user_administrator_rights
            if user_administrator_rights is not ...
            else self.user_administrator_rights,
            bot_administrator_rights=bot_administrator_rights
            if bot_administrator_rights is not ...
            else self.bot_administrator_rights,
            bot_is_member=bot_is_member
            if bot_is_member is not ...
            else self.bot_is_member,
        )


@dataclass(frozen=False, slots=True)
class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed."""

    type: str | None = None
    """Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str | None] | EllipsisType = ...,
    ) -> KeyboardButtonPollType:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return KeyboardButtonPollType(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | None | EllipsisType = ...,
    ) -> KeyboardButtonPollType:
        """Replaces some of model's fields with provided ones"""
        return KeyboardButtonPollType(type=type if type is not ... else self.type)


@dataclass(frozen=False, slots=True)
class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup)."""

    remove_keyboard: bool
    """Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup) """
    selective: bool | None = None
    """Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        remove_keyboard: AlterFn[bool] | EllipsisType = ...,
        selective: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ReplyKeyboardRemove:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ReplyKeyboardRemove(
            remove_keyboard=self.remove_keyboard
            if remove_keyboard is ...
            else prefer(remove_keyboard(self.remove_keyboard), self.remove_keyboard),
            selective=self.selective
            if selective is ...
            else prefer(selective(self.selective), self.selective),
        )

    def copy_with(
        self,
        remove_keyboard: bool | EllipsisType = ...,
        selective: bool | None | EllipsisType = ...,
    ) -> ReplyKeyboardRemove:
        """Replaces some of model's fields with provided ones"""
        return ReplyKeyboardRemove(
            remove_keyboard=remove_keyboard
            if remove_keyboard is not ...
            else self.remove_keyboard,
            selective=selective if selective is not ... else self.selective,
        )


@dataclass(frozen=False, slots=True)
class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to the message it belongs to.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
    """

    inline_keyboard: list[list[InlineKeyboardButton]]
    """Array of button rows, each represented by an Array of InlineKeyboardButton objects """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        inline_keyboard: AlterFn[list[list[InlineKeyboardButton]]] | EllipsisType = ...,
    ) -> InlineKeyboardMarkup:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineKeyboardMarkup(
            inline_keyboard=self.inline_keyboard
            if inline_keyboard is ...
            else prefer(inline_keyboard(self.inline_keyboard), self.inline_keyboard)
        )

    def copy_with(
        self,
        inline_keyboard: list[list[InlineKeyboardButton]] | EllipsisType = ...,
    ) -> InlineKeyboardMarkup:
        """Replaces some of model's fields with provided ones"""
        return InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
            if inline_keyboard is not ...
            else self.inline_keyboard
        )


@dataclass(frozen=False, slots=True)
class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields."""

    text: str
    """Label text on the button """
    url: str | None = None
    """Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings. """
    callback_data: str | None = None
    """Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes """
    web_app: WebAppInfo | None = None
    """Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot. """
    login_url: LoginUrl | None = None
    """Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget. """
    switch_inline_query: str | None = None
    """Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. """
    switch_inline_query_current_chat: str | None = None
    """Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. """
    switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = None
    """Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field """
    callback_game: CallbackGame | None = None
    """Optional. Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row. """
    pay: bool | None = None
    """Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        text: AlterFn[str] | EllipsisType = ...,
        url: AlterFn[str | None] | EllipsisType = ...,
        callback_data: AlterFn[str | None] | EllipsisType = ...,
        web_app: AlterFn[WebAppInfo | None] | EllipsisType = ...,
        login_url: AlterFn[LoginUrl | None] | EllipsisType = ...,
        switch_inline_query: AlterFn[str | None] | EllipsisType = ...,
        switch_inline_query_current_chat: AlterFn[str | None] | EllipsisType = ...,
        switch_inline_query_chosen_chat: AlterFn[SwitchInlineQueryChosenChat | None]
        | EllipsisType = ...,
        callback_game: AlterFn[CallbackGame | None] | EllipsisType = ...,
        pay: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InlineKeyboardButton:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineKeyboardButton(
            text=self.text if text is ... else prefer(text(self.text), self.text),
            url=self.url if url is ... else prefer(url(self.url), self.url),
            callback_data=self.callback_data
            if callback_data is ...
            else prefer(callback_data(self.callback_data), self.callback_data),
            web_app=self.web_app
            if web_app is ...
            else prefer(web_app(self.web_app), self.web_app),
            login_url=self.login_url
            if login_url is ...
            else prefer(login_url(self.login_url), self.login_url),
            switch_inline_query=self.switch_inline_query
            if switch_inline_query is ...
            else prefer(
                switch_inline_query(self.switch_inline_query), self.switch_inline_query
            ),
            switch_inline_query_current_chat=self.switch_inline_query_current_chat
            if switch_inline_query_current_chat is ...
            else prefer(
                switch_inline_query_current_chat(self.switch_inline_query_current_chat),
                self.switch_inline_query_current_chat,
            ),
            switch_inline_query_chosen_chat=self.switch_inline_query_chosen_chat
            if switch_inline_query_chosen_chat is ...
            else prefer(
                switch_inline_query_chosen_chat(self.switch_inline_query_chosen_chat),
                self.switch_inline_query_chosen_chat,
            ),
            callback_game=self.callback_game
            if callback_game is ...
            else prefer(callback_game(self.callback_game), self.callback_game),
            pay=self.pay if pay is ... else prefer(pay(self.pay), self.pay),
        )

    def copy_with(
        self,
        text: str | EllipsisType = ...,
        url: str | None | EllipsisType = ...,
        callback_data: str | None | EllipsisType = ...,
        web_app: WebAppInfo | None | EllipsisType = ...,
        login_url: LoginUrl | None | EllipsisType = ...,
        switch_inline_query: str | None | EllipsisType = ...,
        switch_inline_query_current_chat: str | None | EllipsisType = ...,
        switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat
        | None
        | EllipsisType = ...,
        callback_game: CallbackGame | None | EllipsisType = ...,
        pay: bool | None | EllipsisType = ...,
    ) -> InlineKeyboardButton:
        """Replaces some of model's fields with provided ones"""
        return InlineKeyboardButton(
            text=text if text is not ... else self.text,
            url=url if url is not ... else self.url,
            callback_data=callback_data
            if callback_data is not ...
            else self.callback_data,
            web_app=web_app if web_app is not ... else self.web_app,
            login_url=login_url if login_url is not ... else self.login_url,
            switch_inline_query=switch_inline_query
            if switch_inline_query is not ...
            else self.switch_inline_query,
            switch_inline_query_current_chat=switch_inline_query_current_chat
            if switch_inline_query_current_chat is not ...
            else self.switch_inline_query_current_chat,
            switch_inline_query_chosen_chat=switch_inline_query_chosen_chat
            if switch_inline_query_chosen_chat is not ...
            else self.switch_inline_query_chosen_chat,
            callback_game=callback_game
            if callback_game is not ...
            else self.callback_game,
            pay=pay if pay is not ... else self.pay,
        )


@dataclass(frozen=False, slots=True)
class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7."""

    url: str
    """An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization. """
    forward_text: str | None = None
    """Optional. New text of the button in forwarded messages. """
    bot_username: str | None = None
    """Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details. """
    request_write_access: bool | None = None
    """Optional. Pass True to request the permission for your bot to send messages to the user. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        url: AlterFn[str] | EllipsisType = ...,
        forward_text: AlterFn[str | None] | EllipsisType = ...,
        bot_username: AlterFn[str | None] | EllipsisType = ...,
        request_write_access: AlterFn[bool | None] | EllipsisType = ...,
    ) -> LoginUrl:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return LoginUrl(
            url=self.url if url is ... else prefer(url(self.url), self.url),
            forward_text=self.forward_text
            if forward_text is ...
            else prefer(forward_text(self.forward_text), self.forward_text),
            bot_username=self.bot_username
            if bot_username is ...
            else prefer(bot_username(self.bot_username), self.bot_username),
            request_write_access=self.request_write_access
            if request_write_access is ...
            else prefer(
                request_write_access(self.request_write_access),
                self.request_write_access,
            ),
        )

    def copy_with(
        self,
        url: str | EllipsisType = ...,
        forward_text: str | None | EllipsisType = ...,
        bot_username: str | None | EllipsisType = ...,
        request_write_access: bool | None | EllipsisType = ...,
    ) -> LoginUrl:
        """Replaces some of model's fields with provided ones"""
        return LoginUrl(
            url=url if url is not ... else self.url,
            forward_text=forward_text if forward_text is not ... else self.forward_text,
            bot_username=bot_username if bot_username is not ... else self.bot_username,
            request_write_access=request_write_access
            if request_write_access is not ...
            else self.request_write_access,
        )


@dataclass(frozen=False, slots=True)
class SwitchInlineQueryChosenChat:
    """This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query."""

    query: str | None = None
    """Optional. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted """
    allow_user_chats: bool | None = None
    """Optional. True, if private chats with users can be chosen """
    allow_bot_chats: bool | None = None
    """Optional. True, if private chats with bots can be chosen """
    allow_group_chats: bool | None = None
    """Optional. True, if group and supergroup chats can be chosen """
    allow_channel_chats: bool | None = None
    """Optional. True, if channel chats can be chosen """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        query: AlterFn[str | None] | EllipsisType = ...,
        allow_user_chats: AlterFn[bool | None] | EllipsisType = ...,
        allow_bot_chats: AlterFn[bool | None] | EllipsisType = ...,
        allow_group_chats: AlterFn[bool | None] | EllipsisType = ...,
        allow_channel_chats: AlterFn[bool | None] | EllipsisType = ...,
    ) -> SwitchInlineQueryChosenChat:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return SwitchInlineQueryChosenChat(
            query=self.query if query is ... else prefer(query(self.query), self.query),
            allow_user_chats=self.allow_user_chats
            if allow_user_chats is ...
            else prefer(allow_user_chats(self.allow_user_chats), self.allow_user_chats),
            allow_bot_chats=self.allow_bot_chats
            if allow_bot_chats is ...
            else prefer(allow_bot_chats(self.allow_bot_chats), self.allow_bot_chats),
            allow_group_chats=self.allow_group_chats
            if allow_group_chats is ...
            else prefer(
                allow_group_chats(self.allow_group_chats), self.allow_group_chats
            ),
            allow_channel_chats=self.allow_channel_chats
            if allow_channel_chats is ...
            else prefer(
                allow_channel_chats(self.allow_channel_chats), self.allow_channel_chats
            ),
        )

    def copy_with(
        self,
        query: str | None | EllipsisType = ...,
        allow_user_chats: bool | None | EllipsisType = ...,
        allow_bot_chats: bool | None | EllipsisType = ...,
        allow_group_chats: bool | None | EllipsisType = ...,
        allow_channel_chats: bool | None | EllipsisType = ...,
    ) -> SwitchInlineQueryChosenChat:
        """Replaces some of model's fields with provided ones"""
        return SwitchInlineQueryChosenChat(
            query=query if query is not ... else self.query,
            allow_user_chats=allow_user_chats
            if allow_user_chats is not ...
            else self.allow_user_chats,
            allow_bot_chats=allow_bot_chats
            if allow_bot_chats is not ...
            else self.allow_bot_chats,
            allow_group_chats=allow_group_chats
            if allow_group_chats is not ...
            else self.allow_group_chats,
            allow_channel_chats=allow_channel_chats
            if allow_channel_chats is not ...
            else self.allow_channel_chats,
        )


@dataclass(frozen=False, slots=True)
class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present."""

    id: str
    """Unique identifier for this query """
    from_: User
    """Sender """
    chat_instance: str
    """Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games. """
    message: Message | None = None
    """Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old """
    inline_message_id: str | None = None
    """Optional. Identifier of the message sent via the bot in inline mode, that originated the query. """
    data: str | None = None
    """Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data. """
    game_short_name: str | None = None
    """Optional. Short name of a Game to be returned, serves as the unique identifier for the game """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        message: AlterFn[Message | None] | EllipsisType = ...,
        inline_message_id: AlterFn[str | None] | EllipsisType = ...,
        chat_instance: AlterFn[str] | EllipsisType = ...,
        data: AlterFn[str | None] | EllipsisType = ...,
        game_short_name: AlterFn[str | None] | EllipsisType = ...,
    ) -> CallbackQuery:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return CallbackQuery(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
            inline_message_id=self.inline_message_id
            if inline_message_id is ...
            else prefer(
                inline_message_id(self.inline_message_id), self.inline_message_id
            ),
            chat_instance=self.chat_instance
            if chat_instance is ...
            else prefer(chat_instance(self.chat_instance), self.chat_instance),
            data=self.data if data is ... else prefer(data(self.data), self.data),
            game_short_name=self.game_short_name
            if game_short_name is ...
            else prefer(game_short_name(self.game_short_name), self.game_short_name),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        message: Message | None | EllipsisType = ...,
        inline_message_id: str | None | EllipsisType = ...,
        chat_instance: str | EllipsisType = ...,
        data: str | None | EllipsisType = ...,
        game_short_name: str | None | EllipsisType = ...,
    ) -> CallbackQuery:
        """Replaces some of model's fields with provided ones"""
        return CallbackQuery(
            id=id if id is not ... else self.id,
            from_=from_ if from_ is not ... else self.from_,
            message=message if message is not ... else self.message,
            inline_message_id=inline_message_id
            if inline_message_id is not ...
            else self.inline_message_id,
            chat_instance=chat_instance
            if chat_instance is not ...
            else self.chat_instance,
            data=data if data is not ... else self.data,
            game_short_name=game_short_name
            if game_short_name is not ...
            else self.game_short_name,
        )


@dataclass(frozen=False, slots=True)
class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode."""

    force_reply: bool
    """Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply' """
    input_field_placeholder: str | None = None
    """Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters """
    selective: bool | None = None
    """Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        force_reply: AlterFn[bool] | EllipsisType = ...,
        input_field_placeholder: AlterFn[str | None] | EllipsisType = ...,
        selective: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ForceReply:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForceReply(
            force_reply=self.force_reply
            if force_reply is ...
            else prefer(force_reply(self.force_reply), self.force_reply),
            input_field_placeholder=self.input_field_placeholder
            if input_field_placeholder is ...
            else prefer(
                input_field_placeholder(self.input_field_placeholder),
                self.input_field_placeholder,
            ),
            selective=self.selective
            if selective is ...
            else prefer(selective(self.selective), self.selective),
        )

    def copy_with(
        self,
        force_reply: bool | EllipsisType = ...,
        input_field_placeholder: str | None | EllipsisType = ...,
        selective: bool | None | EllipsisType = ...,
    ) -> ForceReply:
        """Replaces some of model's fields with provided ones"""
        return ForceReply(
            force_reply=force_reply if force_reply is not ... else self.force_reply,
            input_field_placeholder=input_field_placeholder
            if input_field_placeholder is not ...
            else self.input_field_placeholder,
            selective=selective if selective is not ... else self.selective,
        )


@dataclass(frozen=False, slots=True)
class ChatPhoto:
    """This object represents a chat photo."""

    small_file_id: str
    """File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed. """
    small_file_unique_id: str
    """Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    big_file_id: str
    """File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed. """
    big_file_unique_id: str
    """Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        small_file_id: AlterFn[str] | EllipsisType = ...,
        small_file_unique_id: AlterFn[str] | EllipsisType = ...,
        big_file_id: AlterFn[str] | EllipsisType = ...,
        big_file_unique_id: AlterFn[str] | EllipsisType = ...,
    ) -> ChatPhoto:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatPhoto(
            small_file_id=self.small_file_id
            if small_file_id is ...
            else prefer(small_file_id(self.small_file_id), self.small_file_id),
            small_file_unique_id=self.small_file_unique_id
            if small_file_unique_id is ...
            else prefer(
                small_file_unique_id(self.small_file_unique_id),
                self.small_file_unique_id,
            ),
            big_file_id=self.big_file_id
            if big_file_id is ...
            else prefer(big_file_id(self.big_file_id), self.big_file_id),
            big_file_unique_id=self.big_file_unique_id
            if big_file_unique_id is ...
            else prefer(
                big_file_unique_id(self.big_file_unique_id), self.big_file_unique_id
            ),
        )

    def copy_with(
        self,
        small_file_id: str | EllipsisType = ...,
        small_file_unique_id: str | EllipsisType = ...,
        big_file_id: str | EllipsisType = ...,
        big_file_unique_id: str | EllipsisType = ...,
    ) -> ChatPhoto:
        """Replaces some of model's fields with provided ones"""
        return ChatPhoto(
            small_file_id=small_file_id
            if small_file_id is not ...
            else self.small_file_id,
            small_file_unique_id=small_file_unique_id
            if small_file_unique_id is not ...
            else self.small_file_unique_id,
            big_file_id=big_file_id if big_file_id is not ... else self.big_file_id,
            big_file_unique_id=big_file_unique_id
            if big_file_unique_id is not ...
            else self.big_file_unique_id,
        )


@dataclass(frozen=False, slots=True)
class ChatInviteLink:
    """Represents an invite link for a chat."""

    invite_link: str
    """The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "...". """
    creator: User
    """Creator of the link """
    creates_join_request: bool
    """True, if users joining the chat via the link need to be approved by chat administrators """
    is_primary: bool
    """True, if the link is primary """
    is_revoked: bool
    """True, if the link is revoked """
    name: str | None = None
    """Optional. Invite link name """
    expire_date: int | None = None
    """Optional. Point in time (Unix timestamp) when the link will expire or has been expired """
    member_limit: int | None = None
    """Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 """
    pending_join_request_count: int | None = None
    """Optional. Number of pending join requests created using this link """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        invite_link: AlterFn[str] | EllipsisType = ...,
        creator: AlterFn[User] | EllipsisType = ...,
        creates_join_request: AlterFn[bool] | EllipsisType = ...,
        is_primary: AlterFn[bool] | EllipsisType = ...,
        is_revoked: AlterFn[bool] | EllipsisType = ...,
        name: AlterFn[str | None] | EllipsisType = ...,
        expire_date: AlterFn[int | None] | EllipsisType = ...,
        member_limit: AlterFn[int | None] | EllipsisType = ...,
        pending_join_request_count: AlterFn[int | None] | EllipsisType = ...,
    ) -> ChatInviteLink:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatInviteLink(
            invite_link=self.invite_link
            if invite_link is ...
            else prefer(invite_link(self.invite_link), self.invite_link),
            creator=self.creator
            if creator is ...
            else prefer(creator(self.creator), self.creator),
            creates_join_request=self.creates_join_request
            if creates_join_request is ...
            else prefer(
                creates_join_request(self.creates_join_request),
                self.creates_join_request,
            ),
            is_primary=self.is_primary
            if is_primary is ...
            else prefer(is_primary(self.is_primary), self.is_primary),
            is_revoked=self.is_revoked
            if is_revoked is ...
            else prefer(is_revoked(self.is_revoked), self.is_revoked),
            name=self.name if name is ... else prefer(name(self.name), self.name),
            expire_date=self.expire_date
            if expire_date is ...
            else prefer(expire_date(self.expire_date), self.expire_date),
            member_limit=self.member_limit
            if member_limit is ...
            else prefer(member_limit(self.member_limit), self.member_limit),
            pending_join_request_count=self.pending_join_request_count
            if pending_join_request_count is ...
            else prefer(
                pending_join_request_count(self.pending_join_request_count),
                self.pending_join_request_count,
            ),
        )

    def copy_with(
        self,
        invite_link: str | EllipsisType = ...,
        creator: User | EllipsisType = ...,
        creates_join_request: bool | EllipsisType = ...,
        is_primary: bool | EllipsisType = ...,
        is_revoked: bool | EllipsisType = ...,
        name: str | None | EllipsisType = ...,
        expire_date: int | None | EllipsisType = ...,
        member_limit: int | None | EllipsisType = ...,
        pending_join_request_count: int | None | EllipsisType = ...,
    ) -> ChatInviteLink:
        """Replaces some of model's fields with provided ones"""
        return ChatInviteLink(
            invite_link=invite_link if invite_link is not ... else self.invite_link,
            creator=creator if creator is not ... else self.creator,
            creates_join_request=creates_join_request
            if creates_join_request is not ...
            else self.creates_join_request,
            is_primary=is_primary if is_primary is not ... else self.is_primary,
            is_revoked=is_revoked if is_revoked is not ... else self.is_revoked,
            name=name if name is not ... else self.name,
            expire_date=expire_date if expire_date is not ... else self.expire_date,
            member_limit=member_limit if member_limit is not ... else self.member_limit,
            pending_join_request_count=pending_join_request_count
            if pending_join_request_count is not ...
            else self.pending_join_request_count,
        )


@dataclass(frozen=False, slots=True)
class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat."""

    is_anonymous: bool
    """True, if the user's presence in the chat is hidden """
    can_manage_chat: bool
    """True, if the administrator can access the chat event log, boost list in channels, see channel members, report spam messages, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege """
    can_delete_messages: bool
    """True, if the administrator can delete messages of other users """
    can_manage_video_chats: bool
    """True, if the administrator can manage video chats """
    can_restrict_members: bool
    """True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics """
    can_promote_members: bool
    """True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) """
    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other settings """
    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat """
    can_post_messages: bool | None = None
    """Optional. True, if the administrator can post messages in the channel, or access channel statistics; channels only """
    can_edit_messages: bool | None = None
    """Optional. True, if the administrator can edit messages of other users and can pin messages; channels only """
    can_pin_messages: bool | None = None
    """Optional. True, if the user is allowed to pin messages; groups and supergroups only """
    can_post_stories: bool | None = None
    """Optional. True, if the administrator can post stories in the channel; channels only """
    can_edit_stories: bool | None = None
    """Optional. True, if the administrator can edit stories posted by other users; channels only """
    can_delete_stories: bool | None = None
    """Optional. True, if the administrator can delete stories posted by other users; channels only """
    can_manage_topics: bool | None = None
    """Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        is_anonymous: AlterFn[bool] | EllipsisType = ...,
        can_manage_chat: AlterFn[bool] | EllipsisType = ...,
        can_delete_messages: AlterFn[bool] | EllipsisType = ...,
        can_manage_video_chats: AlterFn[bool] | EllipsisType = ...,
        can_restrict_members: AlterFn[bool] | EllipsisType = ...,
        can_promote_members: AlterFn[bool] | EllipsisType = ...,
        can_change_info: AlterFn[bool] | EllipsisType = ...,
        can_invite_users: AlterFn[bool] | EllipsisType = ...,
        can_post_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_edit_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_pin_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_post_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_edit_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_delete_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_manage_topics: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ChatAdministratorRights:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatAdministratorRights(
            is_anonymous=self.is_anonymous
            if is_anonymous is ...
            else prefer(is_anonymous(self.is_anonymous), self.is_anonymous),
            can_manage_chat=self.can_manage_chat
            if can_manage_chat is ...
            else prefer(can_manage_chat(self.can_manage_chat), self.can_manage_chat),
            can_delete_messages=self.can_delete_messages
            if can_delete_messages is ...
            else prefer(
                can_delete_messages(self.can_delete_messages), self.can_delete_messages
            ),
            can_manage_video_chats=self.can_manage_video_chats
            if can_manage_video_chats is ...
            else prefer(
                can_manage_video_chats(self.can_manage_video_chats),
                self.can_manage_video_chats,
            ),
            can_restrict_members=self.can_restrict_members
            if can_restrict_members is ...
            else prefer(
                can_restrict_members(self.can_restrict_members),
                self.can_restrict_members,
            ),
            can_promote_members=self.can_promote_members
            if can_promote_members is ...
            else prefer(
                can_promote_members(self.can_promote_members), self.can_promote_members
            ),
            can_change_info=self.can_change_info
            if can_change_info is ...
            else prefer(can_change_info(self.can_change_info), self.can_change_info),
            can_invite_users=self.can_invite_users
            if can_invite_users is ...
            else prefer(can_invite_users(self.can_invite_users), self.can_invite_users),
            can_post_messages=self.can_post_messages
            if can_post_messages is ...
            else prefer(
                can_post_messages(self.can_post_messages), self.can_post_messages
            ),
            can_edit_messages=self.can_edit_messages
            if can_edit_messages is ...
            else prefer(
                can_edit_messages(self.can_edit_messages), self.can_edit_messages
            ),
            can_pin_messages=self.can_pin_messages
            if can_pin_messages is ...
            else prefer(can_pin_messages(self.can_pin_messages), self.can_pin_messages),
            can_post_stories=self.can_post_stories
            if can_post_stories is ...
            else prefer(can_post_stories(self.can_post_stories), self.can_post_stories),
            can_edit_stories=self.can_edit_stories
            if can_edit_stories is ...
            else prefer(can_edit_stories(self.can_edit_stories), self.can_edit_stories),
            can_delete_stories=self.can_delete_stories
            if can_delete_stories is ...
            else prefer(
                can_delete_stories(self.can_delete_stories), self.can_delete_stories
            ),
            can_manage_topics=self.can_manage_topics
            if can_manage_topics is ...
            else prefer(
                can_manage_topics(self.can_manage_topics), self.can_manage_topics
            ),
        )

    def copy_with(
        self,
        is_anonymous: bool | EllipsisType = ...,
        can_manage_chat: bool | EllipsisType = ...,
        can_delete_messages: bool | EllipsisType = ...,
        can_manage_video_chats: bool | EllipsisType = ...,
        can_restrict_members: bool | EllipsisType = ...,
        can_promote_members: bool | EllipsisType = ...,
        can_change_info: bool | EllipsisType = ...,
        can_invite_users: bool | EllipsisType = ...,
        can_post_messages: bool | None | EllipsisType = ...,
        can_edit_messages: bool | None | EllipsisType = ...,
        can_pin_messages: bool | None | EllipsisType = ...,
        can_post_stories: bool | None | EllipsisType = ...,
        can_edit_stories: bool | None | EllipsisType = ...,
        can_delete_stories: bool | None | EllipsisType = ...,
        can_manage_topics: bool | None | EllipsisType = ...,
    ) -> ChatAdministratorRights:
        """Replaces some of model's fields with provided ones"""
        return ChatAdministratorRights(
            is_anonymous=is_anonymous if is_anonymous is not ... else self.is_anonymous,
            can_manage_chat=can_manage_chat
            if can_manage_chat is not ...
            else self.can_manage_chat,
            can_delete_messages=can_delete_messages
            if can_delete_messages is not ...
            else self.can_delete_messages,
            can_manage_video_chats=can_manage_video_chats
            if can_manage_video_chats is not ...
            else self.can_manage_video_chats,
            can_restrict_members=can_restrict_members
            if can_restrict_members is not ...
            else self.can_restrict_members,
            can_promote_members=can_promote_members
            if can_promote_members is not ...
            else self.can_promote_members,
            can_change_info=can_change_info
            if can_change_info is not ...
            else self.can_change_info,
            can_invite_users=can_invite_users
            if can_invite_users is not ...
            else self.can_invite_users,
            can_post_messages=can_post_messages
            if can_post_messages is not ...
            else self.can_post_messages,
            can_edit_messages=can_edit_messages
            if can_edit_messages is not ...
            else self.can_edit_messages,
            can_pin_messages=can_pin_messages
            if can_pin_messages is not ...
            else self.can_pin_messages,
            can_post_stories=can_post_stories
            if can_post_stories is not ...
            else self.can_post_stories,
            can_edit_stories=can_edit_stories
            if can_edit_stories is not ...
            else self.can_edit_stories,
            can_delete_stories=can_delete_stories
            if can_delete_stories is not ...
            else self.can_delete_stories,
            can_manage_topics=can_manage_topics
            if can_manage_topics is not ...
            else self.can_manage_topics,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges."""

    status: str
    """The member's status in the chat, always "creator" """
    user: User
    """Information about the user """
    is_anonymous: bool
    """True, if the user's presence in the chat is hidden """
    custom_title: str | None = None
    """Optional. Custom title for this user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
        is_anonymous: AlterFn[bool] | EllipsisType = ...,
        custom_title: AlterFn[str | None] | EllipsisType = ...,
    ) -> ChatMemberOwner:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberOwner(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            is_anonymous=self.is_anonymous
            if is_anonymous is ...
            else prefer(is_anonymous(self.is_anonymous), self.is_anonymous),
            custom_title=self.custom_title
            if custom_title is ...
            else prefer(custom_title(self.custom_title), self.custom_title),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
        is_anonymous: bool | EllipsisType = ...,
        custom_title: str | None | EllipsisType = ...,
    ) -> ChatMemberOwner:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberOwner(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
            is_anonymous=is_anonymous if is_anonymous is not ... else self.is_anonymous,
            custom_title=custom_title if custom_title is not ... else self.custom_title,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberAdministrator:
    """Represents a chat member that has some additional privileges."""

    status: str
    """The member's status in the chat, always "administrator" """
    user: User
    """Information about the user """
    can_be_edited: bool
    """True, if the bot is allowed to edit administrator privileges of that user """
    is_anonymous: bool
    """True, if the user's presence in the chat is hidden """
    can_manage_chat: bool
    """True, if the administrator can access the chat event log, boost list in channels, see channel members, report spam messages, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege """
    can_delete_messages: bool
    """True, if the administrator can delete messages of other users """
    can_manage_video_chats: bool
    """True, if the administrator can manage video chats """
    can_restrict_members: bool
    """True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics """
    can_promote_members: bool
    """True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) """
    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other settings """
    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat """
    can_post_messages: bool | None = None
    """Optional. True, if the administrator can post messages in the channel, or access channel statistics; channels only """
    can_edit_messages: bool | None = None
    """Optional. True, if the administrator can edit messages of other users and can pin messages; channels only """
    can_pin_messages: bool | None = None
    """Optional. True, if the user is allowed to pin messages; groups and supergroups only """
    can_post_stories: bool | None = None
    """Optional. True, if the administrator can post stories in the channel; channels only """
    can_edit_stories: bool | None = None
    """Optional. True, if the administrator can edit stories posted by other users; channels only """
    can_delete_stories: bool | None = None
    """Optional. True, if the administrator can delete stories posted by other users; channels only """
    can_manage_topics: bool | None = None
    """Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only """
    custom_title: str | None = None
    """Optional. Custom title for this user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
        can_be_edited: AlterFn[bool] | EllipsisType = ...,
        is_anonymous: AlterFn[bool] | EllipsisType = ...,
        can_manage_chat: AlterFn[bool] | EllipsisType = ...,
        can_delete_messages: AlterFn[bool] | EllipsisType = ...,
        can_manage_video_chats: AlterFn[bool] | EllipsisType = ...,
        can_restrict_members: AlterFn[bool] | EllipsisType = ...,
        can_promote_members: AlterFn[bool] | EllipsisType = ...,
        can_change_info: AlterFn[bool] | EllipsisType = ...,
        can_invite_users: AlterFn[bool] | EllipsisType = ...,
        can_post_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_edit_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_pin_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_post_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_edit_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_delete_stories: AlterFn[bool | None] | EllipsisType = ...,
        can_manage_topics: AlterFn[bool | None] | EllipsisType = ...,
        custom_title: AlterFn[str | None] | EllipsisType = ...,
    ) -> ChatMemberAdministrator:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberAdministrator(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            can_be_edited=self.can_be_edited
            if can_be_edited is ...
            else prefer(can_be_edited(self.can_be_edited), self.can_be_edited),
            is_anonymous=self.is_anonymous
            if is_anonymous is ...
            else prefer(is_anonymous(self.is_anonymous), self.is_anonymous),
            can_manage_chat=self.can_manage_chat
            if can_manage_chat is ...
            else prefer(can_manage_chat(self.can_manage_chat), self.can_manage_chat),
            can_delete_messages=self.can_delete_messages
            if can_delete_messages is ...
            else prefer(
                can_delete_messages(self.can_delete_messages), self.can_delete_messages
            ),
            can_manage_video_chats=self.can_manage_video_chats
            if can_manage_video_chats is ...
            else prefer(
                can_manage_video_chats(self.can_manage_video_chats),
                self.can_manage_video_chats,
            ),
            can_restrict_members=self.can_restrict_members
            if can_restrict_members is ...
            else prefer(
                can_restrict_members(self.can_restrict_members),
                self.can_restrict_members,
            ),
            can_promote_members=self.can_promote_members
            if can_promote_members is ...
            else prefer(
                can_promote_members(self.can_promote_members), self.can_promote_members
            ),
            can_change_info=self.can_change_info
            if can_change_info is ...
            else prefer(can_change_info(self.can_change_info), self.can_change_info),
            can_invite_users=self.can_invite_users
            if can_invite_users is ...
            else prefer(can_invite_users(self.can_invite_users), self.can_invite_users),
            can_post_messages=self.can_post_messages
            if can_post_messages is ...
            else prefer(
                can_post_messages(self.can_post_messages), self.can_post_messages
            ),
            can_edit_messages=self.can_edit_messages
            if can_edit_messages is ...
            else prefer(
                can_edit_messages(self.can_edit_messages), self.can_edit_messages
            ),
            can_pin_messages=self.can_pin_messages
            if can_pin_messages is ...
            else prefer(can_pin_messages(self.can_pin_messages), self.can_pin_messages),
            can_post_stories=self.can_post_stories
            if can_post_stories is ...
            else prefer(can_post_stories(self.can_post_stories), self.can_post_stories),
            can_edit_stories=self.can_edit_stories
            if can_edit_stories is ...
            else prefer(can_edit_stories(self.can_edit_stories), self.can_edit_stories),
            can_delete_stories=self.can_delete_stories
            if can_delete_stories is ...
            else prefer(
                can_delete_stories(self.can_delete_stories), self.can_delete_stories
            ),
            can_manage_topics=self.can_manage_topics
            if can_manage_topics is ...
            else prefer(
                can_manage_topics(self.can_manage_topics), self.can_manage_topics
            ),
            custom_title=self.custom_title
            if custom_title is ...
            else prefer(custom_title(self.custom_title), self.custom_title),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
        can_be_edited: bool | EllipsisType = ...,
        is_anonymous: bool | EllipsisType = ...,
        can_manage_chat: bool | EllipsisType = ...,
        can_delete_messages: bool | EllipsisType = ...,
        can_manage_video_chats: bool | EllipsisType = ...,
        can_restrict_members: bool | EllipsisType = ...,
        can_promote_members: bool | EllipsisType = ...,
        can_change_info: bool | EllipsisType = ...,
        can_invite_users: bool | EllipsisType = ...,
        can_post_messages: bool | None | EllipsisType = ...,
        can_edit_messages: bool | None | EllipsisType = ...,
        can_pin_messages: bool | None | EllipsisType = ...,
        can_post_stories: bool | None | EllipsisType = ...,
        can_edit_stories: bool | None | EllipsisType = ...,
        can_delete_stories: bool | None | EllipsisType = ...,
        can_manage_topics: bool | None | EllipsisType = ...,
        custom_title: str | None | EllipsisType = ...,
    ) -> ChatMemberAdministrator:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberAdministrator(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
            can_be_edited=can_be_edited
            if can_be_edited is not ...
            else self.can_be_edited,
            is_anonymous=is_anonymous if is_anonymous is not ... else self.is_anonymous,
            can_manage_chat=can_manage_chat
            if can_manage_chat is not ...
            else self.can_manage_chat,
            can_delete_messages=can_delete_messages
            if can_delete_messages is not ...
            else self.can_delete_messages,
            can_manage_video_chats=can_manage_video_chats
            if can_manage_video_chats is not ...
            else self.can_manage_video_chats,
            can_restrict_members=can_restrict_members
            if can_restrict_members is not ...
            else self.can_restrict_members,
            can_promote_members=can_promote_members
            if can_promote_members is not ...
            else self.can_promote_members,
            can_change_info=can_change_info
            if can_change_info is not ...
            else self.can_change_info,
            can_invite_users=can_invite_users
            if can_invite_users is not ...
            else self.can_invite_users,
            can_post_messages=can_post_messages
            if can_post_messages is not ...
            else self.can_post_messages,
            can_edit_messages=can_edit_messages
            if can_edit_messages is not ...
            else self.can_edit_messages,
            can_pin_messages=can_pin_messages
            if can_pin_messages is not ...
            else self.can_pin_messages,
            can_post_stories=can_post_stories
            if can_post_stories is not ...
            else self.can_post_stories,
            can_edit_stories=can_edit_stories
            if can_edit_stories is not ...
            else self.can_edit_stories,
            can_delete_stories=can_delete_stories
            if can_delete_stories is not ...
            else self.can_delete_stories,
            can_manage_topics=can_manage_topics
            if can_manage_topics is not ...
            else self.can_manage_topics,
            custom_title=custom_title if custom_title is not ... else self.custom_title,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberMember:
    """Represents a chat member that has no additional privileges or restrictions."""

    status: str
    """The member's status in the chat, always "member" """
    user: User
    """Information about the user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
    ) -> ChatMemberMember:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberMember(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
    ) -> ChatMemberMember:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberMember(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only."""

    status: str
    """The member's status in the chat, always "restricted" """
    user: User
    """Information about the user """
    is_member: bool
    """True, if the user is a member of the chat at the moment of the request """
    can_send_messages: bool
    """True, if the user is allowed to send text messages, contacts, invoices, locations and venues """
    can_send_audios: bool
    """True, if the user is allowed to send audios """
    can_send_documents: bool
    """True, if the user is allowed to send documents """
    can_send_photos: bool
    """True, if the user is allowed to send photos """
    can_send_videos: bool
    """True, if the user is allowed to send videos """
    can_send_video_notes: bool
    """True, if the user is allowed to send video notes """
    can_send_voice_notes: bool
    """True, if the user is allowed to send voice notes """
    can_send_polls: bool
    """True, if the user is allowed to send polls """
    can_send_other_messages: bool
    """True, if the user is allowed to send animations, games, stickers and use inline bots """
    can_add_web_page_previews: bool
    """True, if the user is allowed to add web page previews to their messages """
    can_change_info: bool
    """True, if the user is allowed to change the chat title, photo and other settings """
    can_invite_users: bool
    """True, if the user is allowed to invite new users to the chat """
    can_pin_messages: bool
    """True, if the user is allowed to pin messages """
    can_manage_topics: bool
    """True, if the user is allowed to create forum topics """
    until_date: int
    """Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
        is_member: AlterFn[bool] | EllipsisType = ...,
        can_send_messages: AlterFn[bool] | EllipsisType = ...,
        can_send_audios: AlterFn[bool] | EllipsisType = ...,
        can_send_documents: AlterFn[bool] | EllipsisType = ...,
        can_send_photos: AlterFn[bool] | EllipsisType = ...,
        can_send_videos: AlterFn[bool] | EllipsisType = ...,
        can_send_video_notes: AlterFn[bool] | EllipsisType = ...,
        can_send_voice_notes: AlterFn[bool] | EllipsisType = ...,
        can_send_polls: AlterFn[bool] | EllipsisType = ...,
        can_send_other_messages: AlterFn[bool] | EllipsisType = ...,
        can_add_web_page_previews: AlterFn[bool] | EllipsisType = ...,
        can_change_info: AlterFn[bool] | EllipsisType = ...,
        can_invite_users: AlterFn[bool] | EllipsisType = ...,
        can_pin_messages: AlterFn[bool] | EllipsisType = ...,
        can_manage_topics: AlterFn[bool] | EllipsisType = ...,
        until_date: AlterFn[int] | EllipsisType = ...,
    ) -> ChatMemberRestricted:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberRestricted(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            is_member=self.is_member
            if is_member is ...
            else prefer(is_member(self.is_member), self.is_member),
            can_send_messages=self.can_send_messages
            if can_send_messages is ...
            else prefer(
                can_send_messages(self.can_send_messages), self.can_send_messages
            ),
            can_send_audios=self.can_send_audios
            if can_send_audios is ...
            else prefer(can_send_audios(self.can_send_audios), self.can_send_audios),
            can_send_documents=self.can_send_documents
            if can_send_documents is ...
            else prefer(
                can_send_documents(self.can_send_documents), self.can_send_documents
            ),
            can_send_photos=self.can_send_photos
            if can_send_photos is ...
            else prefer(can_send_photos(self.can_send_photos), self.can_send_photos),
            can_send_videos=self.can_send_videos
            if can_send_videos is ...
            else prefer(can_send_videos(self.can_send_videos), self.can_send_videos),
            can_send_video_notes=self.can_send_video_notes
            if can_send_video_notes is ...
            else prefer(
                can_send_video_notes(self.can_send_video_notes),
                self.can_send_video_notes,
            ),
            can_send_voice_notes=self.can_send_voice_notes
            if can_send_voice_notes is ...
            else prefer(
                can_send_voice_notes(self.can_send_voice_notes),
                self.can_send_voice_notes,
            ),
            can_send_polls=self.can_send_polls
            if can_send_polls is ...
            else prefer(can_send_polls(self.can_send_polls), self.can_send_polls),
            can_send_other_messages=self.can_send_other_messages
            if can_send_other_messages is ...
            else prefer(
                can_send_other_messages(self.can_send_other_messages),
                self.can_send_other_messages,
            ),
            can_add_web_page_previews=self.can_add_web_page_previews
            if can_add_web_page_previews is ...
            else prefer(
                can_add_web_page_previews(self.can_add_web_page_previews),
                self.can_add_web_page_previews,
            ),
            can_change_info=self.can_change_info
            if can_change_info is ...
            else prefer(can_change_info(self.can_change_info), self.can_change_info),
            can_invite_users=self.can_invite_users
            if can_invite_users is ...
            else prefer(can_invite_users(self.can_invite_users), self.can_invite_users),
            can_pin_messages=self.can_pin_messages
            if can_pin_messages is ...
            else prefer(can_pin_messages(self.can_pin_messages), self.can_pin_messages),
            can_manage_topics=self.can_manage_topics
            if can_manage_topics is ...
            else prefer(
                can_manage_topics(self.can_manage_topics), self.can_manage_topics
            ),
            until_date=self.until_date
            if until_date is ...
            else prefer(until_date(self.until_date), self.until_date),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
        is_member: bool | EllipsisType = ...,
        can_send_messages: bool | EllipsisType = ...,
        can_send_audios: bool | EllipsisType = ...,
        can_send_documents: bool | EllipsisType = ...,
        can_send_photos: bool | EllipsisType = ...,
        can_send_videos: bool | EllipsisType = ...,
        can_send_video_notes: bool | EllipsisType = ...,
        can_send_voice_notes: bool | EllipsisType = ...,
        can_send_polls: bool | EllipsisType = ...,
        can_send_other_messages: bool | EllipsisType = ...,
        can_add_web_page_previews: bool | EllipsisType = ...,
        can_change_info: bool | EllipsisType = ...,
        can_invite_users: bool | EllipsisType = ...,
        can_pin_messages: bool | EllipsisType = ...,
        can_manage_topics: bool | EllipsisType = ...,
        until_date: int | EllipsisType = ...,
    ) -> ChatMemberRestricted:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberRestricted(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
            is_member=is_member if is_member is not ... else self.is_member,
            can_send_messages=can_send_messages
            if can_send_messages is not ...
            else self.can_send_messages,
            can_send_audios=can_send_audios
            if can_send_audios is not ...
            else self.can_send_audios,
            can_send_documents=can_send_documents
            if can_send_documents is not ...
            else self.can_send_documents,
            can_send_photos=can_send_photos
            if can_send_photos is not ...
            else self.can_send_photos,
            can_send_videos=can_send_videos
            if can_send_videos is not ...
            else self.can_send_videos,
            can_send_video_notes=can_send_video_notes
            if can_send_video_notes is not ...
            else self.can_send_video_notes,
            can_send_voice_notes=can_send_voice_notes
            if can_send_voice_notes is not ...
            else self.can_send_voice_notes,
            can_send_polls=can_send_polls
            if can_send_polls is not ...
            else self.can_send_polls,
            can_send_other_messages=can_send_other_messages
            if can_send_other_messages is not ...
            else self.can_send_other_messages,
            can_add_web_page_previews=can_add_web_page_previews
            if can_add_web_page_previews is not ...
            else self.can_add_web_page_previews,
            can_change_info=can_change_info
            if can_change_info is not ...
            else self.can_change_info,
            can_invite_users=can_invite_users
            if can_invite_users is not ...
            else self.can_invite_users,
            can_pin_messages=can_pin_messages
            if can_pin_messages is not ...
            else self.can_pin_messages,
            can_manage_topics=can_manage_topics
            if can_manage_topics is not ...
            else self.can_manage_topics,
            until_date=until_date if until_date is not ... else self.until_date,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberLeft:
    """Represents a chat member that isn't currently a member of the chat, but may join it themselves."""

    status: str
    """The member's status in the chat, always "left" """
    user: User
    """Information about the user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
    ) -> ChatMemberLeft:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberLeft(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
    ) -> ChatMemberLeft:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberLeft(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."""

    status: str
    """The member's status in the chat, always "kicked" """
    user: User
    """Information about the user """
    until_date: int
    """Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        status: AlterFn[str] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
        until_date: AlterFn[int] | EllipsisType = ...,
    ) -> ChatMemberBanned:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberBanned(
            status=self.status
            if status is ...
            else prefer(status(self.status), self.status),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            until_date=self.until_date
            if until_date is ...
            else prefer(until_date(self.until_date), self.until_date),
        )

    def copy_with(
        self,
        status: str | EllipsisType = ...,
        user: User | EllipsisType = ...,
        until_date: int | EllipsisType = ...,
    ) -> ChatMemberBanned:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberBanned(
            status=status if status is not ... else self.status,
            user=user if user is not ... else self.user,
            until_date=until_date if until_date is not ... else self.until_date,
        )


@dataclass(frozen=False, slots=True)
class ChatMemberUpdated:
    """This object represents changes in the status of a chat member."""

    chat: Chat
    """Chat the user belongs to """
    from_: User
    """Performer of the action, which resulted in the change """
    date: int
    """Date the change was done in Unix time """
    old_chat_member: ChatMember
    """Previous information about the chat member """
    new_chat_member: ChatMember
    """New information about the chat member """
    invite_link: ChatInviteLink | None = None
    """Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only. """
    via_chat_folder_invite_link: bool | None = None
    """Optional. True, if the user joined the chat via a chat folder invite link """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        chat: AlterFn[Chat] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        date: AlterFn[int] | EllipsisType = ...,
        old_chat_member: AlterFn[ChatMember] | EllipsisType = ...,
        new_chat_member: AlterFn[ChatMember] | EllipsisType = ...,
        invite_link: AlterFn[ChatInviteLink | None] | EllipsisType = ...,
        via_chat_folder_invite_link: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ChatMemberUpdated:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatMemberUpdated(
            chat=self.chat if chat is ... else prefer(chat(self.chat), self.chat),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            date=self.date if date is ... else prefer(date(self.date), self.date),
            old_chat_member=self.old_chat_member
            if old_chat_member is ...
            else prefer(old_chat_member(self.old_chat_member), self.old_chat_member),
            new_chat_member=self.new_chat_member
            if new_chat_member is ...
            else prefer(new_chat_member(self.new_chat_member), self.new_chat_member),
            invite_link=self.invite_link
            if invite_link is ...
            else prefer(invite_link(self.invite_link), self.invite_link),
            via_chat_folder_invite_link=self.via_chat_folder_invite_link
            if via_chat_folder_invite_link is ...
            else prefer(
                via_chat_folder_invite_link(self.via_chat_folder_invite_link),
                self.via_chat_folder_invite_link,
            ),
        )

    def copy_with(
        self,
        chat: Chat | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        date: int | EllipsisType = ...,
        old_chat_member: ChatMember | EllipsisType = ...,
        new_chat_member: ChatMember | EllipsisType = ...,
        invite_link: ChatInviteLink | None | EllipsisType = ...,
        via_chat_folder_invite_link: bool | None | EllipsisType = ...,
    ) -> ChatMemberUpdated:
        """Replaces some of model's fields with provided ones"""
        return ChatMemberUpdated(
            chat=chat if chat is not ... else self.chat,
            from_=from_ if from_ is not ... else self.from_,
            date=date if date is not ... else self.date,
            old_chat_member=old_chat_member
            if old_chat_member is not ...
            else self.old_chat_member,
            new_chat_member=new_chat_member
            if new_chat_member is not ...
            else self.new_chat_member,
            invite_link=invite_link if invite_link is not ... else self.invite_link,
            via_chat_folder_invite_link=via_chat_folder_invite_link
            if via_chat_folder_invite_link is not ...
            else self.via_chat_folder_invite_link,
        )


@dataclass(frozen=False, slots=True)
class ChatJoinRequest:
    """Represents a join request sent to a chat."""

    chat: Chat
    """Chat to which the request was sent """
    from_: User
    """User that sent the join request """
    user_chat_id: int
    """Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user. """
    date: int
    """Date the request was sent in Unix time """
    bio: str | None = None
    """Optional. Bio of the user. """
    invite_link: ChatInviteLink | None = None
    """Optional. Chat invite link that was used by the user to send the join request """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        chat: AlterFn[Chat] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        user_chat_id: AlterFn[int] | EllipsisType = ...,
        date: AlterFn[int] | EllipsisType = ...,
        bio: AlterFn[str | None] | EllipsisType = ...,
        invite_link: AlterFn[ChatInviteLink | None] | EllipsisType = ...,
    ) -> ChatJoinRequest:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatJoinRequest(
            chat=self.chat if chat is ... else prefer(chat(self.chat), self.chat),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            user_chat_id=self.user_chat_id
            if user_chat_id is ...
            else prefer(user_chat_id(self.user_chat_id), self.user_chat_id),
            date=self.date if date is ... else prefer(date(self.date), self.date),
            bio=self.bio if bio is ... else prefer(bio(self.bio), self.bio),
            invite_link=self.invite_link
            if invite_link is ...
            else prefer(invite_link(self.invite_link), self.invite_link),
        )

    def copy_with(
        self,
        chat: Chat | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        user_chat_id: int | EllipsisType = ...,
        date: int | EllipsisType = ...,
        bio: str | None | EllipsisType = ...,
        invite_link: ChatInviteLink | None | EllipsisType = ...,
    ) -> ChatJoinRequest:
        """Replaces some of model's fields with provided ones"""
        return ChatJoinRequest(
            chat=chat if chat is not ... else self.chat,
            from_=from_ if from_ is not ... else self.from_,
            user_chat_id=user_chat_id if user_chat_id is not ... else self.user_chat_id,
            date=date if date is not ... else self.date,
            bio=bio if bio is not ... else self.bio,
            invite_link=invite_link if invite_link is not ... else self.invite_link,
        )


@dataclass(frozen=False, slots=True)
class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat."""

    can_send_messages: bool | None = None
    """Optional. True, if the user is allowed to send text messages, contacts, invoices, locations and venues """
    can_send_audios: bool | None = None
    """Optional. True, if the user is allowed to send audios """
    can_send_documents: bool | None = None
    """Optional. True, if the user is allowed to send documents """
    can_send_photos: bool | None = None
    """Optional. True, if the user is allowed to send photos """
    can_send_videos: bool | None = None
    """Optional. True, if the user is allowed to send videos """
    can_send_video_notes: bool | None = None
    """Optional. True, if the user is allowed to send video notes """
    can_send_voice_notes: bool | None = None
    """Optional. True, if the user is allowed to send voice notes """
    can_send_polls: bool | None = None
    """Optional. True, if the user is allowed to send polls """
    can_send_other_messages: bool | None = None
    """Optional. True, if the user is allowed to send animations, games, stickers and use inline bots """
    can_add_web_page_previews: bool | None = None
    """Optional. True, if the user is allowed to add web page previews to their messages """
    can_change_info: bool | None = None
    """Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups """
    can_invite_users: bool | None = None
    """Optional. True, if the user is allowed to invite new users to the chat """
    can_pin_messages: bool | None = None
    """Optional. True, if the user is allowed to pin messages. Ignored in public supergroups """
    can_manage_topics: bool | None = None
    """Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        can_send_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_send_audios: AlterFn[bool | None] | EllipsisType = ...,
        can_send_documents: AlterFn[bool | None] | EllipsisType = ...,
        can_send_photos: AlterFn[bool | None] | EllipsisType = ...,
        can_send_videos: AlterFn[bool | None] | EllipsisType = ...,
        can_send_video_notes: AlterFn[bool | None] | EllipsisType = ...,
        can_send_voice_notes: AlterFn[bool | None] | EllipsisType = ...,
        can_send_polls: AlterFn[bool | None] | EllipsisType = ...,
        can_send_other_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_add_web_page_previews: AlterFn[bool | None] | EllipsisType = ...,
        can_change_info: AlterFn[bool | None] | EllipsisType = ...,
        can_invite_users: AlterFn[bool | None] | EllipsisType = ...,
        can_pin_messages: AlterFn[bool | None] | EllipsisType = ...,
        can_manage_topics: AlterFn[bool | None] | EllipsisType = ...,
    ) -> ChatPermissions:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatPermissions(
            can_send_messages=self.can_send_messages
            if can_send_messages is ...
            else prefer(
                can_send_messages(self.can_send_messages), self.can_send_messages
            ),
            can_send_audios=self.can_send_audios
            if can_send_audios is ...
            else prefer(can_send_audios(self.can_send_audios), self.can_send_audios),
            can_send_documents=self.can_send_documents
            if can_send_documents is ...
            else prefer(
                can_send_documents(self.can_send_documents), self.can_send_documents
            ),
            can_send_photos=self.can_send_photos
            if can_send_photos is ...
            else prefer(can_send_photos(self.can_send_photos), self.can_send_photos),
            can_send_videos=self.can_send_videos
            if can_send_videos is ...
            else prefer(can_send_videos(self.can_send_videos), self.can_send_videos),
            can_send_video_notes=self.can_send_video_notes
            if can_send_video_notes is ...
            else prefer(
                can_send_video_notes(self.can_send_video_notes),
                self.can_send_video_notes,
            ),
            can_send_voice_notes=self.can_send_voice_notes
            if can_send_voice_notes is ...
            else prefer(
                can_send_voice_notes(self.can_send_voice_notes),
                self.can_send_voice_notes,
            ),
            can_send_polls=self.can_send_polls
            if can_send_polls is ...
            else prefer(can_send_polls(self.can_send_polls), self.can_send_polls),
            can_send_other_messages=self.can_send_other_messages
            if can_send_other_messages is ...
            else prefer(
                can_send_other_messages(self.can_send_other_messages),
                self.can_send_other_messages,
            ),
            can_add_web_page_previews=self.can_add_web_page_previews
            if can_add_web_page_previews is ...
            else prefer(
                can_add_web_page_previews(self.can_add_web_page_previews),
                self.can_add_web_page_previews,
            ),
            can_change_info=self.can_change_info
            if can_change_info is ...
            else prefer(can_change_info(self.can_change_info), self.can_change_info),
            can_invite_users=self.can_invite_users
            if can_invite_users is ...
            else prefer(can_invite_users(self.can_invite_users), self.can_invite_users),
            can_pin_messages=self.can_pin_messages
            if can_pin_messages is ...
            else prefer(can_pin_messages(self.can_pin_messages), self.can_pin_messages),
            can_manage_topics=self.can_manage_topics
            if can_manage_topics is ...
            else prefer(
                can_manage_topics(self.can_manage_topics), self.can_manage_topics
            ),
        )

    def copy_with(
        self,
        can_send_messages: bool | None | EllipsisType = ...,
        can_send_audios: bool | None | EllipsisType = ...,
        can_send_documents: bool | None | EllipsisType = ...,
        can_send_photos: bool | None | EllipsisType = ...,
        can_send_videos: bool | None | EllipsisType = ...,
        can_send_video_notes: bool | None | EllipsisType = ...,
        can_send_voice_notes: bool | None | EllipsisType = ...,
        can_send_polls: bool | None | EllipsisType = ...,
        can_send_other_messages: bool | None | EllipsisType = ...,
        can_add_web_page_previews: bool | None | EllipsisType = ...,
        can_change_info: bool | None | EllipsisType = ...,
        can_invite_users: bool | None | EllipsisType = ...,
        can_pin_messages: bool | None | EllipsisType = ...,
        can_manage_topics: bool | None | EllipsisType = ...,
    ) -> ChatPermissions:
        """Replaces some of model's fields with provided ones"""
        return ChatPermissions(
            can_send_messages=can_send_messages
            if can_send_messages is not ...
            else self.can_send_messages,
            can_send_audios=can_send_audios
            if can_send_audios is not ...
            else self.can_send_audios,
            can_send_documents=can_send_documents
            if can_send_documents is not ...
            else self.can_send_documents,
            can_send_photos=can_send_photos
            if can_send_photos is not ...
            else self.can_send_photos,
            can_send_videos=can_send_videos
            if can_send_videos is not ...
            else self.can_send_videos,
            can_send_video_notes=can_send_video_notes
            if can_send_video_notes is not ...
            else self.can_send_video_notes,
            can_send_voice_notes=can_send_voice_notes
            if can_send_voice_notes is not ...
            else self.can_send_voice_notes,
            can_send_polls=can_send_polls
            if can_send_polls is not ...
            else self.can_send_polls,
            can_send_other_messages=can_send_other_messages
            if can_send_other_messages is not ...
            else self.can_send_other_messages,
            can_add_web_page_previews=can_add_web_page_previews
            if can_add_web_page_previews is not ...
            else self.can_add_web_page_previews,
            can_change_info=can_change_info
            if can_change_info is not ...
            else self.can_change_info,
            can_invite_users=can_invite_users
            if can_invite_users is not ...
            else self.can_invite_users,
            can_pin_messages=can_pin_messages
            if can_pin_messages is not ...
            else self.can_pin_messages,
            can_manage_topics=can_manage_topics
            if can_manage_topics is not ...
            else self.can_manage_topics,
        )


@dataclass(frozen=False, slots=True)
class ChatLocation:
    """Represents a location to which a chat is connected."""

    location: Location
    """The location to which the supergroup is connected. Can't be a live location. """
    address: str
    """Location address; 1-64 characters, as defined by the chat owner """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        location: AlterFn[Location] | EllipsisType = ...,
        address: AlterFn[str] | EllipsisType = ...,
    ) -> ChatLocation:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChatLocation(
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
            address=self.address
            if address is ...
            else prefer(address(self.address), self.address),
        )

    def copy_with(
        self,
        location: Location | EllipsisType = ...,
        address: str | EllipsisType = ...,
    ) -> ChatLocation:
        """Replaces some of model's fields with provided ones"""
        return ChatLocation(
            location=location if location is not ... else self.location,
            address=address if address is not ... else self.address,
        )


@dataclass(frozen=False, slots=True)
class ForumTopic:
    """This object represents a forum topic."""

    message_thread_id: int
    """Unique identifier of the forum topic """
    name: str
    """Name of the topic """
    icon_color: int
    """Color of the topic icon in RGB format """
    icon_custom_emoji_id: str | None = None
    """Optional. Unique identifier of the custom emoji shown as the topic icon """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        message_thread_id: AlterFn[int] | EllipsisType = ...,
        name: AlterFn[str] | EllipsisType = ...,
        icon_color: AlterFn[int] | EllipsisType = ...,
        icon_custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
    ) -> ForumTopic:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ForumTopic(
            message_thread_id=self.message_thread_id
            if message_thread_id is ...
            else prefer(
                message_thread_id(self.message_thread_id), self.message_thread_id
            ),
            name=self.name if name is ... else prefer(name(self.name), self.name),
            icon_color=self.icon_color
            if icon_color is ...
            else prefer(icon_color(self.icon_color), self.icon_color),
            icon_custom_emoji_id=self.icon_custom_emoji_id
            if icon_custom_emoji_id is ...
            else prefer(
                icon_custom_emoji_id(self.icon_custom_emoji_id),
                self.icon_custom_emoji_id,
            ),
        )

    def copy_with(
        self,
        message_thread_id: int | EllipsisType = ...,
        name: str | EllipsisType = ...,
        icon_color: int | EllipsisType = ...,
        icon_custom_emoji_id: str | None | EllipsisType = ...,
    ) -> ForumTopic:
        """Replaces some of model's fields with provided ones"""
        return ForumTopic(
            message_thread_id=message_thread_id
            if message_thread_id is not ...
            else self.message_thread_id,
            name=name if name is not ... else self.name,
            icon_color=icon_color if icon_color is not ... else self.icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id
            if icon_custom_emoji_id is not ...
            else self.icon_custom_emoji_id,
        )


@dataclass(frozen=False, slots=True)
class BotCommand:
    """This object represents a bot command."""

    command: str
    """Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores. """
    description: str
    """Description of the command; 1-256 characters. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        command: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str] | EllipsisType = ...,
    ) -> BotCommand:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommand(
            command=self.command
            if command is ...
            else prefer(command(self.command), self.command),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
        )

    def copy_with(
        self,
        command: str | EllipsisType = ...,
        description: str | EllipsisType = ...,
    ) -> BotCommand:
        """Replaces some of model's fields with provided ones"""
        return BotCommand(
            command=command if command is not ... else self.command,
            description=description if description is not ... else self.description,
        )


@dataclass(frozen=False, slots=True)
class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user."""

    type: str
    """Scope type, must be default """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> BotCommandScopeDefault:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeDefault(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> BotCommandScopeDefault:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeDefault(type=type if type is not ... else self.type)


@dataclass(frozen=False, slots=True)
class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats."""

    type: str
    """Scope type, must be all_private_chats """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> BotCommandScopeAllPrivateChats:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeAllPrivateChats(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> BotCommandScopeAllPrivateChats:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeAllPrivateChats(
            type=type if type is not ... else self.type
        )


@dataclass(frozen=False, slots=True)
class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats."""

    type: str
    """Scope type, must be all_group_chats """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> BotCommandScopeAllGroupChats:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeAllGroupChats(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> BotCommandScopeAllGroupChats:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeAllGroupChats(type=type if type is not ... else self.type)


@dataclass(frozen=False, slots=True)
class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators."""

    type: str
    """Scope type, must be all_chat_administrators """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> BotCommandScopeAllChatAdministrators:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeAllChatAdministrators(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> BotCommandScopeAllChatAdministrators:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeAllChatAdministrators(
            type=type if type is not ... else self.type
        )


@dataclass(frozen=False, slots=True)
class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat."""

    type: str
    """Scope type, must be chat """
    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        chat_id: AlterFn[int | str] | EllipsisType = ...,
    ) -> BotCommandScopeChat:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeChat(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            chat_id=self.chat_id
            if chat_id is ...
            else prefer(chat_id(self.chat_id), self.chat_id),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        chat_id: int | str | EllipsisType = ...,
    ) -> BotCommandScopeChat:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeChat(
            type=type if type is not ... else self.type,
            chat_id=chat_id if chat_id is not ... else self.chat_id,
        )


@dataclass(frozen=False, slots=True)
class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat."""

    type: str
    """Scope type, must be chat_administrators """
    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        chat_id: AlterFn[int | str] | EllipsisType = ...,
    ) -> BotCommandScopeChatAdministrators:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeChatAdministrators(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            chat_id=self.chat_id
            if chat_id is ...
            else prefer(chat_id(self.chat_id), self.chat_id),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        chat_id: int | str | EllipsisType = ...,
    ) -> BotCommandScopeChatAdministrators:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeChatAdministrators(
            type=type if type is not ... else self.type,
            chat_id=chat_id if chat_id is not ... else self.chat_id,
        )


@dataclass(frozen=False, slots=True)
class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat."""

    type: str
    """Scope type, must be chat_member """
    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    user_id: int
    """Unique identifier of the target user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        chat_id: AlterFn[int | str] | EllipsisType = ...,
        user_id: AlterFn[int] | EllipsisType = ...,
    ) -> BotCommandScopeChatMember:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotCommandScopeChatMember(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            chat_id=self.chat_id
            if chat_id is ...
            else prefer(chat_id(self.chat_id), self.chat_id),
            user_id=self.user_id
            if user_id is ...
            else prefer(user_id(self.user_id), self.user_id),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        chat_id: int | str | EllipsisType = ...,
        user_id: int | EllipsisType = ...,
    ) -> BotCommandScopeChatMember:
        """Replaces some of model's fields with provided ones"""
        return BotCommandScopeChatMember(
            type=type if type is not ... else self.type,
            chat_id=chat_id if chat_id is not ... else self.chat_id,
            user_id=user_id if user_id is not ... else self.user_id,
        )


@dataclass(frozen=False, slots=True)
class BotName:
    """This object represents the bot's name."""

    name: str
    """The bot's name """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        name: AlterFn[str] | EllipsisType = ...,
    ) -> BotName:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotName(
            name=self.name if name is ... else prefer(name(self.name), self.name)
        )

    def copy_with(
        self,
        name: str | EllipsisType = ...,
    ) -> BotName:
        """Replaces some of model's fields with provided ones"""
        return BotName(name=name if name is not ... else self.name)


@dataclass(frozen=False, slots=True)
class BotDescription:
    """This object represents the bot's description."""

    description: str
    """The bot's description """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        description: AlterFn[str] | EllipsisType = ...,
    ) -> BotDescription:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotDescription(
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description)
        )

    def copy_with(
        self,
        description: str | EllipsisType = ...,
    ) -> BotDescription:
        """Replaces some of model's fields with provided ones"""
        return BotDescription(
            description=description if description is not ... else self.description
        )


@dataclass(frozen=False, slots=True)
class BotShortDescription:
    """This object represents the bot's short description."""

    short_description: str
    """The bot's short description """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        short_description: AlterFn[str] | EllipsisType = ...,
    ) -> BotShortDescription:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return BotShortDescription(
            short_description=self.short_description
            if short_description is ...
            else prefer(
                short_description(self.short_description), self.short_description
            )
        )

    def copy_with(
        self,
        short_description: str | EllipsisType = ...,
    ) -> BotShortDescription:
        """Replaces some of model's fields with provided ones"""
        return BotShortDescription(
            short_description=short_description
            if short_description is not ...
            else self.short_description
        )


@dataclass(frozen=False, slots=True)
class MenuButtonCommands:
    """Represents a menu button, which opens the bot's list of commands."""

    type: str
    """Type of the button, must be commands """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> MenuButtonCommands:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MenuButtonCommands(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> MenuButtonCommands:
        """Replaces some of model's fields with provided ones"""
        return MenuButtonCommands(type=type if type is not ... else self.type)


@dataclass(frozen=False, slots=True)
class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App."""

    type: str
    """Type of the button, must be web_app """
    text: str
    """Text on the button """
    web_app: WebAppInfo
    """Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        text: AlterFn[str] | EllipsisType = ...,
        web_app: AlterFn[WebAppInfo] | EllipsisType = ...,
    ) -> MenuButtonWebApp:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MenuButtonWebApp(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            text=self.text if text is ... else prefer(text(self.text), self.text),
            web_app=self.web_app
            if web_app is ...
            else prefer(web_app(self.web_app), self.web_app),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        text: str | EllipsisType = ...,
        web_app: WebAppInfo | EllipsisType = ...,
    ) -> MenuButtonWebApp:
        """Replaces some of model's fields with provided ones"""
        return MenuButtonWebApp(
            type=type if type is not ... else self.type,
            text=text if text is not ... else self.text,
            web_app=web_app if web_app is not ... else self.web_app,
        )


@dataclass(frozen=False, slots=True)
class MenuButtonDefault:
    """Describes that no specific value for the menu button was set."""

    type: str
    """Type of the button, must be default """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
    ) -> MenuButtonDefault:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MenuButtonDefault(
            type=self.type if type is ... else prefer(type(self.type), self.type)
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
    ) -> MenuButtonDefault:
        """Replaces some of model's fields with provided ones"""
        return MenuButtonDefault(type=type if type is not ... else self.type)


@dataclass(frozen=False, slots=True)
class ResponseParameters:
    """Describes why a request was unsuccessful."""

    migrate_to_chat_id: int | None = None
    """Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. """
    retry_after: int | None = None
    """Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        migrate_to_chat_id: AlterFn[int | None] | EllipsisType = ...,
        retry_after: AlterFn[int | None] | EllipsisType = ...,
    ) -> ResponseParameters:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ResponseParameters(
            migrate_to_chat_id=self.migrate_to_chat_id
            if migrate_to_chat_id is ...
            else prefer(
                migrate_to_chat_id(self.migrate_to_chat_id), self.migrate_to_chat_id
            ),
            retry_after=self.retry_after
            if retry_after is ...
            else prefer(retry_after(self.retry_after), self.retry_after),
        )

    def copy_with(
        self,
        migrate_to_chat_id: int | None | EllipsisType = ...,
        retry_after: int | None | EllipsisType = ...,
    ) -> ResponseParameters:
        """Replaces some of model's fields with provided ones"""
        return ResponseParameters(
            migrate_to_chat_id=migrate_to_chat_id
            if migrate_to_chat_id is not ...
            else self.migrate_to_chat_id,
            retry_after=retry_after if retry_after is not ... else self.retry_after,
        )


@dataclass(frozen=False, slots=True)
class InputMediaPhoto:
    """Represents a photo to be sent."""

    type: str
    """Type of the result, must be photo """
    media: str
    """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    has_spoiler: bool | None = None
    """Optional. Pass True if the photo needs to be covered with a spoiler animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        media: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        has_spoiler: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputMediaPhoto:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputMediaPhoto(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            media=self.media if media is ... else prefer(media(self.media), self.media),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            has_spoiler=self.has_spoiler
            if has_spoiler is ...
            else prefer(has_spoiler(self.has_spoiler), self.has_spoiler),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        media: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        has_spoiler: bool | None | EllipsisType = ...,
    ) -> InputMediaPhoto:
        """Replaces some of model's fields with provided ones"""
        return InputMediaPhoto(
            type=type if type is not ... else self.type,
            media=media if media is not ... else self.media,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            has_spoiler=has_spoiler if has_spoiler is not ... else self.has_spoiler,
        )


@dataclass(frozen=False, slots=True)
class InputMediaVideo:
    """Represents a video to be sent."""

    type: str
    """Type of the result, must be video """
    media: str
    """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    thumbnail: IOBase | str | None = None
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    width: int | None = None
    """Optional. Video width """
    height: int | None = None
    """Optional. Video height """
    duration: int | None = None
    """Optional. Video duration in seconds """
    supports_streaming: bool | None = None
    """Optional. Pass True if the uploaded video is suitable for streaming """
    has_spoiler: bool | None = None
    """Optional. Pass True if the video needs to be covered with a spoiler animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.thumbnail, IOBase):
            dest[str(id(self.thumbnail))] = self.thumbnail

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        media: AlterFn[str] | EllipsisType = ...,
        thumbnail: AlterFn[IOBase | str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        width: AlterFn[int | None] | EllipsisType = ...,
        height: AlterFn[int | None] | EllipsisType = ...,
        duration: AlterFn[int | None] | EllipsisType = ...,
        supports_streaming: AlterFn[bool | None] | EllipsisType = ...,
        has_spoiler: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputMediaVideo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputMediaVideo(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            media=self.media if media is ... else prefer(media(self.media), self.media),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            supports_streaming=self.supports_streaming
            if supports_streaming is ...
            else prefer(
                supports_streaming(self.supports_streaming), self.supports_streaming
            ),
            has_spoiler=self.has_spoiler
            if has_spoiler is ...
            else prefer(has_spoiler(self.has_spoiler), self.has_spoiler),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        media: str | EllipsisType = ...,
        thumbnail: IOBase | str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        width: int | None | EllipsisType = ...,
        height: int | None | EllipsisType = ...,
        duration: int | None | EllipsisType = ...,
        supports_streaming: bool | None | EllipsisType = ...,
        has_spoiler: bool | None | EllipsisType = ...,
    ) -> InputMediaVideo:
        """Replaces some of model's fields with provided ones"""
        return InputMediaVideo(
            type=type if type is not ... else self.type,
            media=media if media is not ... else self.media,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            duration=duration if duration is not ... else self.duration,
            supports_streaming=supports_streaming
            if supports_streaming is not ...
            else self.supports_streaming,
            has_spoiler=has_spoiler if has_spoiler is not ... else self.has_spoiler,
        )


@dataclass(frozen=False, slots=True)
class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent."""

    type: str
    """Type of the result, must be animation """
    media: str
    """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    thumbnail: IOBase | str | None = None
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the animation caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    width: int | None = None
    """Optional. Animation width """
    height: int | None = None
    """Optional. Animation height """
    duration: int | None = None
    """Optional. Animation duration in seconds """
    has_spoiler: bool | None = None
    """Optional. Pass True if the animation needs to be covered with a spoiler animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.thumbnail, IOBase):
            dest[str(id(self.thumbnail))] = self.thumbnail

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        media: AlterFn[str] | EllipsisType = ...,
        thumbnail: AlterFn[IOBase | str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        width: AlterFn[int | None] | EllipsisType = ...,
        height: AlterFn[int | None] | EllipsisType = ...,
        duration: AlterFn[int | None] | EllipsisType = ...,
        has_spoiler: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputMediaAnimation:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputMediaAnimation(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            media=self.media if media is ... else prefer(media(self.media), self.media),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            has_spoiler=self.has_spoiler
            if has_spoiler is ...
            else prefer(has_spoiler(self.has_spoiler), self.has_spoiler),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        media: str | EllipsisType = ...,
        thumbnail: IOBase | str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        width: int | None | EllipsisType = ...,
        height: int | None | EllipsisType = ...,
        duration: int | None | EllipsisType = ...,
        has_spoiler: bool | None | EllipsisType = ...,
    ) -> InputMediaAnimation:
        """Replaces some of model's fields with provided ones"""
        return InputMediaAnimation(
            type=type if type is not ... else self.type,
            media=media if media is not ... else self.media,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            duration=duration if duration is not ... else self.duration,
            has_spoiler=has_spoiler if has_spoiler is not ... else self.has_spoiler,
        )


@dataclass(frozen=False, slots=True)
class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent."""

    type: str
    """Type of the result, must be audio """
    media: str
    """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    thumbnail: IOBase | str | None = None
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    duration: int | None = None
    """Optional. Duration of the audio in seconds """
    performer: str | None = None
    """Optional. Performer of the audio """
    title: str | None = None
    """Optional. Title of the audio """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.thumbnail, IOBase):
            dest[str(id(self.thumbnail))] = self.thumbnail

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        media: AlterFn[str] | EllipsisType = ...,
        thumbnail: AlterFn[IOBase | str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        duration: AlterFn[int | None] | EllipsisType = ...,
        performer: AlterFn[str | None] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
    ) -> InputMediaAudio:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputMediaAudio(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            media=self.media if media is ... else prefer(media(self.media), self.media),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            duration=self.duration
            if duration is ...
            else prefer(duration(self.duration), self.duration),
            performer=self.performer
            if performer is ...
            else prefer(performer(self.performer), self.performer),
            title=self.title if title is ... else prefer(title(self.title), self.title),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        media: str | EllipsisType = ...,
        thumbnail: IOBase | str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        duration: int | None | EllipsisType = ...,
        performer: str | None | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
    ) -> InputMediaAudio:
        """Replaces some of model's fields with provided ones"""
        return InputMediaAudio(
            type=type if type is not ... else self.type,
            media=media if media is not ... else self.media,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            duration=duration if duration is not ... else self.duration,
            performer=performer if performer is not ... else self.performer,
            title=title if title is not ... else self.title,
        )


@dataclass(frozen=False, slots=True)
class InputMediaDocument:
    """Represents a general file to be sent."""

    type: str
    """Type of the result, must be document """
    media: str
    """File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    thumbnail: IOBase | str | None = None
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    caption: str | None = None
    """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    disable_content_type_detection: bool | None = None
    """Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.thumbnail, IOBase):
            dest[str(id(self.thumbnail))] = self.thumbnail

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        media: AlterFn[str] | EllipsisType = ...,
        thumbnail: AlterFn[IOBase | str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        disable_content_type_detection: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputMediaDocument:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputMediaDocument(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            media=self.media if media is ... else prefer(media(self.media), self.media),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            disable_content_type_detection=self.disable_content_type_detection
            if disable_content_type_detection is ...
            else prefer(
                disable_content_type_detection(self.disable_content_type_detection),
                self.disable_content_type_detection,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        media: str | EllipsisType = ...,
        thumbnail: IOBase | str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        disable_content_type_detection: bool | None | EllipsisType = ...,
    ) -> InputMediaDocument:
        """Replaces some of model's fields with provided ones"""
        return InputMediaDocument(
            type=type if type is not ... else self.type,
            media=media if media is not ... else self.media,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            disable_content_type_detection=disable_content_type_detection
            if disable_content_type_detection is not ...
            else self.disable_content_type_detection,
        )


@dataclass(frozen=False, slots=True)
class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> InputFile:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputFile()

    def copy_with(
        self,
    ) -> InputFile:
        """Replaces some of model's fields with provided ones"""
        return InputFile()


@dataclass(frozen=False, slots=True)
class Sticker:
    """This object represents a sticker."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    type: str
    """Type of the sticker, currently one of "regular", "mask", "custom_emoji". The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video. """
    width: int
    """Sticker width """
    height: int
    """Sticker height """
    is_animated: bool
    """True, if the sticker is animated """
    is_video: bool
    """True, if the sticker is a video sticker """
    thumbnail: PhotoSize | None = None
    """Optional. Sticker thumbnail in the .WEBP or .JPG format """
    emoji: str | None = None
    """Optional. Emoji associated with the sticker """
    set_name: str | None = None
    """Optional. Name of the sticker set to which the sticker belongs """
    premium_animation: File | None = None
    """Optional. For premium regular stickers, premium animation for the sticker """
    mask_position: MaskPosition | None = None
    """Optional. For mask stickers, the position where the mask should be placed """
    custom_emoji_id: str | None = None
    """Optional. For custom emoji stickers, unique identifier of the custom emoji """
    needs_repainting: bool | None = None
    """Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places """
    file_size: int | None = None
    """Optional. File size in bytes """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        width: AlterFn[int] | EllipsisType = ...,
        height: AlterFn[int] | EllipsisType = ...,
        is_animated: AlterFn[bool] | EllipsisType = ...,
        is_video: AlterFn[bool] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
        emoji: AlterFn[str | None] | EllipsisType = ...,
        set_name: AlterFn[str | None] | EllipsisType = ...,
        premium_animation: AlterFn[File | None] | EllipsisType = ...,
        mask_position: AlterFn[MaskPosition | None] | EllipsisType = ...,
        custom_emoji_id: AlterFn[str | None] | EllipsisType = ...,
        needs_repainting: AlterFn[bool | None] | EllipsisType = ...,
        file_size: AlterFn[int | None] | EllipsisType = ...,
    ) -> Sticker:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Sticker(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            width=self.width if width is ... else prefer(width(self.width), self.width),
            height=self.height
            if height is ...
            else prefer(height(self.height), self.height),
            is_animated=self.is_animated
            if is_animated is ...
            else prefer(is_animated(self.is_animated), self.is_animated),
            is_video=self.is_video
            if is_video is ...
            else prefer(is_video(self.is_video), self.is_video),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
            emoji=self.emoji if emoji is ... else prefer(emoji(self.emoji), self.emoji),
            set_name=self.set_name
            if set_name is ...
            else prefer(set_name(self.set_name), self.set_name),
            premium_animation=self.premium_animation
            if premium_animation is ...
            else prefer(
                premium_animation(self.premium_animation), self.premium_animation
            ),
            mask_position=self.mask_position
            if mask_position is ...
            else prefer(mask_position(self.mask_position), self.mask_position),
            custom_emoji_id=self.custom_emoji_id
            if custom_emoji_id is ...
            else prefer(custom_emoji_id(self.custom_emoji_id), self.custom_emoji_id),
            needs_repainting=self.needs_repainting
            if needs_repainting is ...
            else prefer(needs_repainting(self.needs_repainting), self.needs_repainting),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        width: int | EllipsisType = ...,
        height: int | EllipsisType = ...,
        is_animated: bool | EllipsisType = ...,
        is_video: bool | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
        emoji: str | None | EllipsisType = ...,
        set_name: str | None | EllipsisType = ...,
        premium_animation: File | None | EllipsisType = ...,
        mask_position: MaskPosition | None | EllipsisType = ...,
        custom_emoji_id: str | None | EllipsisType = ...,
        needs_repainting: bool | None | EllipsisType = ...,
        file_size: int | None | EllipsisType = ...,
    ) -> Sticker:
        """Replaces some of model's fields with provided ones"""
        return Sticker(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            type=type if type is not ... else self.type,
            width=width if width is not ... else self.width,
            height=height if height is not ... else self.height,
            is_animated=is_animated if is_animated is not ... else self.is_animated,
            is_video=is_video if is_video is not ... else self.is_video,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
            emoji=emoji if emoji is not ... else self.emoji,
            set_name=set_name if set_name is not ... else self.set_name,
            premium_animation=premium_animation
            if premium_animation is not ...
            else self.premium_animation,
            mask_position=mask_position
            if mask_position is not ...
            else self.mask_position,
            custom_emoji_id=custom_emoji_id
            if custom_emoji_id is not ...
            else self.custom_emoji_id,
            needs_repainting=needs_repainting
            if needs_repainting is not ...
            else self.needs_repainting,
            file_size=file_size if file_size is not ... else self.file_size,
        )


@dataclass(frozen=False, slots=True)
class StickerSet:
    """This object represents a sticker set."""

    name: str
    """Sticker set name """
    title: str
    """Sticker set title """
    sticker_type: str
    """Type of stickers in the set, currently one of "regular", "mask", "custom_emoji" """
    is_animated: bool
    """True, if the sticker set contains animated stickers """
    is_video: bool
    """True, if the sticker set contains video stickers """
    stickers: list[Sticker]
    """List of all set stickers """
    thumbnail: PhotoSize | None = None
    """Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        name: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        sticker_type: AlterFn[str] | EllipsisType = ...,
        is_animated: AlterFn[bool] | EllipsisType = ...,
        is_video: AlterFn[bool] | EllipsisType = ...,
        stickers: AlterFn[list[Sticker]] | EllipsisType = ...,
        thumbnail: AlterFn[PhotoSize | None] | EllipsisType = ...,
    ) -> StickerSet:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return StickerSet(
            name=self.name if name is ... else prefer(name(self.name), self.name),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            sticker_type=self.sticker_type
            if sticker_type is ...
            else prefer(sticker_type(self.sticker_type), self.sticker_type),
            is_animated=self.is_animated
            if is_animated is ...
            else prefer(is_animated(self.is_animated), self.is_animated),
            is_video=self.is_video
            if is_video is ...
            else prefer(is_video(self.is_video), self.is_video),
            stickers=self.stickers
            if stickers is ...
            else prefer(stickers(self.stickers), self.stickers),
            thumbnail=self.thumbnail
            if thumbnail is ...
            else prefer(thumbnail(self.thumbnail), self.thumbnail),
        )

    def copy_with(
        self,
        name: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        sticker_type: str | EllipsisType = ...,
        is_animated: bool | EllipsisType = ...,
        is_video: bool | EllipsisType = ...,
        stickers: list[Sticker] | EllipsisType = ...,
        thumbnail: PhotoSize | None | EllipsisType = ...,
    ) -> StickerSet:
        """Replaces some of model's fields with provided ones"""
        return StickerSet(
            name=name if name is not ... else self.name,
            title=title if title is not ... else self.title,
            sticker_type=sticker_type if sticker_type is not ... else self.sticker_type,
            is_animated=is_animated if is_animated is not ... else self.is_animated,
            is_video=is_video if is_video is not ... else self.is_video,
            stickers=stickers if stickers is not ... else self.stickers,
            thumbnail=thumbnail if thumbnail is not ... else self.thumbnail,
        )


@dataclass(frozen=False, slots=True)
class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default."""

    point: str
    """The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin". """
    x_shift: float
    """Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position. """
    y_shift: float
    """Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position. """
    scale: float
    """Mask scaling coefficient. For example, 2.0 means double size. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        point: AlterFn[str] | EllipsisType = ...,
        x_shift: AlterFn[float] | EllipsisType = ...,
        y_shift: AlterFn[float] | EllipsisType = ...,
        scale: AlterFn[float] | EllipsisType = ...,
    ) -> MaskPosition:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return MaskPosition(
            point=self.point if point is ... else prefer(point(self.point), self.point),
            x_shift=self.x_shift
            if x_shift is ...
            else prefer(x_shift(self.x_shift), self.x_shift),
            y_shift=self.y_shift
            if y_shift is ...
            else prefer(y_shift(self.y_shift), self.y_shift),
            scale=self.scale if scale is ... else prefer(scale(self.scale), self.scale),
        )

    def copy_with(
        self,
        point: str | EllipsisType = ...,
        x_shift: float | EllipsisType = ...,
        y_shift: float | EllipsisType = ...,
        scale: float | EllipsisType = ...,
    ) -> MaskPosition:
        """Replaces some of model's fields with provided ones"""
        return MaskPosition(
            point=point if point is not ... else self.point,
            x_shift=x_shift if x_shift is not ... else self.x_shift,
            y_shift=y_shift if y_shift is not ... else self.y_shift,
            scale=scale if scale is not ... else self.scale,
        )


@dataclass(frozen=False, slots=True)
class InputSticker:
    """This object describes a sticker to be added to a sticker set."""

    sticker: IOBase | str
    """The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    emoji_list: list[str]
    """List of 1-20 emoji associated with the sticker """
    mask_position: MaskPosition | None = None
    """Optional. Position where the mask should be placed on faces. For "mask" stickers only. """
    keywords: list[str] | None = None
    """Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For "regular" and "custom_emoji" stickers only. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.sticker, IOBase):
            dest[str(id(self.sticker))] = self.sticker

    def alter(
        self,
        sticker: AlterFn[IOBase | str] | EllipsisType = ...,
        emoji_list: AlterFn[list[str]] | EllipsisType = ...,
        mask_position: AlterFn[MaskPosition | None] | EllipsisType = ...,
        keywords: AlterFn[list[str] | None] | EllipsisType = ...,
    ) -> InputSticker:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputSticker(
            sticker=self.sticker
            if sticker is ...
            else prefer(sticker(self.sticker), self.sticker),
            emoji_list=self.emoji_list
            if emoji_list is ...
            else prefer(emoji_list(self.emoji_list), self.emoji_list),
            mask_position=self.mask_position
            if mask_position is ...
            else prefer(mask_position(self.mask_position), self.mask_position),
            keywords=self.keywords
            if keywords is ...
            else prefer(keywords(self.keywords), self.keywords),
        )

    def copy_with(
        self,
        sticker: IOBase | str | EllipsisType = ...,
        emoji_list: list[str] | EllipsisType = ...,
        mask_position: MaskPosition | None | EllipsisType = ...,
        keywords: list[str] | None | EllipsisType = ...,
    ) -> InputSticker:
        """Replaces some of model's fields with provided ones"""
        return InputSticker(
            sticker=sticker if sticker is not ... else self.sticker,
            emoji_list=emoji_list if emoji_list is not ... else self.emoji_list,
            mask_position=mask_position
            if mask_position is not ...
            else self.mask_position,
            keywords=keywords if keywords is not ... else self.keywords,
        )


@dataclass(frozen=False, slots=True)
class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results."""

    id: str
    """Unique identifier for this query """
    from_: User
    """Sender """
    query: str
    """Text of the query (up to 256 characters) """
    offset: str
    """Offset of the results to be returned, can be controlled by the bot """
    chat_type: str | None = None
    """Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat """
    location: Location | None = None
    """Optional. Sender location, only for bots that request user location """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        query: AlterFn[str] | EllipsisType = ...,
        offset: AlterFn[str] | EllipsisType = ...,
        chat_type: AlterFn[str | None] | EllipsisType = ...,
        location: AlterFn[Location | None] | EllipsisType = ...,
    ) -> InlineQuery:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQuery(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            query=self.query if query is ... else prefer(query(self.query), self.query),
            offset=self.offset
            if offset is ...
            else prefer(offset(self.offset), self.offset),
            chat_type=self.chat_type
            if chat_type is ...
            else prefer(chat_type(self.chat_type), self.chat_type),
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        query: str | EllipsisType = ...,
        offset: str | EllipsisType = ...,
        chat_type: str | None | EllipsisType = ...,
        location: Location | None | EllipsisType = ...,
    ) -> InlineQuery:
        """Replaces some of model's fields with provided ones"""
        return InlineQuery(
            id=id if id is not ... else self.id,
            from_=from_ if from_ is not ... else self.from_,
            query=query if query is not ... else self.query,
            offset=offset if offset is not ... else self.offset,
            chat_type=chat_type if chat_type is not ... else self.chat_type,
            location=location if location is not ... else self.location,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultsButton:
    """This object represents a button to be shown above inline query results. You must use exactly one of the optional fields."""

    text: str
    """Label text on the button """
    web_app: WebAppInfo | None = None
    """Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method switchInlineQuery inside the Web App. """
    start_parameter: str | None = None
    """Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        text: AlterFn[str] | EllipsisType = ...,
        web_app: AlterFn[WebAppInfo | None] | EllipsisType = ...,
        start_parameter: AlterFn[str | None] | EllipsisType = ...,
    ) -> InlineQueryResultsButton:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultsButton(
            text=self.text if text is ... else prefer(text(self.text), self.text),
            web_app=self.web_app
            if web_app is ...
            else prefer(web_app(self.web_app), self.web_app),
            start_parameter=self.start_parameter
            if start_parameter is ...
            else prefer(start_parameter(self.start_parameter), self.start_parameter),
        )

    def copy_with(
        self,
        text: str | EllipsisType = ...,
        web_app: WebAppInfo | None | EllipsisType = ...,
        start_parameter: str | None | EllipsisType = ...,
    ) -> InlineQueryResultsButton:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultsButton(
            text=text if text is not ... else self.text,
            web_app=web_app if web_app is not ... else self.web_app,
            start_parameter=start_parameter
            if start_parameter is not ...
            else self.start_parameter,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultArticle:
    """Represents a link to an article or web page."""

    type: str
    """Type of the result, must be article """
    id: str
    """Unique identifier for this result, 1-64 Bytes """
    title: str
    """Title of the result """
    input_message_content: InputMessageContent
    """Content of the message to be sent """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    url: str | None = None
    """Optional. URL of the result """
    hide_url: bool | None = None
    """Optional. Pass True if you don't want the URL to be shown in the message """
    description: str | None = None
    """Optional. Short description of the result """
    thumbnail_url: str | None = None
    """Optional. Url of the thumbnail for the result """
    thumbnail_width: int | None = None
    """Optional. Thumbnail width """
    thumbnail_height: int | None = None
    """Optional. Thumbnail height """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        url: AlterFn[str | None] | EllipsisType = ...,
        hide_url: AlterFn[bool | None] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_width: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_height: AlterFn[int | None] | EllipsisType = ...,
    ) -> InlineQueryResultArticle:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultArticle(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            url=self.url if url is ... else prefer(url(self.url), self.url),
            hide_url=self.hide_url
            if hide_url is ...
            else prefer(hide_url(self.hide_url), self.hide_url),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_width=self.thumbnail_width
            if thumbnail_width is ...
            else prefer(thumbnail_width(self.thumbnail_width), self.thumbnail_width),
            thumbnail_height=self.thumbnail_height
            if thumbnail_height is ...
            else prefer(thumbnail_height(self.thumbnail_height), self.thumbnail_height),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        input_message_content: InputMessageContent | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        url: str | None | EllipsisType = ...,
        hide_url: bool | None | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        thumbnail_url: str | None | EllipsisType = ...,
        thumbnail_width: int | None | EllipsisType = ...,
        thumbnail_height: int | None | EllipsisType = ...,
    ) -> InlineQueryResultArticle:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultArticle(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            title=title if title is not ... else self.title,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            url=url if url is not ... else self.url,
            hide_url=hide_url if hide_url is not ... else self.hide_url,
            description=description if description is not ... else self.description,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_width=thumbnail_width
            if thumbnail_width is not ...
            else self.thumbnail_width,
            thumbnail_height=thumbnail_height
            if thumbnail_height is not ...
            else self.thumbnail_height,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""

    type: str
    """Type of the result, must be photo """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    photo_url: str
    """A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB """
    thumbnail_url: str
    """URL of the thumbnail for the photo """
    photo_width: int | None = None
    """Optional. Width of the photo """
    photo_height: int | None = None
    """Optional. Height of the photo """
    title: str | None = None
    """Optional. Title for the result """
    description: str | None = None
    """Optional. Short description of the result """
    caption: str | None = None
    """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the photo """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        photo_url: AlterFn[str] | EllipsisType = ...,
        thumbnail_url: AlterFn[str] | EllipsisType = ...,
        photo_width: AlterFn[int | None] | EllipsisType = ...,
        photo_height: AlterFn[int | None] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultPhoto:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultPhoto(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            photo_url=self.photo_url
            if photo_url is ...
            else prefer(photo_url(self.photo_url), self.photo_url),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            photo_width=self.photo_width
            if photo_width is ...
            else prefer(photo_width(self.photo_width), self.photo_width),
            photo_height=self.photo_height
            if photo_height is ...
            else prefer(photo_height(self.photo_height), self.photo_height),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        photo_url: str | EllipsisType = ...,
        thumbnail_url: str | EllipsisType = ...,
        photo_width: int | None | EllipsisType = ...,
        photo_height: int | None | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultPhoto:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultPhoto(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            photo_url=photo_url if photo_url is not ... else self.photo_url,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            photo_width=photo_width if photo_width is not ... else self.photo_width,
            photo_height=photo_height if photo_height is not ... else self.photo_height,
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultGif:
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""

    type: str
    """Type of the result, must be gif """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    gif_url: str
    """A valid URL for the GIF file. File size must not exceed 1MB """
    thumbnail_url: str
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result """
    gif_width: int | None = None
    """Optional. Width of the GIF """
    gif_height: int | None = None
    """Optional. Height of the GIF """
    gif_duration: int | None = None
    """Optional. Duration of the GIF in seconds """
    thumbnail_mime_type: str | None = None
    """Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg" """
    title: str | None = None
    """Optional. Title for the result """
    caption: str | None = None
    """Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the GIF animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        gif_url: AlterFn[str] | EllipsisType = ...,
        gif_width: AlterFn[int | None] | EllipsisType = ...,
        gif_height: AlterFn[int | None] | EllipsisType = ...,
        gif_duration: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str] | EllipsisType = ...,
        thumbnail_mime_type: AlterFn[str | None] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultGif:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultGif(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            gif_url=self.gif_url
            if gif_url is ...
            else prefer(gif_url(self.gif_url), self.gif_url),
            gif_width=self.gif_width
            if gif_width is ...
            else prefer(gif_width(self.gif_width), self.gif_width),
            gif_height=self.gif_height
            if gif_height is ...
            else prefer(gif_height(self.gif_height), self.gif_height),
            gif_duration=self.gif_duration
            if gif_duration is ...
            else prefer(gif_duration(self.gif_duration), self.gif_duration),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_mime_type=self.thumbnail_mime_type
            if thumbnail_mime_type is ...
            else prefer(
                thumbnail_mime_type(self.thumbnail_mime_type), self.thumbnail_mime_type
            ),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        gif_url: str | EllipsisType = ...,
        gif_width: int | None | EllipsisType = ...,
        gif_height: int | None | EllipsisType = ...,
        gif_duration: int | None | EllipsisType = ...,
        thumbnail_url: str | EllipsisType = ...,
        thumbnail_mime_type: str | None | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultGif:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultGif(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            gif_url=gif_url if gif_url is not ... else self.gif_url,
            gif_width=gif_width if gif_width is not ... else self.gif_width,
            gif_height=gif_height if gif_height is not ... else self.gif_height,
            gif_duration=gif_duration if gif_duration is not ... else self.gif_duration,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_mime_type=thumbnail_mime_type
            if thumbnail_mime_type is not ...
            else self.thumbnail_mime_type,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""

    type: str
    """Type of the result, must be mpeg4_gif """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    mpeg4_url: str
    """A valid URL for the MPEG4 file. File size must not exceed 1MB """
    thumbnail_url: str
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result """
    mpeg4_width: int | None = None
    """Optional. Video width """
    mpeg4_height: int | None = None
    """Optional. Video height """
    mpeg4_duration: int | None = None
    """Optional. Video duration in seconds """
    thumbnail_mime_type: str | None = None
    """Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg" """
    title: str | None = None
    """Optional. Title for the result """
    caption: str | None = None
    """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the video animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        mpeg4_url: AlterFn[str] | EllipsisType = ...,
        mpeg4_width: AlterFn[int | None] | EllipsisType = ...,
        mpeg4_height: AlterFn[int | None] | EllipsisType = ...,
        mpeg4_duration: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str] | EllipsisType = ...,
        thumbnail_mime_type: AlterFn[str | None] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultMpeg4Gif:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultMpeg4Gif(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            mpeg4_url=self.mpeg4_url
            if mpeg4_url is ...
            else prefer(mpeg4_url(self.mpeg4_url), self.mpeg4_url),
            mpeg4_width=self.mpeg4_width
            if mpeg4_width is ...
            else prefer(mpeg4_width(self.mpeg4_width), self.mpeg4_width),
            mpeg4_height=self.mpeg4_height
            if mpeg4_height is ...
            else prefer(mpeg4_height(self.mpeg4_height), self.mpeg4_height),
            mpeg4_duration=self.mpeg4_duration
            if mpeg4_duration is ...
            else prefer(mpeg4_duration(self.mpeg4_duration), self.mpeg4_duration),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_mime_type=self.thumbnail_mime_type
            if thumbnail_mime_type is ...
            else prefer(
                thumbnail_mime_type(self.thumbnail_mime_type), self.thumbnail_mime_type
            ),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        mpeg4_url: str | EllipsisType = ...,
        mpeg4_width: int | None | EllipsisType = ...,
        mpeg4_height: int | None | EllipsisType = ...,
        mpeg4_duration: int | None | EllipsisType = ...,
        thumbnail_url: str | EllipsisType = ...,
        thumbnail_mime_type: str | None | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultMpeg4Gif:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultMpeg4Gif(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            mpeg4_url=mpeg4_url if mpeg4_url is not ... else self.mpeg4_url,
            mpeg4_width=mpeg4_width if mpeg4_width is not ... else self.mpeg4_width,
            mpeg4_height=mpeg4_height if mpeg4_height is not ... else self.mpeg4_height,
            mpeg4_duration=mpeg4_duration
            if mpeg4_duration is not ...
            else self.mpeg4_duration,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_mime_type=thumbnail_mime_type
            if thumbnail_mime_type is not ...
            else self.thumbnail_mime_type,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""

    type: str
    """Type of the result, must be video """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    video_url: str
    """A valid URL for the embedded video player or video file """
    mime_type: str
    """MIME type of the content of the video URL, "text/html" or "video/mp4" """
    thumbnail_url: str
    """URL of the thumbnail (JPEG only) for the video """
    title: str
    """Title for the result """
    caption: str | None = None
    """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    video_width: int | None = None
    """Optional. Video width """
    video_height: int | None = None
    """Optional. Video height """
    video_duration: int | None = None
    """Optional. Video duration in seconds """
    description: str | None = None
    """Optional. Short description of the result """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video). """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        video_url: AlterFn[str] | EllipsisType = ...,
        mime_type: AlterFn[str] | EllipsisType = ...,
        thumbnail_url: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        video_width: AlterFn[int | None] | EllipsisType = ...,
        video_height: AlterFn[int | None] | EllipsisType = ...,
        video_duration: AlterFn[int | None] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultVideo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultVideo(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            video_url=self.video_url
            if video_url is ...
            else prefer(video_url(self.video_url), self.video_url),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            video_width=self.video_width
            if video_width is ...
            else prefer(video_width(self.video_width), self.video_width),
            video_height=self.video_height
            if video_height is ...
            else prefer(video_height(self.video_height), self.video_height),
            video_duration=self.video_duration
            if video_duration is ...
            else prefer(video_duration(self.video_duration), self.video_duration),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        video_url: str | EllipsisType = ...,
        mime_type: str | EllipsisType = ...,
        thumbnail_url: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        video_width: int | None | EllipsisType = ...,
        video_height: int | None | EllipsisType = ...,
        video_duration: int | None | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultVideo:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultVideo(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            video_url=video_url if video_url is not ... else self.video_url,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            video_width=video_width if video_width is not ... else self.video_width,
            video_height=video_height if video_height is not ... else self.video_height,
            video_duration=video_duration
            if video_duration is not ...
            else self.video_duration,
            description=description if description is not ... else self.description,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultAudio:
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be audio """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    audio_url: str
    """A valid URL for the audio file """
    title: str
    """Title """
    caption: str | None = None
    """Optional. Caption, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    performer: str | None = None
    """Optional. Performer """
    audio_duration: int | None = None
    """Optional. Audio duration in seconds """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the audio """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        audio_url: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        performer: AlterFn[str | None] | EllipsisType = ...,
        audio_duration: AlterFn[int | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultAudio:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultAudio(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            audio_url=self.audio_url
            if audio_url is ...
            else prefer(audio_url(self.audio_url), self.audio_url),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            performer=self.performer
            if performer is ...
            else prefer(performer(self.performer), self.performer),
            audio_duration=self.audio_duration
            if audio_duration is ...
            else prefer(audio_duration(self.audio_duration), self.audio_duration),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        audio_url: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        performer: str | None | EllipsisType = ...,
        audio_duration: int | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultAudio:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultAudio(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            audio_url=audio_url if audio_url is not ... else self.audio_url,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            performer=performer if performer is not ... else self.performer,
            audio_duration=audio_duration
            if audio_duration is not ...
            else self.audio_duration,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be voice """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    voice_url: str
    """A valid URL for the voice recording """
    title: str
    """Recording title """
    caption: str | None = None
    """Optional. Caption, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the voice message caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    voice_duration: int | None = None
    """Optional. Recording duration in seconds """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the voice recording """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        voice_url: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        voice_duration: AlterFn[int | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultVoice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultVoice(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            voice_url=self.voice_url
            if voice_url is ...
            else prefer(voice_url(self.voice_url), self.voice_url),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            voice_duration=self.voice_duration
            if voice_duration is ...
            else prefer(voice_duration(self.voice_duration), self.voice_duration),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        voice_url: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        voice_duration: int | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultVoice:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultVoice(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            voice_url=voice_url if voice_url is not ... else self.voice_url,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            voice_duration=voice_duration
            if voice_duration is not ...
            else self.voice_duration,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be document """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    title: str
    """Title for the result """
    document_url: str
    """A valid URL for the file """
    mime_type: str
    """MIME type of the content of the file, either "application/pdf" or "application/zip" """
    caption: str | None = None
    """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str | None = None
    """Optional. Short description of the result """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the file """
    thumbnail_url: str | None = None
    """Optional. URL of the thumbnail (JPEG only) for the file """
    thumbnail_width: int | None = None
    """Optional. Thumbnail width """
    thumbnail_height: int | None = None
    """Optional. Thumbnail height """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        document_url: AlterFn[str] | EllipsisType = ...,
        mime_type: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_width: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_height: AlterFn[int | None] | EllipsisType = ...,
    ) -> InlineQueryResultDocument:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultDocument(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            document_url=self.document_url
            if document_url is ...
            else prefer(document_url(self.document_url), self.document_url),
            mime_type=self.mime_type
            if mime_type is ...
            else prefer(mime_type(self.mime_type), self.mime_type),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_width=self.thumbnail_width
            if thumbnail_width is ...
            else prefer(thumbnail_width(self.thumbnail_width), self.thumbnail_width),
            thumbnail_height=self.thumbnail_height
            if thumbnail_height is ...
            else prefer(thumbnail_height(self.thumbnail_height), self.thumbnail_height),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        document_url: str | EllipsisType = ...,
        mime_type: str | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
        thumbnail_url: str | None | EllipsisType = ...,
        thumbnail_width: int | None | EllipsisType = ...,
        thumbnail_height: int | None | EllipsisType = ...,
    ) -> InlineQueryResultDocument:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultDocument(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            document_url=document_url if document_url is not ... else self.document_url,
            mime_type=mime_type if mime_type is not ... else self.mime_type,
            description=description if description is not ... else self.description,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_width=thumbnail_width
            if thumbnail_width is not ...
            else self.thumbnail_width,
            thumbnail_height=thumbnail_height
            if thumbnail_height is not ...
            else self.thumbnail_height,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be location """
    id: str
    """Unique identifier for this result, 1-64 Bytes """
    latitude: float
    """Location latitude in degrees """
    longitude: float
    """Location longitude in degrees """
    title: str
    """Location title """
    horizontal_accuracy: float | None = None
    """Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    live_period: int | None = None
    """Optional. Period in seconds for which the location can be updated, should be between 60 and 86400. """
    heading: int | None = None
    """Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. """
    proximity_alert_radius: int | None = None
    """Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the location """
    thumbnail_url: str | None = None
    """Optional. Url of the thumbnail for the result """
    thumbnail_width: int | None = None
    """Optional. Thumbnail width """
    thumbnail_height: int | None = None
    """Optional. Thumbnail height """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        latitude: AlterFn[float] | EllipsisType = ...,
        longitude: AlterFn[float] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        horizontal_accuracy: AlterFn[float | None] | EllipsisType = ...,
        live_period: AlterFn[int | None] | EllipsisType = ...,
        heading: AlterFn[int | None] | EllipsisType = ...,
        proximity_alert_radius: AlterFn[int | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_width: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_height: AlterFn[int | None] | EllipsisType = ...,
    ) -> InlineQueryResultLocation:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultLocation(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            latitude=self.latitude
            if latitude is ...
            else prefer(latitude(self.latitude), self.latitude),
            longitude=self.longitude
            if longitude is ...
            else prefer(longitude(self.longitude), self.longitude),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            horizontal_accuracy=self.horizontal_accuracy
            if horizontal_accuracy is ...
            else prefer(
                horizontal_accuracy(self.horizontal_accuracy), self.horizontal_accuracy
            ),
            live_period=self.live_period
            if live_period is ...
            else prefer(live_period(self.live_period), self.live_period),
            heading=self.heading
            if heading is ...
            else prefer(heading(self.heading), self.heading),
            proximity_alert_radius=self.proximity_alert_radius
            if proximity_alert_radius is ...
            else prefer(
                proximity_alert_radius(self.proximity_alert_radius),
                self.proximity_alert_radius,
            ),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_width=self.thumbnail_width
            if thumbnail_width is ...
            else prefer(thumbnail_width(self.thumbnail_width), self.thumbnail_width),
            thumbnail_height=self.thumbnail_height
            if thumbnail_height is ...
            else prefer(thumbnail_height(self.thumbnail_height), self.thumbnail_height),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        latitude: float | EllipsisType = ...,
        longitude: float | EllipsisType = ...,
        title: str | EllipsisType = ...,
        horizontal_accuracy: float | None | EllipsisType = ...,
        live_period: int | None | EllipsisType = ...,
        heading: int | None | EllipsisType = ...,
        proximity_alert_radius: int | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
        thumbnail_url: str | None | EllipsisType = ...,
        thumbnail_width: int | None | EllipsisType = ...,
        thumbnail_height: int | None | EllipsisType = ...,
    ) -> InlineQueryResultLocation:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultLocation(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            latitude=latitude if latitude is not ... else self.latitude,
            longitude=longitude if longitude is not ... else self.longitude,
            title=title if title is not ... else self.title,
            horizontal_accuracy=horizontal_accuracy
            if horizontal_accuracy is not ...
            else self.horizontal_accuracy,
            live_period=live_period if live_period is not ... else self.live_period,
            heading=heading if heading is not ... else self.heading,
            proximity_alert_radius=proximity_alert_radius
            if proximity_alert_radius is not ...
            else self.proximity_alert_radius,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_width=thumbnail_width
            if thumbnail_width is not ...
            else self.thumbnail_width,
            thumbnail_height=thumbnail_height
            if thumbnail_height is not ...
            else self.thumbnail_height,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be venue """
    id: str
    """Unique identifier for this result, 1-64 Bytes """
    latitude: float
    """Latitude of the venue location in degrees """
    longitude: float
    """Longitude of the venue location in degrees """
    title: str
    """Title of the venue """
    address: str
    """Address of the venue """
    foursquare_id: str | None = None
    """Optional. Foursquare identifier of the venue if known """
    foursquare_type: str | None = None
    """Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str | None = None
    """Optional. Google Places identifier of the venue """
    google_place_type: str | None = None
    """Optional. Google Places type of the venue. (See supported types.) """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the venue """
    thumbnail_url: str | None = None
    """Optional. Url of the thumbnail for the result """
    thumbnail_width: int | None = None
    """Optional. Thumbnail width """
    thumbnail_height: int | None = None
    """Optional. Thumbnail height """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        latitude: AlterFn[float] | EllipsisType = ...,
        longitude: AlterFn[float] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        address: AlterFn[str] | EllipsisType = ...,
        foursquare_id: AlterFn[str | None] | EllipsisType = ...,
        foursquare_type: AlterFn[str | None] | EllipsisType = ...,
        google_place_id: AlterFn[str | None] | EllipsisType = ...,
        google_place_type: AlterFn[str | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_width: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_height: AlterFn[int | None] | EllipsisType = ...,
    ) -> InlineQueryResultVenue:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultVenue(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            latitude=self.latitude
            if latitude is ...
            else prefer(latitude(self.latitude), self.latitude),
            longitude=self.longitude
            if longitude is ...
            else prefer(longitude(self.longitude), self.longitude),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            address=self.address
            if address is ...
            else prefer(address(self.address), self.address),
            foursquare_id=self.foursquare_id
            if foursquare_id is ...
            else prefer(foursquare_id(self.foursquare_id), self.foursquare_id),
            foursquare_type=self.foursquare_type
            if foursquare_type is ...
            else prefer(foursquare_type(self.foursquare_type), self.foursquare_type),
            google_place_id=self.google_place_id
            if google_place_id is ...
            else prefer(google_place_id(self.google_place_id), self.google_place_id),
            google_place_type=self.google_place_type
            if google_place_type is ...
            else prefer(
                google_place_type(self.google_place_type), self.google_place_type
            ),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_width=self.thumbnail_width
            if thumbnail_width is ...
            else prefer(thumbnail_width(self.thumbnail_width), self.thumbnail_width),
            thumbnail_height=self.thumbnail_height
            if thumbnail_height is ...
            else prefer(thumbnail_height(self.thumbnail_height), self.thumbnail_height),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        latitude: float | EllipsisType = ...,
        longitude: float | EllipsisType = ...,
        title: str | EllipsisType = ...,
        address: str | EllipsisType = ...,
        foursquare_id: str | None | EllipsisType = ...,
        foursquare_type: str | None | EllipsisType = ...,
        google_place_id: str | None | EllipsisType = ...,
        google_place_type: str | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
        thumbnail_url: str | None | EllipsisType = ...,
        thumbnail_width: int | None | EllipsisType = ...,
        thumbnail_height: int | None | EllipsisType = ...,
    ) -> InlineQueryResultVenue:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultVenue(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            latitude=latitude if latitude is not ... else self.latitude,
            longitude=longitude if longitude is not ... else self.longitude,
            title=title if title is not ... else self.title,
            address=address if address is not ... else self.address,
            foursquare_id=foursquare_id
            if foursquare_id is not ...
            else self.foursquare_id,
            foursquare_type=foursquare_type
            if foursquare_type is not ...
            else self.foursquare_type,
            google_place_id=google_place_id
            if google_place_id is not ...
            else self.google_place_id,
            google_place_type=google_place_type
            if google_place_type is not ...
            else self.google_place_type,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_width=thumbnail_width
            if thumbnail_width is not ...
            else self.thumbnail_width,
            thumbnail_height=thumbnail_height
            if thumbnail_height is not ...
            else self.thumbnail_height,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be contact """
    id: str
    """Unique identifier for this result, 1-64 Bytes """
    phone_number: str
    """Contact's phone number """
    first_name: str
    """Contact's first name """
    last_name: str | None = None
    """Optional. Contact's last name """
    vcard: str | None = None
    """Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the contact """
    thumbnail_url: str | None = None
    """Optional. Url of the thumbnail for the result """
    thumbnail_width: int | None = None
    """Optional. Thumbnail width """
    thumbnail_height: int | None = None
    """Optional. Thumbnail height """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        phone_number: AlterFn[str] | EllipsisType = ...,
        first_name: AlterFn[str] | EllipsisType = ...,
        last_name: AlterFn[str | None] | EllipsisType = ...,
        vcard: AlterFn[str | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
        thumbnail_url: AlterFn[str | None] | EllipsisType = ...,
        thumbnail_width: AlterFn[int | None] | EllipsisType = ...,
        thumbnail_height: AlterFn[int | None] | EllipsisType = ...,
    ) -> InlineQueryResultContact:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultContact(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            phone_number=self.phone_number
            if phone_number is ...
            else prefer(phone_number(self.phone_number), self.phone_number),
            first_name=self.first_name
            if first_name is ...
            else prefer(first_name(self.first_name), self.first_name),
            last_name=self.last_name
            if last_name is ...
            else prefer(last_name(self.last_name), self.last_name),
            vcard=self.vcard if vcard is ... else prefer(vcard(self.vcard), self.vcard),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
            thumbnail_url=self.thumbnail_url
            if thumbnail_url is ...
            else prefer(thumbnail_url(self.thumbnail_url), self.thumbnail_url),
            thumbnail_width=self.thumbnail_width
            if thumbnail_width is ...
            else prefer(thumbnail_width(self.thumbnail_width), self.thumbnail_width),
            thumbnail_height=self.thumbnail_height
            if thumbnail_height is ...
            else prefer(thumbnail_height(self.thumbnail_height), self.thumbnail_height),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        phone_number: str | EllipsisType = ...,
        first_name: str | EllipsisType = ...,
        last_name: str | None | EllipsisType = ...,
        vcard: str | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
        thumbnail_url: str | None | EllipsisType = ...,
        thumbnail_width: int | None | EllipsisType = ...,
        thumbnail_height: int | None | EllipsisType = ...,
    ) -> InlineQueryResultContact:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultContact(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            phone_number=phone_number if phone_number is not ... else self.phone_number,
            first_name=first_name if first_name is not ... else self.first_name,
            last_name=last_name if last_name is not ... else self.last_name,
            vcard=vcard if vcard is not ... else self.vcard,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
            thumbnail_url=thumbnail_url
            if thumbnail_url is not ...
            else self.thumbnail_url,
            thumbnail_width=thumbnail_width
            if thumbnail_width is not ...
            else self.thumbnail_width,
            thumbnail_height=thumbnail_height
            if thumbnail_height is not ...
            else self.thumbnail_height,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultGame:
    """Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.
    """

    type: str
    """Type of the result, must be game """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    game_short_name: str
    """Short name of the game """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        game_short_name: AlterFn[str] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
    ) -> InlineQueryResultGame:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultGame(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            game_short_name=self.game_short_name
            if game_short_name is ...
            else prefer(game_short_name(self.game_short_name), self.game_short_name),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        game_short_name: str | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
    ) -> InlineQueryResultGame:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultGame(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            game_short_name=game_short_name
            if game_short_name is not ...
            else self.game_short_name,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedPhoto:
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""

    type: str
    """Type of the result, must be photo """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    photo_file_id: str
    """A valid file identifier of the photo """
    title: str | None = None
    """Optional. Title for the result """
    description: str | None = None
    """Optional. Short description of the result """
    caption: str | None = None
    """Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the photo """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        photo_file_id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedPhoto:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedPhoto(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            photo_file_id=self.photo_file_id
            if photo_file_id is ...
            else prefer(photo_file_id(self.photo_file_id), self.photo_file_id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        photo_file_id: str | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedPhoto:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedPhoto(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            photo_file_id=photo_file_id
            if photo_file_id is not ...
            else self.photo_file_id,
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedGif:
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation."""

    type: str
    """Type of the result, must be gif """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    gif_file_id: str
    """A valid file identifier for the GIF file """
    title: str | None = None
    """Optional. Title for the result """
    caption: str | None = None
    """Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the GIF animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        gif_file_id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedGif:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedGif(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            gif_file_id=self.gif_file_id
            if gif_file_id is ...
            else prefer(gif_file_id(self.gif_file_id), self.gif_file_id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        gif_file_id: str | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedGif:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedGif(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            gif_file_id=gif_file_id if gif_file_id is not ... else self.gif_file_id,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""

    type: str
    """Type of the result, must be mpeg4_gif """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    mpeg4_file_id: str
    """A valid file identifier for the MPEG4 file """
    title: str | None = None
    """Optional. Title for the result """
    caption: str | None = None
    """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the video animation """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        mpeg4_file_id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedMpeg4Gif:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedMpeg4Gif(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            mpeg4_file_id=self.mpeg4_file_id
            if mpeg4_file_id is ...
            else prefer(mpeg4_file_id(self.mpeg4_file_id), self.mpeg4_file_id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        mpeg4_file_id: str | EllipsisType = ...,
        title: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedMpeg4Gif:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedMpeg4Gif(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            mpeg4_file_id=mpeg4_file_id
            if mpeg4_file_id is not ...
            else self.mpeg4_file_id,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be sticker """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    sticker_file_id: str
    """A valid file identifier of the sticker """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the sticker """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        sticker_file_id: AlterFn[str] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedSticker:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedSticker(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            sticker_file_id=self.sticker_file_id
            if sticker_file_id is ...
            else prefer(sticker_file_id(self.sticker_file_id), self.sticker_file_id),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        sticker_file_id: str | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedSticker:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedSticker(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            sticker_file_id=sticker_file_id
            if sticker_file_id is not ...
            else self.sticker_file_id,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedDocument:
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be document """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    title: str
    """Title for the result """
    document_file_id: str
    """A valid file identifier for the file """
    description: str | None = None
    """Optional. Short description of the result """
    caption: str | None = None
    """Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the file """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        document_file_id: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedDocument:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedDocument(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            document_file_id=self.document_file_id
            if document_file_id is ...
            else prefer(document_file_id(self.document_file_id), self.document_file_id),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        document_file_id: str | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedDocument:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedDocument(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            title=title if title is not ... else self.title,
            document_file_id=document_file_id
            if document_file_id is not ...
            else self.document_file_id,
            description=description if description is not ... else self.description,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedVideo:
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""

    type: str
    """Type of the result, must be video """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    video_file_id: str
    """A valid file identifier for the video file """
    title: str
    """Title for the result """
    description: str | None = None
    """Optional. Short description of the result """
    caption: str | None = None
    """Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the video """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        video_file_id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str | None] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedVideo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedVideo(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            video_file_id=self.video_file_id
            if video_file_id is ...
            else prefer(video_file_id(self.video_file_id), self.video_file_id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        video_file_id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        description: str | None | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedVideo:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedVideo(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            video_file_id=video_file_id
            if video_file_id is not ...
            else self.video_file_id,
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedVoice:
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be voice """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    voice_file_id: str
    """A valid file identifier for the voice message """
    title: str
    """Voice message title """
    caption: str | None = None
    """Optional. Caption, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the voice message caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the voice message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        voice_file_id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedVoice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedVoice(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            voice_file_id=self.voice_file_id
            if voice_file_id is ...
            else prefer(voice_file_id(self.voice_file_id), self.voice_file_id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        voice_file_id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedVoice:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedVoice(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            voice_file_id=voice_file_id
            if voice_file_id is not ...
            else self.voice_file_id,
            title=title if title is not ... else self.title,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InlineQueryResultCachedAudio:
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """

    type: str
    """Type of the result, must be audio """
    id: str
    """Unique identifier for this result, 1-64 bytes """
    audio_file_id: str
    """A valid file identifier for the audio file """
    caption: str | None = None
    """Optional. Caption, 0-1024 characters after entities parsing """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    caption_entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    reply_markup: InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message """
    input_message_content: InputMessageContent | None = None
    """Optional. Content of the message to be sent instead of the audio """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        id: AlterFn[str] | EllipsisType = ...,
        audio_file_id: AlterFn[str] | EllipsisType = ...,
        caption: AlterFn[str | None] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        caption_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        reply_markup: AlterFn[InlineKeyboardMarkup | None] | EllipsisType = ...,
        input_message_content: AlterFn[InputMessageContent | None] | EllipsisType = ...,
    ) -> InlineQueryResultCachedAudio:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InlineQueryResultCachedAudio(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            id=self.id if id is ... else prefer(id(self.id), self.id),
            audio_file_id=self.audio_file_id
            if audio_file_id is ...
            else prefer(audio_file_id(self.audio_file_id), self.audio_file_id),
            caption=self.caption
            if caption is ...
            else prefer(caption(self.caption), self.caption),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            caption_entities=self.caption_entities
            if caption_entities is ...
            else prefer(caption_entities(self.caption_entities), self.caption_entities),
            reply_markup=self.reply_markup
            if reply_markup is ...
            else prefer(reply_markup(self.reply_markup), self.reply_markup),
            input_message_content=self.input_message_content
            if input_message_content is ...
            else prefer(
                input_message_content(self.input_message_content),
                self.input_message_content,
            ),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        id: str | EllipsisType = ...,
        audio_file_id: str | EllipsisType = ...,
        caption: str | None | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        caption_entities: list[MessageEntity] | None | EllipsisType = ...,
        reply_markup: InlineKeyboardMarkup | None | EllipsisType = ...,
        input_message_content: InputMessageContent | None | EllipsisType = ...,
    ) -> InlineQueryResultCachedAudio:
        """Replaces some of model's fields with provided ones"""
        return InlineQueryResultCachedAudio(
            type=type if type is not ... else self.type,
            id=id if id is not ... else self.id,
            audio_file_id=audio_file_id
            if audio_file_id is not ...
            else self.audio_file_id,
            caption=caption if caption is not ... else self.caption,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            caption_entities=caption_entities
            if caption_entities is not ...
            else self.caption_entities,
            reply_markup=reply_markup if reply_markup is not ... else self.reply_markup,
            input_message_content=input_message_content
            if input_message_content is not ...
            else self.input_message_content,
        )


@dataclass(frozen=False, slots=True)
class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query."""

    message_text: str
    """Text of the message to be sent, 1-4096 characters """
    parse_mode: str | None = None
    """Optional. Mode for parsing entities in the message text. See formatting options for more details. """
    entities: list[MessageEntity] | None = None
    """Optional. List of special entities that appear in message text, which can be specified instead of parse_mode """
    disable_web_page_preview: bool | None = None
    """Optional. Disables link previews for links in the sent message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        message_text: AlterFn[str] | EllipsisType = ...,
        parse_mode: AlterFn[str | None] | EllipsisType = ...,
        entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        disable_web_page_preview: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputTextMessageContent:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputTextMessageContent(
            message_text=self.message_text
            if message_text is ...
            else prefer(message_text(self.message_text), self.message_text),
            parse_mode=self.parse_mode
            if parse_mode is ...
            else prefer(parse_mode(self.parse_mode), self.parse_mode),
            entities=self.entities
            if entities is ...
            else prefer(entities(self.entities), self.entities),
            disable_web_page_preview=self.disable_web_page_preview
            if disable_web_page_preview is ...
            else prefer(
                disable_web_page_preview(self.disable_web_page_preview),
                self.disable_web_page_preview,
            ),
        )

    def copy_with(
        self,
        message_text: str | EllipsisType = ...,
        parse_mode: str | None | EllipsisType = ...,
        entities: list[MessageEntity] | None | EllipsisType = ...,
        disable_web_page_preview: bool | None | EllipsisType = ...,
    ) -> InputTextMessageContent:
        """Replaces some of model's fields with provided ones"""
        return InputTextMessageContent(
            message_text=message_text if message_text is not ... else self.message_text,
            parse_mode=parse_mode if parse_mode is not ... else self.parse_mode,
            entities=entities if entities is not ... else self.entities,
            disable_web_page_preview=disable_web_page_preview
            if disable_web_page_preview is not ...
            else self.disable_web_page_preview,
        )


@dataclass(frozen=False, slots=True)
class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query."""

    latitude: float
    """Latitude of the location in degrees """
    longitude: float
    """Longitude of the location in degrees """
    horizontal_accuracy: float | None = None
    """Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    live_period: int | None = None
    """Optional. Period in seconds for which the location can be updated, should be between 60 and 86400. """
    heading: int | None = None
    """Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. """
    proximity_alert_radius: int | None = None
    """Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        latitude: AlterFn[float] | EllipsisType = ...,
        longitude: AlterFn[float] | EllipsisType = ...,
        horizontal_accuracy: AlterFn[float | None] | EllipsisType = ...,
        live_period: AlterFn[int | None] | EllipsisType = ...,
        heading: AlterFn[int | None] | EllipsisType = ...,
        proximity_alert_radius: AlterFn[int | None] | EllipsisType = ...,
    ) -> InputLocationMessageContent:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputLocationMessageContent(
            latitude=self.latitude
            if latitude is ...
            else prefer(latitude(self.latitude), self.latitude),
            longitude=self.longitude
            if longitude is ...
            else prefer(longitude(self.longitude), self.longitude),
            horizontal_accuracy=self.horizontal_accuracy
            if horizontal_accuracy is ...
            else prefer(
                horizontal_accuracy(self.horizontal_accuracy), self.horizontal_accuracy
            ),
            live_period=self.live_period
            if live_period is ...
            else prefer(live_period(self.live_period), self.live_period),
            heading=self.heading
            if heading is ...
            else prefer(heading(self.heading), self.heading),
            proximity_alert_radius=self.proximity_alert_radius
            if proximity_alert_radius is ...
            else prefer(
                proximity_alert_radius(self.proximity_alert_radius),
                self.proximity_alert_radius,
            ),
        )

    def copy_with(
        self,
        latitude: float | EllipsisType = ...,
        longitude: float | EllipsisType = ...,
        horizontal_accuracy: float | None | EllipsisType = ...,
        live_period: int | None | EllipsisType = ...,
        heading: int | None | EllipsisType = ...,
        proximity_alert_radius: int | None | EllipsisType = ...,
    ) -> InputLocationMessageContent:
        """Replaces some of model's fields with provided ones"""
        return InputLocationMessageContent(
            latitude=latitude if latitude is not ... else self.latitude,
            longitude=longitude if longitude is not ... else self.longitude,
            horizontal_accuracy=horizontal_accuracy
            if horizontal_accuracy is not ...
            else self.horizontal_accuracy,
            live_period=live_period if live_period is not ... else self.live_period,
            heading=heading if heading is not ... else self.heading,
            proximity_alert_radius=proximity_alert_radius
            if proximity_alert_radius is not ...
            else self.proximity_alert_radius,
        )


@dataclass(frozen=False, slots=True)
class InputVenueMessageContent:
    """Represents the content of a venue message to be sent as the result of an inline query."""

    latitude: float
    """Latitude of the venue in degrees """
    longitude: float
    """Longitude of the venue in degrees """
    title: str
    """Name of the venue """
    address: str
    """Address of the venue """
    foursquare_id: str | None = None
    """Optional. Foursquare identifier of the venue, if known """
    foursquare_type: str | None = None
    """Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str | None = None
    """Optional. Google Places identifier of the venue """
    google_place_type: str | None = None
    """Optional. Google Places type of the venue. (See supported types.) """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        latitude: AlterFn[float] | EllipsisType = ...,
        longitude: AlterFn[float] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        address: AlterFn[str] | EllipsisType = ...,
        foursquare_id: AlterFn[str | None] | EllipsisType = ...,
        foursquare_type: AlterFn[str | None] | EllipsisType = ...,
        google_place_id: AlterFn[str | None] | EllipsisType = ...,
        google_place_type: AlterFn[str | None] | EllipsisType = ...,
    ) -> InputVenueMessageContent:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputVenueMessageContent(
            latitude=self.latitude
            if latitude is ...
            else prefer(latitude(self.latitude), self.latitude),
            longitude=self.longitude
            if longitude is ...
            else prefer(longitude(self.longitude), self.longitude),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            address=self.address
            if address is ...
            else prefer(address(self.address), self.address),
            foursquare_id=self.foursquare_id
            if foursquare_id is ...
            else prefer(foursquare_id(self.foursquare_id), self.foursquare_id),
            foursquare_type=self.foursquare_type
            if foursquare_type is ...
            else prefer(foursquare_type(self.foursquare_type), self.foursquare_type),
            google_place_id=self.google_place_id
            if google_place_id is ...
            else prefer(google_place_id(self.google_place_id), self.google_place_id),
            google_place_type=self.google_place_type
            if google_place_type is ...
            else prefer(
                google_place_type(self.google_place_type), self.google_place_type
            ),
        )

    def copy_with(
        self,
        latitude: float | EllipsisType = ...,
        longitude: float | EllipsisType = ...,
        title: str | EllipsisType = ...,
        address: str | EllipsisType = ...,
        foursquare_id: str | None | EllipsisType = ...,
        foursquare_type: str | None | EllipsisType = ...,
        google_place_id: str | None | EllipsisType = ...,
        google_place_type: str | None | EllipsisType = ...,
    ) -> InputVenueMessageContent:
        """Replaces some of model's fields with provided ones"""
        return InputVenueMessageContent(
            latitude=latitude if latitude is not ... else self.latitude,
            longitude=longitude if longitude is not ... else self.longitude,
            title=title if title is not ... else self.title,
            address=address if address is not ... else self.address,
            foursquare_id=foursquare_id
            if foursquare_id is not ...
            else self.foursquare_id,
            foursquare_type=foursquare_type
            if foursquare_type is not ...
            else self.foursquare_type,
            google_place_id=google_place_id
            if google_place_id is not ...
            else self.google_place_id,
            google_place_type=google_place_type
            if google_place_type is not ...
            else self.google_place_type,
        )


@dataclass(frozen=False, slots=True)
class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query."""

    phone_number: str
    """Contact's phone number """
    first_name: str
    """Contact's first name """
    last_name: str | None = None
    """Optional. Contact's last name """
    vcard: str | None = None
    """Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        phone_number: AlterFn[str] | EllipsisType = ...,
        first_name: AlterFn[str] | EllipsisType = ...,
        last_name: AlterFn[str | None] | EllipsisType = ...,
        vcard: AlterFn[str | None] | EllipsisType = ...,
    ) -> InputContactMessageContent:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputContactMessageContent(
            phone_number=self.phone_number
            if phone_number is ...
            else prefer(phone_number(self.phone_number), self.phone_number),
            first_name=self.first_name
            if first_name is ...
            else prefer(first_name(self.first_name), self.first_name),
            last_name=self.last_name
            if last_name is ...
            else prefer(last_name(self.last_name), self.last_name),
            vcard=self.vcard if vcard is ... else prefer(vcard(self.vcard), self.vcard),
        )

    def copy_with(
        self,
        phone_number: str | EllipsisType = ...,
        first_name: str | EllipsisType = ...,
        last_name: str | None | EllipsisType = ...,
        vcard: str | None | EllipsisType = ...,
    ) -> InputContactMessageContent:
        """Replaces some of model's fields with provided ones"""
        return InputContactMessageContent(
            phone_number=phone_number if phone_number is not ... else self.phone_number,
            first_name=first_name if first_name is not ... else self.first_name,
            last_name=last_name if last_name is not ... else self.last_name,
            vcard=vcard if vcard is not ... else self.vcard,
        )


@dataclass(frozen=False, slots=True)
class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query."""

    title: str
    """Product name, 1-32 characters """
    description: str
    """Product description, 1-255 characters """
    payload: str
    """Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes. """
    provider_token: str
    """Payment provider token, obtained via @BotFather """
    currency: str
    """Three-letter ISO 4217 currency code, see more on currencies """
    prices: list[LabeledPrice]
    """Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.) """
    max_tip_amount: int | None = None
    """Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0 """
    suggested_tip_amounts: list[int] | None = None
    """Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount. """
    provider_data: str | None = None
    """Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider. """
    photo_url: str | None = None
    """Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. """
    photo_size: int | None = None
    """Optional. Photo size in bytes """
    photo_width: int | None = None
    """Optional. Photo width """
    photo_height: int | None = None
    """Optional. Photo height """
    need_name: bool | None = None
    """Optional. Pass True if you require the user's full name to complete the order """
    need_phone_number: bool | None = None
    """Optional. Pass True if you require the user's phone number to complete the order """
    need_email: bool | None = None
    """Optional. Pass True if you require the user's email address to complete the order """
    need_shipping_address: bool | None = None
    """Optional. Pass True if you require the user's shipping address to complete the order """
    send_phone_number_to_provider: bool | None = None
    """Optional. Pass True if the user's phone number should be sent to provider """
    send_email_to_provider: bool | None = None
    """Optional. Pass True if the user's email address should be sent to provider """
    is_flexible: bool | None = None
    """Optional. Pass True if the final price depends on the shipping method """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        title: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str] | EllipsisType = ...,
        payload: AlterFn[str] | EllipsisType = ...,
        provider_token: AlterFn[str] | EllipsisType = ...,
        currency: AlterFn[str] | EllipsisType = ...,
        prices: AlterFn[list[LabeledPrice]] | EllipsisType = ...,
        max_tip_amount: AlterFn[int | None] | EllipsisType = ...,
        suggested_tip_amounts: AlterFn[list[int] | None] | EllipsisType = ...,
        provider_data: AlterFn[str | None] | EllipsisType = ...,
        photo_url: AlterFn[str | None] | EllipsisType = ...,
        photo_size: AlterFn[int | None] | EllipsisType = ...,
        photo_width: AlterFn[int | None] | EllipsisType = ...,
        photo_height: AlterFn[int | None] | EllipsisType = ...,
        need_name: AlterFn[bool | None] | EllipsisType = ...,
        need_phone_number: AlterFn[bool | None] | EllipsisType = ...,
        need_email: AlterFn[bool | None] | EllipsisType = ...,
        need_shipping_address: AlterFn[bool | None] | EllipsisType = ...,
        send_phone_number_to_provider: AlterFn[bool | None] | EllipsisType = ...,
        send_email_to_provider: AlterFn[bool | None] | EllipsisType = ...,
        is_flexible: AlterFn[bool | None] | EllipsisType = ...,
    ) -> InputInvoiceMessageContent:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return InputInvoiceMessageContent(
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            payload=self.payload
            if payload is ...
            else prefer(payload(self.payload), self.payload),
            provider_token=self.provider_token
            if provider_token is ...
            else prefer(provider_token(self.provider_token), self.provider_token),
            currency=self.currency
            if currency is ...
            else prefer(currency(self.currency), self.currency),
            prices=self.prices
            if prices is ...
            else prefer(prices(self.prices), self.prices),
            max_tip_amount=self.max_tip_amount
            if max_tip_amount is ...
            else prefer(max_tip_amount(self.max_tip_amount), self.max_tip_amount),
            suggested_tip_amounts=self.suggested_tip_amounts
            if suggested_tip_amounts is ...
            else prefer(
                suggested_tip_amounts(self.suggested_tip_amounts),
                self.suggested_tip_amounts,
            ),
            provider_data=self.provider_data
            if provider_data is ...
            else prefer(provider_data(self.provider_data), self.provider_data),
            photo_url=self.photo_url
            if photo_url is ...
            else prefer(photo_url(self.photo_url), self.photo_url),
            photo_size=self.photo_size
            if photo_size is ...
            else prefer(photo_size(self.photo_size), self.photo_size),
            photo_width=self.photo_width
            if photo_width is ...
            else prefer(photo_width(self.photo_width), self.photo_width),
            photo_height=self.photo_height
            if photo_height is ...
            else prefer(photo_height(self.photo_height), self.photo_height),
            need_name=self.need_name
            if need_name is ...
            else prefer(need_name(self.need_name), self.need_name),
            need_phone_number=self.need_phone_number
            if need_phone_number is ...
            else prefer(
                need_phone_number(self.need_phone_number), self.need_phone_number
            ),
            need_email=self.need_email
            if need_email is ...
            else prefer(need_email(self.need_email), self.need_email),
            need_shipping_address=self.need_shipping_address
            if need_shipping_address is ...
            else prefer(
                need_shipping_address(self.need_shipping_address),
                self.need_shipping_address,
            ),
            send_phone_number_to_provider=self.send_phone_number_to_provider
            if send_phone_number_to_provider is ...
            else prefer(
                send_phone_number_to_provider(self.send_phone_number_to_provider),
                self.send_phone_number_to_provider,
            ),
            send_email_to_provider=self.send_email_to_provider
            if send_email_to_provider is ...
            else prefer(
                send_email_to_provider(self.send_email_to_provider),
                self.send_email_to_provider,
            ),
            is_flexible=self.is_flexible
            if is_flexible is ...
            else prefer(is_flexible(self.is_flexible), self.is_flexible),
        )

    def copy_with(
        self,
        title: str | EllipsisType = ...,
        description: str | EllipsisType = ...,
        payload: str | EllipsisType = ...,
        provider_token: str | EllipsisType = ...,
        currency: str | EllipsisType = ...,
        prices: list[LabeledPrice] | EllipsisType = ...,
        max_tip_amount: int | None | EllipsisType = ...,
        suggested_tip_amounts: list[int] | None | EllipsisType = ...,
        provider_data: str | None | EllipsisType = ...,
        photo_url: str | None | EllipsisType = ...,
        photo_size: int | None | EllipsisType = ...,
        photo_width: int | None | EllipsisType = ...,
        photo_height: int | None | EllipsisType = ...,
        need_name: bool | None | EllipsisType = ...,
        need_phone_number: bool | None | EllipsisType = ...,
        need_email: bool | None | EllipsisType = ...,
        need_shipping_address: bool | None | EllipsisType = ...,
        send_phone_number_to_provider: bool | None | EllipsisType = ...,
        send_email_to_provider: bool | None | EllipsisType = ...,
        is_flexible: bool | None | EllipsisType = ...,
    ) -> InputInvoiceMessageContent:
        """Replaces some of model's fields with provided ones"""
        return InputInvoiceMessageContent(
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            payload=payload if payload is not ... else self.payload,
            provider_token=provider_token
            if provider_token is not ...
            else self.provider_token,
            currency=currency if currency is not ... else self.currency,
            prices=prices if prices is not ... else self.prices,
            max_tip_amount=max_tip_amount
            if max_tip_amount is not ...
            else self.max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts
            if suggested_tip_amounts is not ...
            else self.suggested_tip_amounts,
            provider_data=provider_data
            if provider_data is not ...
            else self.provider_data,
            photo_url=photo_url if photo_url is not ... else self.photo_url,
            photo_size=photo_size if photo_size is not ... else self.photo_size,
            photo_width=photo_width if photo_width is not ... else self.photo_width,
            photo_height=photo_height if photo_height is not ... else self.photo_height,
            need_name=need_name if need_name is not ... else self.need_name,
            need_phone_number=need_phone_number
            if need_phone_number is not ...
            else self.need_phone_number,
            need_email=need_email if need_email is not ... else self.need_email,
            need_shipping_address=need_shipping_address
            if need_shipping_address is not ...
            else self.need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider
            if send_phone_number_to_provider is not ...
            else self.send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider
            if send_email_to_provider is not ...
            else self.send_email_to_provider,
            is_flexible=is_flexible if is_flexible is not ... else self.is_flexible,
        )


@dataclass(frozen=False, slots=True)
class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.
    """

    result_id: str
    """The unique identifier for the result that was chosen """
    from_: User
    """The user that chose the result """
    query: str
    """The query that was used to obtain the result """
    location: Location | None = None
    """Optional. Sender location, only for bots that require user location """
    inline_message_id: str | None = None
    """Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        result_id: AlterFn[str] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        location: AlterFn[Location | None] | EllipsisType = ...,
        inline_message_id: AlterFn[str | None] | EllipsisType = ...,
        query: AlterFn[str] | EllipsisType = ...,
    ) -> ChosenInlineResult:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ChosenInlineResult(
            result_id=self.result_id
            if result_id is ...
            else prefer(result_id(self.result_id), self.result_id),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            location=self.location
            if location is ...
            else prefer(location(self.location), self.location),
            inline_message_id=self.inline_message_id
            if inline_message_id is ...
            else prefer(
                inline_message_id(self.inline_message_id), self.inline_message_id
            ),
            query=self.query if query is ... else prefer(query(self.query), self.query),
        )

    def copy_with(
        self,
        result_id: str | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        location: Location | None | EllipsisType = ...,
        inline_message_id: str | None | EllipsisType = ...,
        query: str | EllipsisType = ...,
    ) -> ChosenInlineResult:
        """Replaces some of model's fields with provided ones"""
        return ChosenInlineResult(
            result_id=result_id if result_id is not ... else self.result_id,
            from_=from_ if from_ is not ... else self.from_,
            location=location if location is not ... else self.location,
            inline_message_id=inline_message_id
            if inline_message_id is not ...
            else self.inline_message_id,
            query=query if query is not ... else self.query,
        )


@dataclass(frozen=False, slots=True)
class SentWebAppMessage:
    """Describes an inline message sent by a Web App on behalf of a user."""

    inline_message_id: str | None = None
    """Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        inline_message_id: AlterFn[str | None] | EllipsisType = ...,
    ) -> SentWebAppMessage:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return SentWebAppMessage(
            inline_message_id=self.inline_message_id
            if inline_message_id is ...
            else prefer(
                inline_message_id(self.inline_message_id), self.inline_message_id
            )
        )

    def copy_with(
        self,
        inline_message_id: str | None | EllipsisType = ...,
    ) -> SentWebAppMessage:
        """Replaces some of model's fields with provided ones"""
        return SentWebAppMessage(
            inline_message_id=inline_message_id
            if inline_message_id is not ...
            else self.inline_message_id
        )


@dataclass(frozen=False, slots=True)
class LabeledPrice:
    """This object represents a portion of the price for goods or services."""

    label: str
    """Portion label """
    amount: int
    """Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        label: AlterFn[str] | EllipsisType = ...,
        amount: AlterFn[int] | EllipsisType = ...,
    ) -> LabeledPrice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return LabeledPrice(
            label=self.label if label is ... else prefer(label(self.label), self.label),
            amount=self.amount
            if amount is ...
            else prefer(amount(self.amount), self.amount),
        )

    def copy_with(
        self,
        label: str | EllipsisType = ...,
        amount: int | EllipsisType = ...,
    ) -> LabeledPrice:
        """Replaces some of model's fields with provided ones"""
        return LabeledPrice(
            label=label if label is not ... else self.label,
            amount=amount if amount is not ... else self.amount,
        )


@dataclass(frozen=False, slots=True)
class Invoice:
    """This object contains basic information about an invoice."""

    title: str
    """Product name """
    description: str
    """Product description """
    start_parameter: str
    """Unique bot deep-linking parameter that can be used to generate this invoice """
    currency: str
    """Three-letter ISO 4217 currency code """
    total_amount: int
    """Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        title: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str] | EllipsisType = ...,
        start_parameter: AlterFn[str] | EllipsisType = ...,
        currency: AlterFn[str] | EllipsisType = ...,
        total_amount: AlterFn[int] | EllipsisType = ...,
    ) -> Invoice:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Invoice(
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            start_parameter=self.start_parameter
            if start_parameter is ...
            else prefer(start_parameter(self.start_parameter), self.start_parameter),
            currency=self.currency
            if currency is ...
            else prefer(currency(self.currency), self.currency),
            total_amount=self.total_amount
            if total_amount is ...
            else prefer(total_amount(self.total_amount), self.total_amount),
        )

    def copy_with(
        self,
        title: str | EllipsisType = ...,
        description: str | EllipsisType = ...,
        start_parameter: str | EllipsisType = ...,
        currency: str | EllipsisType = ...,
        total_amount: int | EllipsisType = ...,
    ) -> Invoice:
        """Replaces some of model's fields with provided ones"""
        return Invoice(
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            start_parameter=start_parameter
            if start_parameter is not ...
            else self.start_parameter,
            currency=currency if currency is not ... else self.currency,
            total_amount=total_amount if total_amount is not ... else self.total_amount,
        )


@dataclass(frozen=False, slots=True)
class ShippingAddress:
    """This object represents a shipping address."""

    country_code: str
    """Two-letter ISO 3166-1 alpha-2 country code """
    state: str
    """State, if applicable """
    city: str
    """City """
    street_line1: str
    """First line for the address """
    street_line2: str
    """Second line for the address """
    post_code: str
    """Address post code """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        country_code: AlterFn[str] | EllipsisType = ...,
        state: AlterFn[str] | EllipsisType = ...,
        city: AlterFn[str] | EllipsisType = ...,
        street_line1: AlterFn[str] | EllipsisType = ...,
        street_line2: AlterFn[str] | EllipsisType = ...,
        post_code: AlterFn[str] | EllipsisType = ...,
    ) -> ShippingAddress:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ShippingAddress(
            country_code=self.country_code
            if country_code is ...
            else prefer(country_code(self.country_code), self.country_code),
            state=self.state if state is ... else prefer(state(self.state), self.state),
            city=self.city if city is ... else prefer(city(self.city), self.city),
            street_line1=self.street_line1
            if street_line1 is ...
            else prefer(street_line1(self.street_line1), self.street_line1),
            street_line2=self.street_line2
            if street_line2 is ...
            else prefer(street_line2(self.street_line2), self.street_line2),
            post_code=self.post_code
            if post_code is ...
            else prefer(post_code(self.post_code), self.post_code),
        )

    def copy_with(
        self,
        country_code: str | EllipsisType = ...,
        state: str | EllipsisType = ...,
        city: str | EllipsisType = ...,
        street_line1: str | EllipsisType = ...,
        street_line2: str | EllipsisType = ...,
        post_code: str | EllipsisType = ...,
    ) -> ShippingAddress:
        """Replaces some of model's fields with provided ones"""
        return ShippingAddress(
            country_code=country_code if country_code is not ... else self.country_code,
            state=state if state is not ... else self.state,
            city=city if city is not ... else self.city,
            street_line1=street_line1 if street_line1 is not ... else self.street_line1,
            street_line2=street_line2 if street_line2 is not ... else self.street_line2,
            post_code=post_code if post_code is not ... else self.post_code,
        )


@dataclass(frozen=False, slots=True)
class OrderInfo:
    """This object represents information about an order."""

    name: str | None = None
    """Optional. User name """
    phone_number: str | None = None
    """Optional. User's phone number """
    email: str | None = None
    """Optional. User email """
    shipping_address: ShippingAddress | None = None
    """Optional. User shipping address """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        name: AlterFn[str | None] | EllipsisType = ...,
        phone_number: AlterFn[str | None] | EllipsisType = ...,
        email: AlterFn[str | None] | EllipsisType = ...,
        shipping_address: AlterFn[ShippingAddress | None] | EllipsisType = ...,
    ) -> OrderInfo:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return OrderInfo(
            name=self.name if name is ... else prefer(name(self.name), self.name),
            phone_number=self.phone_number
            if phone_number is ...
            else prefer(phone_number(self.phone_number), self.phone_number),
            email=self.email if email is ... else prefer(email(self.email), self.email),
            shipping_address=self.shipping_address
            if shipping_address is ...
            else prefer(shipping_address(self.shipping_address), self.shipping_address),
        )

    def copy_with(
        self,
        name: str | None | EllipsisType = ...,
        phone_number: str | None | EllipsisType = ...,
        email: str | None | EllipsisType = ...,
        shipping_address: ShippingAddress | None | EllipsisType = ...,
    ) -> OrderInfo:
        """Replaces some of model's fields with provided ones"""
        return OrderInfo(
            name=name if name is not ... else self.name,
            phone_number=phone_number if phone_number is not ... else self.phone_number,
            email=email if email is not ... else self.email,
            shipping_address=shipping_address
            if shipping_address is not ...
            else self.shipping_address,
        )


@dataclass(frozen=False, slots=True)
class ShippingOption:
    """This object represents one shipping option."""

    id: str
    """Shipping option identifier """
    title: str
    """Option title """
    prices: list[LabeledPrice]
    """List of price portions """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        title: AlterFn[str] | EllipsisType = ...,
        prices: AlterFn[list[LabeledPrice]] | EllipsisType = ...,
    ) -> ShippingOption:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ShippingOption(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            title=self.title if title is ... else prefer(title(self.title), self.title),
            prices=self.prices
            if prices is ...
            else prefer(prices(self.prices), self.prices),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        title: str | EllipsisType = ...,
        prices: list[LabeledPrice] | EllipsisType = ...,
    ) -> ShippingOption:
        """Replaces some of model's fields with provided ones"""
        return ShippingOption(
            id=id if id is not ... else self.id,
            title=title if title is not ... else self.title,
            prices=prices if prices is not ... else self.prices,
        )


@dataclass(frozen=False, slots=True)
class SuccessfulPayment:
    """This object contains basic information about a successful payment."""

    currency: str
    """Three-letter ISO 4217 currency code """
    total_amount: int
    """Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """
    invoice_payload: str
    """Bot specified invoice payload """
    telegram_payment_charge_id: str
    """Telegram payment identifier """
    provider_payment_charge_id: str
    """Provider payment identifier """
    shipping_option_id: str | None = None
    """Optional. Identifier of the shipping option chosen by the user """
    order_info: OrderInfo | None = None
    """Optional. Order information provided by the user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        currency: AlterFn[str] | EllipsisType = ...,
        total_amount: AlterFn[int] | EllipsisType = ...,
        invoice_payload: AlterFn[str] | EllipsisType = ...,
        shipping_option_id: AlterFn[str | None] | EllipsisType = ...,
        order_info: AlterFn[OrderInfo | None] | EllipsisType = ...,
        telegram_payment_charge_id: AlterFn[str] | EllipsisType = ...,
        provider_payment_charge_id: AlterFn[str] | EllipsisType = ...,
    ) -> SuccessfulPayment:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return SuccessfulPayment(
            currency=self.currency
            if currency is ...
            else prefer(currency(self.currency), self.currency),
            total_amount=self.total_amount
            if total_amount is ...
            else prefer(total_amount(self.total_amount), self.total_amount),
            invoice_payload=self.invoice_payload
            if invoice_payload is ...
            else prefer(invoice_payload(self.invoice_payload), self.invoice_payload),
            shipping_option_id=self.shipping_option_id
            if shipping_option_id is ...
            else prefer(
                shipping_option_id(self.shipping_option_id), self.shipping_option_id
            ),
            order_info=self.order_info
            if order_info is ...
            else prefer(order_info(self.order_info), self.order_info),
            telegram_payment_charge_id=self.telegram_payment_charge_id
            if telegram_payment_charge_id is ...
            else prefer(
                telegram_payment_charge_id(self.telegram_payment_charge_id),
                self.telegram_payment_charge_id,
            ),
            provider_payment_charge_id=self.provider_payment_charge_id
            if provider_payment_charge_id is ...
            else prefer(
                provider_payment_charge_id(self.provider_payment_charge_id),
                self.provider_payment_charge_id,
            ),
        )

    def copy_with(
        self,
        currency: str | EllipsisType = ...,
        total_amount: int | EllipsisType = ...,
        invoice_payload: str | EllipsisType = ...,
        shipping_option_id: str | None | EllipsisType = ...,
        order_info: OrderInfo | None | EllipsisType = ...,
        telegram_payment_charge_id: str | EllipsisType = ...,
        provider_payment_charge_id: str | EllipsisType = ...,
    ) -> SuccessfulPayment:
        """Replaces some of model's fields with provided ones"""
        return SuccessfulPayment(
            currency=currency if currency is not ... else self.currency,
            total_amount=total_amount if total_amount is not ... else self.total_amount,
            invoice_payload=invoice_payload
            if invoice_payload is not ...
            else self.invoice_payload,
            shipping_option_id=shipping_option_id
            if shipping_option_id is not ...
            else self.shipping_option_id,
            order_info=order_info if order_info is not ... else self.order_info,
            telegram_payment_charge_id=telegram_payment_charge_id
            if telegram_payment_charge_id is not ...
            else self.telegram_payment_charge_id,
            provider_payment_charge_id=provider_payment_charge_id
            if provider_payment_charge_id is not ...
            else self.provider_payment_charge_id,
        )


@dataclass(frozen=False, slots=True)
class ShippingQuery:
    """This object contains information about an incoming shipping query."""

    id: str
    """Unique query identifier """
    from_: User
    """User who sent the query """
    invoice_payload: str
    """Bot specified invoice payload """
    shipping_address: ShippingAddress
    """User specified shipping address """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        invoice_payload: AlterFn[str] | EllipsisType = ...,
        shipping_address: AlterFn[ShippingAddress] | EllipsisType = ...,
    ) -> ShippingQuery:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return ShippingQuery(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            invoice_payload=self.invoice_payload
            if invoice_payload is ...
            else prefer(invoice_payload(self.invoice_payload), self.invoice_payload),
            shipping_address=self.shipping_address
            if shipping_address is ...
            else prefer(shipping_address(self.shipping_address), self.shipping_address),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        invoice_payload: str | EllipsisType = ...,
        shipping_address: ShippingAddress | EllipsisType = ...,
    ) -> ShippingQuery:
        """Replaces some of model's fields with provided ones"""
        return ShippingQuery(
            id=id if id is not ... else self.id,
            from_=from_ if from_ is not ... else self.from_,
            invoice_payload=invoice_payload
            if invoice_payload is not ...
            else self.invoice_payload,
            shipping_address=shipping_address
            if shipping_address is not ...
            else self.shipping_address,
        )


@dataclass(frozen=False, slots=True)
class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query."""

    id: str
    """Unique query identifier """
    from_: User
    """User who sent the query """
    currency: str
    """Three-letter ISO 4217 currency code """
    total_amount: int
    """Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). """
    invoice_payload: str
    """Bot specified invoice payload """
    shipping_option_id: str | None = None
    """Optional. Identifier of the shipping option chosen by the user """
    order_info: OrderInfo | None = None
    """Optional. Order information provided by the user """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        id: AlterFn[str] | EllipsisType = ...,
        from_: AlterFn[User] | EllipsisType = ...,
        currency: AlterFn[str] | EllipsisType = ...,
        total_amount: AlterFn[int] | EllipsisType = ...,
        invoice_payload: AlterFn[str] | EllipsisType = ...,
        shipping_option_id: AlterFn[str | None] | EllipsisType = ...,
        order_info: AlterFn[OrderInfo | None] | EllipsisType = ...,
    ) -> PreCheckoutQuery:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PreCheckoutQuery(
            id=self.id if id is ... else prefer(id(self.id), self.id),
            from_=self.from_ if from_ is ... else prefer(from_(self.from_), self.from_),
            currency=self.currency
            if currency is ...
            else prefer(currency(self.currency), self.currency),
            total_amount=self.total_amount
            if total_amount is ...
            else prefer(total_amount(self.total_amount), self.total_amount),
            invoice_payload=self.invoice_payload
            if invoice_payload is ...
            else prefer(invoice_payload(self.invoice_payload), self.invoice_payload),
            shipping_option_id=self.shipping_option_id
            if shipping_option_id is ...
            else prefer(
                shipping_option_id(self.shipping_option_id), self.shipping_option_id
            ),
            order_info=self.order_info
            if order_info is ...
            else prefer(order_info(self.order_info), self.order_info),
        )

    def copy_with(
        self,
        id: str | EllipsisType = ...,
        from_: User | EllipsisType = ...,
        currency: str | EllipsisType = ...,
        total_amount: int | EllipsisType = ...,
        invoice_payload: str | EllipsisType = ...,
        shipping_option_id: str | None | EllipsisType = ...,
        order_info: OrderInfo | None | EllipsisType = ...,
    ) -> PreCheckoutQuery:
        """Replaces some of model's fields with provided ones"""
        return PreCheckoutQuery(
            id=id if id is not ... else self.id,
            from_=from_ if from_ is not ... else self.from_,
            currency=currency if currency is not ... else self.currency,
            total_amount=total_amount if total_amount is not ... else self.total_amount,
            invoice_payload=invoice_payload
            if invoice_payload is not ...
            else self.invoice_payload,
            shipping_option_id=shipping_option_id
            if shipping_option_id is not ...
            else self.shipping_option_id,
            order_info=order_info if order_info is not ... else self.order_info,
        )


@dataclass(frozen=False, slots=True)
class PassportData:
    """Describes Telegram Passport data shared with the bot by the user."""

    data: list[EncryptedPassportElement]
    """Array with information about documents and other Telegram Passport elements that was shared with the bot """
    credentials: EncryptedCredentials
    """Encrypted credentials required to decrypt the data """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        data: AlterFn[list[EncryptedPassportElement]] | EllipsisType = ...,
        credentials: AlterFn[EncryptedCredentials] | EllipsisType = ...,
    ) -> PassportData:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportData(
            data=self.data if data is ... else prefer(data(self.data), self.data),
            credentials=self.credentials
            if credentials is ...
            else prefer(credentials(self.credentials), self.credentials),
        )

    def copy_with(
        self,
        data: list[EncryptedPassportElement] | EllipsisType = ...,
        credentials: EncryptedCredentials | EllipsisType = ...,
    ) -> PassportData:
        """Replaces some of model's fields with provided ones"""
        return PassportData(
            data=data if data is not ... else self.data,
            credentials=credentials if credentials is not ... else self.credentials,
        )


@dataclass(frozen=False, slots=True)
class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB."""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    file_size: int
    """File size in bytes """
    file_date: int
    """Unix time when the file was uploaded """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        file_id: AlterFn[str] | EllipsisType = ...,
        file_unique_id: AlterFn[str] | EllipsisType = ...,
        file_size: AlterFn[int] | EllipsisType = ...,
        file_date: AlterFn[int] | EllipsisType = ...,
    ) -> PassportFile:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportFile(
            file_id=self.file_id
            if file_id is ...
            else prefer(file_id(self.file_id), self.file_id),
            file_unique_id=self.file_unique_id
            if file_unique_id is ...
            else prefer(file_unique_id(self.file_unique_id), self.file_unique_id),
            file_size=self.file_size
            if file_size is ...
            else prefer(file_size(self.file_size), self.file_size),
            file_date=self.file_date
            if file_date is ...
            else prefer(file_date(self.file_date), self.file_date),
        )

    def copy_with(
        self,
        file_id: str | EllipsisType = ...,
        file_unique_id: str | EllipsisType = ...,
        file_size: int | EllipsisType = ...,
        file_date: int | EllipsisType = ...,
    ) -> PassportFile:
        """Replaces some of model's fields with provided ones"""
        return PassportFile(
            file_id=file_id if file_id is not ... else self.file_id,
            file_unique_id=file_unique_id
            if file_unique_id is not ...
            else self.file_unique_id,
            file_size=file_size if file_size is not ... else self.file_size,
            file_date=file_date if file_date is not ... else self.file_date,
        )


@dataclass(frozen=False, slots=True)
class EncryptedPassportElement:
    """Describes documents or other Telegram Passport elements shared with the bot by the user."""

    type: str
    """Element type. One of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration", "phone_number", "email". """
    hash: str
    """Base64-encoded element hash for using in PassportElementErrorUnspecified """
    data: str | None = None
    """Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for "personal_details", "passport", "driver_license", "identity_card", "internal_passport" and "address" types. Can be decrypted and verified using the accompanying EncryptedCredentials. """
    phone_number: str | None = None
    """Optional. User's verified phone number, available only for "phone_number" type """
    email: str | None = None
    """Optional. User's verified email address, available only for "email" type """
    files: list[PassportFile] | None = None
    """Optional. Array of encrypted files with documents provided by the user, available for "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials. """
    front_side: PassportFile | None = None
    """Optional. Encrypted file with the front side of the document, provided by the user. Available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials. """
    reverse_side: PassportFile | None = None
    """Optional. Encrypted file with the reverse side of the document, provided by the user. Available for "driver_license" and "identity_card". The file can be decrypted and verified using the accompanying EncryptedCredentials. """
    selfie: PassportFile | None = None
    """Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials. """
    translation: list[PassportFile] | None = None
    """Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        type: AlterFn[str] | EllipsisType = ...,
        data: AlterFn[str | None] | EllipsisType = ...,
        phone_number: AlterFn[str | None] | EllipsisType = ...,
        email: AlterFn[str | None] | EllipsisType = ...,
        files: AlterFn[list[PassportFile] | None] | EllipsisType = ...,
        front_side: AlterFn[PassportFile | None] | EllipsisType = ...,
        reverse_side: AlterFn[PassportFile | None] | EllipsisType = ...,
        selfie: AlterFn[PassportFile | None] | EllipsisType = ...,
        translation: AlterFn[list[PassportFile] | None] | EllipsisType = ...,
        hash: AlterFn[str] | EllipsisType = ...,
    ) -> EncryptedPassportElement:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return EncryptedPassportElement(
            type=self.type if type is ... else prefer(type(self.type), self.type),
            data=self.data if data is ... else prefer(data(self.data), self.data),
            phone_number=self.phone_number
            if phone_number is ...
            else prefer(phone_number(self.phone_number), self.phone_number),
            email=self.email if email is ... else prefer(email(self.email), self.email),
            files=self.files if files is ... else prefer(files(self.files), self.files),
            front_side=self.front_side
            if front_side is ...
            else prefer(front_side(self.front_side), self.front_side),
            reverse_side=self.reverse_side
            if reverse_side is ...
            else prefer(reverse_side(self.reverse_side), self.reverse_side),
            selfie=self.selfie
            if selfie is ...
            else prefer(selfie(self.selfie), self.selfie),
            translation=self.translation
            if translation is ...
            else prefer(translation(self.translation), self.translation),
            hash=self.hash if hash is ... else prefer(hash(self.hash), self.hash),
        )

    def copy_with(
        self,
        type: str | EllipsisType = ...,
        data: str | None | EllipsisType = ...,
        phone_number: str | None | EllipsisType = ...,
        email: str | None | EllipsisType = ...,
        files: list[PassportFile] | None | EllipsisType = ...,
        front_side: PassportFile | None | EllipsisType = ...,
        reverse_side: PassportFile | None | EllipsisType = ...,
        selfie: PassportFile | None | EllipsisType = ...,
        translation: list[PassportFile] | None | EllipsisType = ...,
        hash: str | EllipsisType = ...,
    ) -> EncryptedPassportElement:
        """Replaces some of model's fields with provided ones"""
        return EncryptedPassportElement(
            type=type if type is not ... else self.type,
            data=data if data is not ... else self.data,
            phone_number=phone_number if phone_number is not ... else self.phone_number,
            email=email if email is not ... else self.email,
            files=files if files is not ... else self.files,
            front_side=front_side if front_side is not ... else self.front_side,
            reverse_side=reverse_side if reverse_side is not ... else self.reverse_side,
            selfie=selfie if selfie is not ... else self.selfie,
            translation=translation if translation is not ... else self.translation,
            hash=hash if hash is not ... else self.hash,
        )


@dataclass(frozen=False, slots=True)
class EncryptedCredentials:
    """Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes."""

    data: str
    """Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication """
    hash: str
    """Base64-encoded data hash for data authentication """
    secret: str
    """Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        data: AlterFn[str] | EllipsisType = ...,
        hash: AlterFn[str] | EllipsisType = ...,
        secret: AlterFn[str] | EllipsisType = ...,
    ) -> EncryptedCredentials:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return EncryptedCredentials(
            data=self.data if data is ... else prefer(data(self.data), self.data),
            hash=self.hash if hash is ... else prefer(hash(self.hash), self.hash),
            secret=self.secret
            if secret is ...
            else prefer(secret(self.secret), self.secret),
        )

    def copy_with(
        self,
        data: str | EllipsisType = ...,
        hash: str | EllipsisType = ...,
        secret: str | EllipsisType = ...,
    ) -> EncryptedCredentials:
        """Replaces some of model's fields with provided ones"""
        return EncryptedCredentials(
            data=data if data is not ... else self.data,
            hash=hash if hash is not ... else self.hash,
            secret=secret if secret is not ... else self.secret,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."""

    source: str
    """Error source, must be data """
    type: str
    """The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address" """
    field_name: str
    """Name of the data field which has the error """
    data_hash: str
    """Base64-encoded data hash """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        field_name: AlterFn[str] | EllipsisType = ...,
        data_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorDataField:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorDataField(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            field_name=self.field_name
            if field_name is ...
            else prefer(field_name(self.field_name), self.field_name),
            data_hash=self.data_hash
            if data_hash is ...
            else prefer(data_hash(self.data_hash), self.data_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        field_name: str | EllipsisType = ...,
        data_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorDataField:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorDataField(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            field_name=field_name if field_name is not ... else self.field_name,
            data_hash=data_hash if data_hash is not ... else self.data_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes."""

    source: str
    """Error source, must be front_side """
    type: str
    """The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport" """
    file_hash: str
    """Base64-encoded hash of the file with the front side of the document """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorFrontSide:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorFrontSide(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hash=self.file_hash
            if file_hash is ...
            else prefer(file_hash(self.file_hash), self.file_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorFrontSide:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorFrontSide(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hash=file_hash if file_hash is not ... else self.file_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes."""

    source: str
    """Error source, must be reverse_side """
    type: str
    """The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card" """
    file_hash: str
    """Base64-encoded hash of the file with the reverse side of the document """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorReverseSide:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorReverseSide(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hash=self.file_hash
            if file_hash is ...
            else prefer(file_hash(self.file_hash), self.file_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorReverseSide:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorReverseSide(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hash=file_hash if file_hash is not ... else self.file_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes."""

    source: str
    """Error source, must be selfie """
    type: str
    """The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport" """
    file_hash: str
    """Base64-encoded hash of the file with the selfie """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorSelfie:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorSelfie(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hash=self.file_hash
            if file_hash is ...
            else prefer(file_hash(self.file_hash), self.file_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorSelfie:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorSelfie(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hash=file_hash if file_hash is not ... else self.file_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes."""

    source: str
    """Error source, must be file """
    type: str
    """The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """
    file_hash: str
    """Base64-encoded file hash """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorFile:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorFile(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hash=self.file_hash
            if file_hash is ...
            else prefer(file_hash(self.file_hash), self.file_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorFile:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorFile(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hash=file_hash if file_hash is not ... else self.file_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."""

    source: str
    """Error source, must be files """
    type: str
    """The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """
    file_hashes: list[str]
    """List of base64-encoded file hashes """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hashes: AlterFn[list[str]] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorFiles:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorFiles(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hashes=self.file_hashes
            if file_hashes is ...
            else prefer(file_hashes(self.file_hashes), self.file_hashes),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hashes: list[str] | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorFiles:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorFiles(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hashes=file_hashes if file_hashes is not ... else self.file_hashes,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes."""

    source: str
    """Error source, must be translation_file """
    type: str
    """Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """
    file_hash: str
    """Base64-encoded file hash """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorTranslationFile:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorTranslationFile(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hash=self.file_hash
            if file_hash is ...
            else prefer(file_hash(self.file_hash), self.file_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorTranslationFile:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorTranslationFile(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hash=file_hash if file_hash is not ... else self.file_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change."""

    source: str
    """Error source, must be translation_files """
    type: str
    """Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """
    file_hashes: list[str]
    """List of base64-encoded file hashes """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        file_hashes: AlterFn[list[str]] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorTranslationFiles:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorTranslationFiles(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            file_hashes=self.file_hashes
            if file_hashes is ...
            else prefer(file_hashes(self.file_hashes), self.file_hashes),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        file_hashes: list[str] | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorTranslationFiles:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorTranslationFiles(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            file_hashes=file_hashes if file_hashes is not ... else self.file_hashes,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added."""

    source: str
    """Error source, must be unspecified """
    type: str
    """Type of element of the user's Telegram Passport which has the issue """
    element_hash: str
    """Base64-encoded element hash """
    message: str
    """Error message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        source: AlterFn[str] | EllipsisType = ...,
        type: AlterFn[str] | EllipsisType = ...,
        element_hash: AlterFn[str] | EllipsisType = ...,
        message: AlterFn[str] | EllipsisType = ...,
    ) -> PassportElementErrorUnspecified:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return PassportElementErrorUnspecified(
            source=self.source
            if source is ...
            else prefer(source(self.source), self.source),
            type=self.type if type is ... else prefer(type(self.type), self.type),
            element_hash=self.element_hash
            if element_hash is ...
            else prefer(element_hash(self.element_hash), self.element_hash),
            message=self.message
            if message is ...
            else prefer(message(self.message), self.message),
        )

    def copy_with(
        self,
        source: str | EllipsisType = ...,
        type: str | EllipsisType = ...,
        element_hash: str | EllipsisType = ...,
        message: str | EllipsisType = ...,
    ) -> PassportElementErrorUnspecified:
        """Replaces some of model's fields with provided ones"""
        return PassportElementErrorUnspecified(
            source=source if source is not ... else self.source,
            type=type if type is not ... else self.type,
            element_hash=element_hash if element_hash is not ... else self.element_hash,
            message=message if message is not ... else self.message,
        )


@dataclass(frozen=False, slots=True)
class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers."""

    title: str
    """Title of the game """
    description: str
    """Description of the game """
    photo: list[PhotoSize]
    """Photo that will be displayed in the game message in chats. """
    text: str | None = None
    """Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters. """
    text_entities: list[MessageEntity] | None = None
    """Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc. """
    animation: Animation | None = None
    """Optional. Animation that will be displayed in the game message in chats. Upload via BotFather """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        title: AlterFn[str] | EllipsisType = ...,
        description: AlterFn[str] | EllipsisType = ...,
        photo: AlterFn[list[PhotoSize]] | EllipsisType = ...,
        text: AlterFn[str | None] | EllipsisType = ...,
        text_entities: AlterFn[list[MessageEntity] | None] | EllipsisType = ...,
        animation: AlterFn[Animation | None] | EllipsisType = ...,
    ) -> Game:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return Game(
            title=self.title if title is ... else prefer(title(self.title), self.title),
            description=self.description
            if description is ...
            else prefer(description(self.description), self.description),
            photo=self.photo if photo is ... else prefer(photo(self.photo), self.photo),
            text=self.text if text is ... else prefer(text(self.text), self.text),
            text_entities=self.text_entities
            if text_entities is ...
            else prefer(text_entities(self.text_entities), self.text_entities),
            animation=self.animation
            if animation is ...
            else prefer(animation(self.animation), self.animation),
        )

    def copy_with(
        self,
        title: str | EllipsisType = ...,
        description: str | EllipsisType = ...,
        photo: list[PhotoSize] | EllipsisType = ...,
        text: str | None | EllipsisType = ...,
        text_entities: list[MessageEntity] | None | EllipsisType = ...,
        animation: Animation | None | EllipsisType = ...,
    ) -> Game:
        """Replaces some of model's fields with provided ones"""
        return Game(
            title=title if title is not ... else self.title,
            description=description if description is not ... else self.description,
            photo=photo if photo is not ... else self.photo,
            text=text if text is not ... else self.text,
            text_entities=text_entities
            if text_entities is not ...
            else self.text_entities,
            animation=animation if animation is not ... else self.animation,
        )


@dataclass(frozen=False, slots=True)
class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up your game."""

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
    ) -> CallbackGame:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return CallbackGame()

    def copy_with(
        self,
    ) -> CallbackGame:
        """Replaces some of model's fields with provided ones"""
        return CallbackGame()


@dataclass(frozen=False, slots=True)
class GameHighScore:
    """This object represents one row of the high scores table for a game."""

    position: int
    """Position in high score table for the game """
    user: User
    """User """
    score: int
    """Score """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass

    def alter(
        self,
        position: AlterFn[int] | EllipsisType = ...,
        user: AlterFn[User] | EllipsisType = ...,
        score: AlterFn[int] | EllipsisType = ...,
    ) -> GameHighScore:
        """Alters every type with the provided callable, if callable returns ... - field left untouched"""
        return GameHighScore(
            position=self.position
            if position is ...
            else prefer(position(self.position), self.position),
            user=self.user if user is ... else prefer(user(self.user), self.user),
            score=self.score if score is ... else prefer(score(self.score), self.score),
        )

    def copy_with(
        self,
        position: int | EllipsisType = ...,
        user: User | EllipsisType = ...,
        score: int | EllipsisType = ...,
    ) -> GameHighScore:
        """Replaces some of model's fields with provided ones"""
        return GameHighScore(
            position=position if position is not ... else self.position,
            user=user if user is not ... else self.user,
            score=score if score is not ... else self.score,
        )


ChatMember: TypeAlias = (
    ChatMemberOwner
    | ChatMemberAdministrator
    | ChatMemberMember
    | ChatMemberRestricted
    | ChatMemberLeft
    | ChatMemberBanned
)
"""This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:
- ChatMemberOwner
- ChatMemberAdministrator
- ChatMemberMember
- ChatMemberRestricted
- ChatMemberLeft
- ChatMemberBanned"""
BotCommandScope: TypeAlias = (
    BotCommandScopeDefault
    | BotCommandScopeAllPrivateChats
    | BotCommandScopeAllGroupChats
    | BotCommandScopeAllChatAdministrators
    | BotCommandScopeChat
    | BotCommandScopeChatAdministrators
    | BotCommandScopeChatMember
)
"""This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
- BotCommandScopeDefault
- BotCommandScopeAllPrivateChats
- BotCommandScopeAllGroupChats
- BotCommandScopeAllChatAdministrators
- BotCommandScopeChat
- BotCommandScopeChatAdministrators
- BotCommandScopeChatMember"""
MenuButton: TypeAlias = MenuButtonCommands | MenuButtonWebApp | MenuButtonDefault
"""This object describes the bot's menu button in a private chat. It should be one of
- MenuButtonCommands
- MenuButtonWebApp
- MenuButtonDefault
If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands."""
InputMedia: TypeAlias = (
    InputMediaAnimation
    | InputMediaDocument
    | InputMediaAudio
    | InputMediaPhoto
    | InputMediaVideo
)
"""This object represents the content of a media message to be sent. It should be one of
- InputMediaAnimation
- InputMediaDocument
- InputMediaAudio
- InputMediaPhoto
- InputMediaVideo"""
InlineQueryResult: TypeAlias = (
    InlineQueryResultCachedAudio
    | InlineQueryResultCachedDocument
    | InlineQueryResultCachedGif
    | InlineQueryResultCachedMpeg4Gif
    | InlineQueryResultCachedPhoto
    | InlineQueryResultCachedSticker
    | InlineQueryResultCachedVideo
    | InlineQueryResultCachedVoice
    | InlineQueryResultArticle
    | InlineQueryResultAudio
    | InlineQueryResultContact
    | InlineQueryResultGame
    | InlineQueryResultDocument
    | InlineQueryResultGif
    | InlineQueryResultLocation
    | InlineQueryResultMpeg4Gif
    | InlineQueryResultPhoto
    | InlineQueryResultVenue
    | InlineQueryResultVideo
    | InlineQueryResultVoice
)
"""This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:
- InlineQueryResultCachedAudio
- InlineQueryResultCachedDocument
- InlineQueryResultCachedGif
- InlineQueryResultCachedMpeg4Gif
- InlineQueryResultCachedPhoto
- InlineQueryResultCachedSticker
- InlineQueryResultCachedVideo
- InlineQueryResultCachedVoice
- InlineQueryResultArticle
- InlineQueryResultAudio
- InlineQueryResultContact
- InlineQueryResultGame
- InlineQueryResultDocument
- InlineQueryResultGif
- InlineQueryResultLocation
- InlineQueryResultMpeg4Gif
- InlineQueryResultPhoto
- InlineQueryResultVenue
- InlineQueryResultVideo
- InlineQueryResultVoice
Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public."""
InputMessageContent: TypeAlias = (
    InputTextMessageContent
    | InputLocationMessageContent
    | InputVenueMessageContent
    | InputContactMessageContent
    | InputInvoiceMessageContent
)
"""This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:
- InputTextMessageContent
- InputLocationMessageContent
- InputVenueMessageContent
- InputContactMessageContent
- InputInvoiceMessageContent"""
PassportElementError: TypeAlias = (
    PassportElementErrorDataField
    | PassportElementErrorFrontSide
    | PassportElementErrorReverseSide
    | PassportElementErrorSelfie
    | PassportElementErrorFile
    | PassportElementErrorFiles
    | PassportElementErrorTranslationFile
    | PassportElementErrorTranslationFiles
    | PassportElementErrorUnspecified
)
"""This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:
- PassportElementErrorDataField
- PassportElementErrorFrontSide
- PassportElementErrorReverseSide
- PassportElementErrorSelfie
- PassportElementErrorFile
- PassportElementErrorFiles
- PassportElementErrorTranslationFile
- PassportElementErrorTranslationFiles
- PassportElementErrorUnspecified"""
