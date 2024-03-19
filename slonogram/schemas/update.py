"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    callback_query as _callback_query,
    maybe_inaccessible_message as _maybe_inaccessible_message,
    chat_boost_updated as _chat_boost_updated,
    chat_join_request as _chat_join_request,
    chat_member_updated as _chat_member_updated,
    chosen_inline_result as _chosen_inline_result,
    inline_query as _inline_query,
    message_reaction_updated as _message_reaction_updated,
    message_reaction_count_updated as _message_reaction_count_updated,
    poll as _poll,
    poll_answer as _poll_answer,
    pre_checkout_query as _pre_checkout_query,
    chat_boost_removed as _chat_boost_removed,
    shipping_query as _shipping_query,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class Update:
    """This object represents an incoming update. At most one of the optional
    parameters can be present in any given update.  Telegram
    documentation: https://core.telegram.org/bots/api#update"""

    update_id: int
    """The update's unique identifier. Update identifiers start from a
    certain positive number and increase sequentially. This identifier
    becomes especially handy if you're using webhooks, since it allows you
    to ignore repeated updates or to restore the correct update sequence,
    should they get out of order. If there are no new updates for at least
    a week, then identifier of the next update will be chosen randomly
    instead of sequentially."""
    callback_query: _callback_query.CallbackQuery | None = None
    """Optional. New incoming callback query"""
    channel_post: _maybe_inaccessible_message.Message | None = None
    """Optional. New incoming channel post of any kind - text, photo,
    sticker, etc."""
    chat_boost: _chat_boost_updated.ChatBoostUpdated | None = None
    """Optional. A chat boost was added or changed. The bot must be an
    administrator in the chat to receive these updates."""
    chat_join_request: _chat_join_request.ChatJoinRequest | None = None
    """Optional. A request to join the chat has been sent. The bot must have
    the can_invite_users administrator right in the chat to receive these
    updates."""
    chat_member: _chat_member_updated.ChatMemberUpdated | None = None
    """Optional. A chat member's status was updated in a chat. The bot must
    be an administrator in the chat and must explicitly specify
    "chat_member" in the list of allowed_updates to receive these updates."""
    chosen_inline_result: _chosen_inline_result.ChosenInlineResult | None = None
    """Optional. The result of an inline query that was chosen by a user and
    sent to their chat partner. Please see our documentation on the
    feedback collecting for details on how to enable these updates for
    your bot."""
    edited_channel_post: _maybe_inaccessible_message.Message | None = None
    """Optional. New version of a channel post that is known to the bot and
    was edited. This update may at times be triggered by changes to
    message fields that are either unavailable or not actively used by
    your bot."""
    edited_message: _maybe_inaccessible_message.Message | None = None
    """Optional. New version of a message that is known to the bot and was
    edited. This update may at times be triggered by changes to message
    fields that are either unavailable or not actively used by your bot."""
    inline_query: _inline_query.InlineQuery | None = None
    """Optional. New incoming inline query"""
    message: _maybe_inaccessible_message.Message | None = None
    """Optional. New incoming message of any kind - text, photo, sticker,
    etc."""
    message_reaction: _message_reaction_updated.MessageReactionUpdated | None = None
    """Optional. A reaction to a message was changed by a user. The bot must
    be an administrator in the chat and must explicitly specify
    "message_reaction" in the list of allowed_updates to receive these
    updates. The update isn't received for reactions set by bots."""
    message_reaction_count: _message_reaction_count_updated.MessageReactionCountUpdated | None = None
    """Optional. Reactions to a message with anonymous reactions were
    changed. The bot must be an administrator in the chat and must
    explicitly specify "message_reaction_count" in the list of
    allowed_updates to receive these updates. The updates are grouped and
    can be sent with delay up to a few minutes."""
    my_chat_member: _chat_member_updated.ChatMemberUpdated | None = None
    """Optional. The bot's chat member status was updated in a chat. For
    private chats, this update is received only when the bot is blocked or
    unblocked by the user."""
    poll: _poll.Poll | None = None
    """Optional. New poll state. Bots receive only updates about manually
    stopped polls and polls, which are sent by the bot"""
    poll_answer: _poll_answer.PollAnswer | None = None
    """Optional. A user changed their answer in a non-anonymous poll. Bots
    receive new votes only in polls that were sent by the bot itself."""
    pre_checkout_query: _pre_checkout_query.PreCheckoutQuery | None = None
    """Optional. New incoming pre-checkout query. Contains full information
    about checkout"""
    removed_chat_boost: _chat_boost_removed.ChatBoostRemoved | None = None
    """Optional. A boost was removed from a chat. The bot must be an
    administrator in the chat to receive these updates."""
    shipping_query: _shipping_query.ShippingQuery | None = None
    """Optional. New incoming shipping query. Only for invoices with flexible
    price"""

    def alter(
        self,
        update_id: Omittable[Alterer1[int]] = OMIT,
        callback_query: Omittable[
            Alterer1[_callback_query.CallbackQuery | None]
        ] = OMIT,
        channel_post: Omittable[
            Alterer1[_maybe_inaccessible_message.Message | None]
        ] = OMIT,
        chat_boost: Omittable[
            Alterer1[_chat_boost_updated.ChatBoostUpdated | None]
        ] = OMIT,
        chat_join_request: Omittable[
            Alterer1[_chat_join_request.ChatJoinRequest | None]
        ] = OMIT,
        chat_member: Omittable[
            Alterer1[_chat_member_updated.ChatMemberUpdated | None]
        ] = OMIT,
        chosen_inline_result: Omittable[
            Alterer1[_chosen_inline_result.ChosenInlineResult | None]
        ] = OMIT,
        edited_channel_post: Omittable[
            Alterer1[_maybe_inaccessible_message.Message | None]
        ] = OMIT,
        edited_message: Omittable[
            Alterer1[_maybe_inaccessible_message.Message | None]
        ] = OMIT,
        inline_query: Omittable[Alterer1[_inline_query.InlineQuery | None]] = OMIT,
        message: Omittable[Alterer1[_maybe_inaccessible_message.Message | None]] = OMIT,
        message_reaction: Omittable[
            Alterer1[_message_reaction_updated.MessageReactionUpdated | None]
        ] = OMIT,
        message_reaction_count: Omittable[
            Alterer1[_message_reaction_count_updated.MessageReactionCountUpdated | None]
        ] = OMIT,
        my_chat_member: Omittable[
            Alterer1[_chat_member_updated.ChatMemberUpdated | None]
        ] = OMIT,
        poll: Omittable[Alterer1[_poll.Poll | None]] = OMIT,
        poll_answer: Omittable[Alterer1[_poll_answer.PollAnswer | None]] = OMIT,
        pre_checkout_query: Omittable[
            Alterer1[_pre_checkout_query.PreCheckoutQuery | None]
        ] = OMIT,
        removed_chat_boost: Omittable[
            Alterer1[_chat_boost_removed.ChatBoostRemoved | None]
        ] = OMIT,
        shipping_query: Omittable[
            Alterer1[_shipping_query.ShippingQuery | None]
        ] = OMIT,
    ) -> Update:
        return Update(
            update_id=alter1(update_id, self.update_id),
            callback_query=alter1(callback_query, self.callback_query),
            channel_post=alter1(channel_post, self.channel_post),
            chat_boost=alter1(chat_boost, self.chat_boost),
            chat_join_request=alter1(chat_join_request, self.chat_join_request),
            chat_member=alter1(chat_member, self.chat_member),
            chosen_inline_result=alter1(
                chosen_inline_result, self.chosen_inline_result
            ),
            edited_channel_post=alter1(edited_channel_post, self.edited_channel_post),
            edited_message=alter1(edited_message, self.edited_message),
            inline_query=alter1(inline_query, self.inline_query),
            message=alter1(message, self.message),
            message_reaction=alter1(message_reaction, self.message_reaction),
            message_reaction_count=alter1(
                message_reaction_count, self.message_reaction_count
            ),
            my_chat_member=alter1(my_chat_member, self.my_chat_member),
            poll=alter1(poll, self.poll),
            poll_answer=alter1(poll_answer, self.poll_answer),
            pre_checkout_query=alter1(pre_checkout_query, self.pre_checkout_query),
            removed_chat_boost=alter1(removed_chat_boost, self.removed_chat_boost),
            shipping_query=alter1(shipping_query, self.shipping_query),
        )


__all__ = ["Update"]
