"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    chat as _chat,
    animation as _animation,
    audio as _audio,
    chat_boost_added as _chat_boost_added,
    message_entity as _message_entity,
    chat_shared as _chat_shared,
    contact as _contact,
    dice as _dice,
    document as _document,
    external_reply_info as _external_reply_info,
    forum_topic_closed as _forum_topic_closed,
    forum_topic_created as _forum_topic_created,
    forum_topic_edited as _forum_topic_edited,
    forum_topic_reopened as _forum_topic_reopened,
    message_origin as _message_origin,
    user as _user,
    game as _game,
    general_forum_topic_hidden as _general_forum_topic_hidden,
    general_forum_topic_unhidden as _general_forum_topic_unhidden,
    giveaway as _giveaway,
    giveaway_completed as _giveaway_completed,
    giveaway_created as _giveaway_created,
    giveaway_winners as _giveaway_winners,
    invoice as _invoice,
    link_preview_options as _link_preview_options,
    location as _location,
    message_auto_delete_timer_changed as _message_auto_delete_timer_changed,
    photo_size as _photo_size,
    passport_data as _passport_data,
    poll as _poll,
    proximity_alert_triggered as _proximity_alert_triggered,
    text_quote as _text_quote,
    inline_keyboard_markup as _inline_keyboard_markup,
    story as _story,
    sticker as _sticker,
    successful_payment as _successful_payment,
    users_shared as _users_shared,
    venue as _venue,
    video as _video,
    video_chat_ended as _video_chat_ended,
    video_chat_participants_invited as _video_chat_participants_invited,
    video_chat_scheduled as _video_chat_scheduled,
    video_chat_started as _video_chat_started,
    video_note as _video_note,
    voice as _voice,
    web_app_data as _web_app_data,
    write_access_allowed as _write_access_allowed,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass
from typing import TypeAlias


@dataclass(slots=True)
class InaccessibleMessage:
    """This object describes a message that was deleted or is otherwise
    inaccessible to the bot.  Telegram documentation:
    https://core.telegram.org/bots/api#inaccessiblemessage"""

    chat: _chat.Chat
    """Chat the message belonged to"""
    date: int
    """Always 0. The field can be used to differentiate regular and
    inaccessible messages."""
    message_id: int
    """Unique message identifier inside the chat"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
    ) -> InaccessibleMessage:
        return InaccessibleMessage(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
        )


@dataclass(slots=True)
class Message:
    """This object represents a message.  Telegram documentation:
    https://core.telegram.org/bots/api#message"""

    chat: _chat.Chat
    """Chat the message belongs to"""
    date: int
    """Date the message was sent in Unix time. It is always a positive
    number, representing a valid date."""
    message_id: int
    """Unique message identifier inside this chat"""
    animation: _animation.Animation | None = None
    """Optional. Message is an animation, information about the animation.
    For backward compatibility, when this field is set, the document field
    will also be set"""
    audio: _audio.Audio | None = None
    """Optional. Message is an audio file, information about the file"""
    author_signature: str | None = None
    """Optional. Signature of the post author for messages in channels, or
    the custom title of an anonymous group administrator"""
    boost_added: _chat_boost_added.ChatBoostAdded | None = None
    """Optional. Service message: user boosted the chat"""
    caption: str | None = None
    """Optional. Caption for the animation, audio, document, photo, video or
    voice"""
    caption_entities: tuple[_message_entity.MessageEntity, ...] | None = None
    """Optional. For messages with a caption, special entities like
    usernames, URLs, bot commands, etc. that appear in the caption"""
    channel_chat_created: bool | None = None
    """Optional. Service message: the channel has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a channel when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a channel."""
    chat_shared: _chat_shared.ChatShared | None = None
    """Optional. Service message: a chat was shared with the bot"""
    connected_website: str | None = None
    """Optional. The domain name of the website on which the user has logged
    in. More about Telegram Login: https://core.telegram.org/widgets/login"""
    contact: _contact.Contact | None = None
    """Optional. Message is a shared contact, information about the contact"""
    delete_chat_photo: bool | None = None
    """Optional. Service message: the chat photo was deleted"""
    dice: _dice.Dice | None = None
    """Optional. Message is a dice with random value"""
    document: _document.Document | None = None
    """Optional. Message is a general file, information about the file"""
    edit_date: int | None = None
    """Optional. Date the message was last edited in Unix time"""
    entities: tuple[_message_entity.MessageEntity, ...] | None = None
    """Optional. For text messages, special entities like usernames, URLs,
    bot commands, etc. that appear in the text"""
    external_reply: _external_reply_info.ExternalReplyInfo | None = None
    """Optional. Information about the message that is being replied to,
    which may come from another chat or forum topic"""
    forum_topic_closed: _forum_topic_closed.ForumTopicClosed | None = None
    """Optional. Service message: forum topic closed"""
    forum_topic_created: _forum_topic_created.ForumTopicCreated | None = None
    """Optional. Service message: forum topic created"""
    forum_topic_edited: _forum_topic_edited.ForumTopicEdited | None = None
    """Optional. Service message: forum topic edited"""
    forum_topic_reopened: _forum_topic_reopened.ForumTopicReopened | None = None
    """Optional. Service message: forum topic reopened"""
    forward_origin: _message_origin.MessageOrigin | None = None
    """Optional. Information about the original message for forwarded
    messages"""
    from_: _user.User | None = None
    """Optional. Sender of the message; empty for messages sent to channels.
    For backward compatibility, the field contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""
    game: _game.Game | None = None
    """Optional. Message is a game, information about the game. More about
    games: https://core.telegram.org/bots/api#games"""
    general_forum_topic_hidden: _general_forum_topic_hidden.GeneralForumTopicHidden | None = None
    """Optional. Service message: the 'General' forum topic hidden"""
    general_forum_topic_unhidden: _general_forum_topic_unhidden.GeneralForumTopicUnhidden | None = None
    """Optional. Service message: the 'General' forum topic unhidden"""
    giveaway: _giveaway.Giveaway | None = None
    """Optional. The message is a scheduled giveaway message"""
    giveaway_completed: _giveaway_completed.GiveawayCompleted | None = None
    """Optional. Service message: a giveaway without public winners was
    completed"""
    giveaway_created: _giveaway_created.GiveawayCreated | None = None
    """Optional. Service message: a scheduled giveaway was created"""
    giveaway_winners: _giveaway_winners.GiveawayWinners | None = None
    """Optional. A giveaway with public winners was completed"""
    group_chat_created: bool | None = None
    """Optional. Service message: the group has been created"""
    has_media_spoiler: bool | None = None
    """Optional. True, if the message media is covered by a spoiler animation"""
    has_protected_content: bool | None = None
    """Optional. True, if the message can't be forwarded"""
    invoice: _invoice.Invoice | None = None
    """Optional. Message is an invoice for a payment, information about the
    invoice. More about payments:
    https://core.telegram.org/bots/api#payments"""
    is_automatic_forward: bool | None = None
    """Optional. True, if the message is a channel post that was
    automatically forwarded to the connected discussion group"""
    is_topic_message: bool | None = None
    """Optional. True, if the message is sent to a forum topic"""
    left_chat_member: _user.User | None = None
    """Optional. A member was removed from the group, information about them
    (this member may be the bot itself)"""
    link_preview_options: _link_preview_options.LinkPreviewOptions | None = None
    """Optional. Options used for link preview generation for the message, if
    it is a text message and link preview options were changed"""
    location: _location.Location | None = None
    """Optional. Message is a shared location, information about the location"""
    media_group_id: str | None = None
    """Optional. The unique identifier of a media message group this message
    belongs to"""
    message_auto_delete_timer_changed: _message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged | None = None
    """Optional. Service message: auto-delete timer settings changed in the
    chat"""
    message_thread_id: int | None = None
    """Optional. Unique identifier of a message thread to which the message
    belongs; for supergroups only"""
    migrate_from_chat_id: int | None = None
    """Optional. The supergroup has been migrated from a group with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""
    migrate_to_chat_id: int | None = None
    """Optional. The group has been migrated to a supergroup with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""
    new_chat_members: tuple[_user.User, ...] | None = None
    """Optional. New members that were added to the group or supergroup and
    information about them (the bot itself may be one of these members)"""
    new_chat_photo: tuple[_photo_size.PhotoSize, ...] | None = None
    """Optional. A chat photo was change to this value"""
    new_chat_title: str | None = None
    """Optional. A chat title was changed to this value"""
    passport_data: _passport_data.PassportData | None = None
    """Optional. Telegram Passport data"""
    photo: tuple[_photo_size.PhotoSize, ...] | None = None
    """Optional. Message is a photo, available sizes of the photo"""
    pinned_message: MaybeInaccessibleMessage | None = None
    """Optional. Specified message was pinned. Note that the Message object
    in this field will not contain further reply_to_message fields even if
    it itself is a reply."""
    poll: _poll.Poll | None = None
    """Optional. Message is a native poll, information about the poll"""
    proximity_alert_triggered: _proximity_alert_triggered.ProximityAlertTriggered | None = None
    """Optional. Service message. A user in the chat triggered another user's
    proximity alert while sharing Live Location."""
    quote: _text_quote.TextQuote | None = None
    """Optional. For replies that quote part of the original message, the
    quoted part of the message"""
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup | None = None
    """Optional. Inline keyboard attached to the message. login_url buttons
    are represented as ordinary url buttons."""
    reply_to_message: Message | None = None
    """Optional. For replies in the same chat and message thread, the
    original message. Note that the Message object in this field will not
    contain further reply_to_message fields even if it itself is a reply."""
    reply_to_story: _story.Story | None = None
    """Optional. For replies to a story, the original story"""
    sender_boost_count: int | None = None
    """Optional. If the sender of the message boosted the chat, the number of
    boosts added by the user"""
    sender_chat: _chat.Chat | None = None
    """Optional. Sender of the message, sent on behalf of a chat. For
    example, the channel itself for channel posts, the supergroup itself
    for messages from anonymous group administrators, the linked channel
    for messages automatically forwarded to the discussion group. For
    backward compatibility, the field from contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""
    sticker: _sticker.Sticker | None = None
    """Optional. Message is a sticker, information about the sticker"""
    story: _story.Story | None = None
    """Optional. Message is a forwarded story"""
    successful_payment: _successful_payment.SuccessfulPayment | None = None
    """Optional. Message is a service message about a successful payment,
    information about the payment. More about payments:
    https://core.telegram.org/bots/api#payments"""
    supergroup_chat_created: bool | None = None
    """Optional. Service message: the supergroup has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a supergroup when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a directly created supergroup."""
    text: str | None = None
    """Optional. For text messages, the actual UTF-8 text of the message"""
    users_shared: _users_shared.UsersShared | None = None
    """Optional. Service message: users were shared with the bot"""
    venue: _venue.Venue | None = None
    """Optional. Message is a venue, information about the venue. For
    backward compatibility, when this field is set, the location field
    will also be set"""
    via_bot: _user.User | None = None
    """Optional. Bot through which the message was sent"""
    video: _video.Video | None = None
    """Optional. Message is a video, information about the video"""
    video_chat_ended: _video_chat_ended.VideoChatEnded | None = None
    """Optional. Service message: video chat ended"""
    video_chat_participants_invited: _video_chat_participants_invited.VideoChatParticipantsInvited | None = None
    """Optional. Service message: new participants invited to a video chat"""
    video_chat_scheduled: _video_chat_scheduled.VideoChatScheduled | None = None
    """Optional. Service message: video chat scheduled"""
    video_chat_started: _video_chat_started.VideoChatStarted | None = None
    """Optional. Service message: video chat started"""
    video_note: _video_note.VideoNote | None = None
    """Optional. Message is a video note, information about the video message"""
    voice: _voice.Voice | None = None
    """Optional. Message is a voice message, information about the file"""
    web_app_data: _web_app_data.WebAppData | None = None
    """Optional. Service message: data sent by a Web App"""
    write_access_allowed: _write_access_allowed.WriteAccessAllowed | None = None
    """Optional. Service message: the user allowed the bot to write messages
    after adding it to the attachment or side menu, launching a Web App
    from a link, or accepting an explicit request from a Web App sent by
    the method requestWriteAccess"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        animation: Omittable[Alterer1[_animation.Animation | None]] = OMIT,
        audio: Omittable[Alterer1[_audio.Audio | None]] = OMIT,
        author_signature: Omittable[Alterer1[str | None]] = OMIT,
        boost_added: Omittable[
            Alterer1[_chat_boost_added.ChatBoostAdded | None]
        ] = OMIT,
        caption: Omittable[Alterer1[str | None]] = OMIT,
        caption_entities: Omittable[
            Alterer1[tuple[_message_entity.MessageEntity, ...] | None]
        ] = OMIT,
        channel_chat_created: Omittable[Alterer1[bool | None]] = OMIT,
        chat_shared: Omittable[Alterer1[_chat_shared.ChatShared | None]] = OMIT,
        connected_website: Omittable[Alterer1[str | None]] = OMIT,
        contact: Omittable[Alterer1[_contact.Contact | None]] = OMIT,
        delete_chat_photo: Omittable[Alterer1[bool | None]] = OMIT,
        dice: Omittable[Alterer1[_dice.Dice | None]] = OMIT,
        document: Omittable[Alterer1[_document.Document | None]] = OMIT,
        edit_date: Omittable[Alterer1[int | None]] = OMIT,
        entities: Omittable[
            Alterer1[tuple[_message_entity.MessageEntity, ...] | None]
        ] = OMIT,
        external_reply: Omittable[
            Alterer1[_external_reply_info.ExternalReplyInfo | None]
        ] = OMIT,
        forum_topic_closed: Omittable[
            Alterer1[_forum_topic_closed.ForumTopicClosed | None]
        ] = OMIT,
        forum_topic_created: Omittable[
            Alterer1[_forum_topic_created.ForumTopicCreated | None]
        ] = OMIT,
        forum_topic_edited: Omittable[
            Alterer1[_forum_topic_edited.ForumTopicEdited | None]
        ] = OMIT,
        forum_topic_reopened: Omittable[
            Alterer1[_forum_topic_reopened.ForumTopicReopened | None]
        ] = OMIT,
        forward_origin: Omittable[
            Alterer1[_message_origin.MessageOrigin | None]
        ] = OMIT,
        from_: Omittable[Alterer1[_user.User | None]] = OMIT,
        game: Omittable[Alterer1[_game.Game | None]] = OMIT,
        general_forum_topic_hidden: Omittable[
            Alterer1[_general_forum_topic_hidden.GeneralForumTopicHidden | None]
        ] = OMIT,
        general_forum_topic_unhidden: Omittable[
            Alterer1[_general_forum_topic_unhidden.GeneralForumTopicUnhidden | None]
        ] = OMIT,
        giveaway: Omittable[Alterer1[_giveaway.Giveaway | None]] = OMIT,
        giveaway_completed: Omittable[
            Alterer1[_giveaway_completed.GiveawayCompleted | None]
        ] = OMIT,
        giveaway_created: Omittable[
            Alterer1[_giveaway_created.GiveawayCreated | None]
        ] = OMIT,
        giveaway_winners: Omittable[
            Alterer1[_giveaway_winners.GiveawayWinners | None]
        ] = OMIT,
        group_chat_created: Omittable[Alterer1[bool | None]] = OMIT,
        has_media_spoiler: Omittable[Alterer1[bool | None]] = OMIT,
        has_protected_content: Omittable[Alterer1[bool | None]] = OMIT,
        invoice: Omittable[Alterer1[_invoice.Invoice | None]] = OMIT,
        is_automatic_forward: Omittable[Alterer1[bool | None]] = OMIT,
        is_topic_message: Omittable[Alterer1[bool | None]] = OMIT,
        left_chat_member: Omittable[Alterer1[_user.User | None]] = OMIT,
        link_preview_options: Omittable[
            Alterer1[_link_preview_options.LinkPreviewOptions | None]
        ] = OMIT,
        location: Omittable[Alterer1[_location.Location | None]] = OMIT,
        media_group_id: Omittable[Alterer1[str | None]] = OMIT,
        message_auto_delete_timer_changed: Omittable[
            Alterer1[
                _message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged | None
            ]
        ] = OMIT,
        message_thread_id: Omittable[Alterer1[int | None]] = OMIT,
        migrate_from_chat_id: Omittable[Alterer1[int | None]] = OMIT,
        migrate_to_chat_id: Omittable[Alterer1[int | None]] = OMIT,
        new_chat_members: Omittable[Alterer1[tuple[_user.User, ...] | None]] = OMIT,
        new_chat_photo: Omittable[
            Alterer1[tuple[_photo_size.PhotoSize, ...] | None]
        ] = OMIT,
        new_chat_title: Omittable[Alterer1[str | None]] = OMIT,
        passport_data: Omittable[Alterer1[_passport_data.PassportData | None]] = OMIT,
        photo: Omittable[Alterer1[tuple[_photo_size.PhotoSize, ...] | None]] = OMIT,
        pinned_message: Omittable[Alterer1[MaybeInaccessibleMessage | None]] = OMIT,
        poll: Omittable[Alterer1[_poll.Poll | None]] = OMIT,
        proximity_alert_triggered: Omittable[
            Alterer1[_proximity_alert_triggered.ProximityAlertTriggered | None]
        ] = OMIT,
        quote: Omittable[Alterer1[_text_quote.TextQuote | None]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup | None]
        ] = OMIT,
        reply_to_message: Omittable[Alterer1[Message | None]] = OMIT,
        reply_to_story: Omittable[Alterer1[_story.Story | None]] = OMIT,
        sender_boost_count: Omittable[Alterer1[int | None]] = OMIT,
        sender_chat: Omittable[Alterer1[_chat.Chat | None]] = OMIT,
        sticker: Omittable[Alterer1[_sticker.Sticker | None]] = OMIT,
        story: Omittable[Alterer1[_story.Story | None]] = OMIT,
        successful_payment: Omittable[
            Alterer1[_successful_payment.SuccessfulPayment | None]
        ] = OMIT,
        supergroup_chat_created: Omittable[Alterer1[bool | None]] = OMIT,
        text: Omittable[Alterer1[str | None]] = OMIT,
        users_shared: Omittable[Alterer1[_users_shared.UsersShared | None]] = OMIT,
        venue: Omittable[Alterer1[_venue.Venue | None]] = OMIT,
        via_bot: Omittable[Alterer1[_user.User | None]] = OMIT,
        video: Omittable[Alterer1[_video.Video | None]] = OMIT,
        video_chat_ended: Omittable[
            Alterer1[_video_chat_ended.VideoChatEnded | None]
        ] = OMIT,
        video_chat_participants_invited: Omittable[
            Alterer1[
                _video_chat_participants_invited.VideoChatParticipantsInvited | None
            ]
        ] = OMIT,
        video_chat_scheduled: Omittable[
            Alterer1[_video_chat_scheduled.VideoChatScheduled | None]
        ] = OMIT,
        video_chat_started: Omittable[
            Alterer1[_video_chat_started.VideoChatStarted | None]
        ] = OMIT,
        video_note: Omittable[Alterer1[_video_note.VideoNote | None]] = OMIT,
        voice: Omittable[Alterer1[_voice.Voice | None]] = OMIT,
        web_app_data: Omittable[Alterer1[_web_app_data.WebAppData | None]] = OMIT,
        write_access_allowed: Omittable[
            Alterer1[_write_access_allowed.WriteAccessAllowed | None]
        ] = OMIT,
    ) -> Message:
        return Message(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            animation=alter1(animation, self.animation),
            audio=alter1(audio, self.audio),
            author_signature=alter1(author_signature, self.author_signature),
            boost_added=alter1(boost_added, self.boost_added),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            channel_chat_created=alter1(
                channel_chat_created, self.channel_chat_created
            ),
            chat_shared=alter1(chat_shared, self.chat_shared),
            connected_website=alter1(connected_website, self.connected_website),
            contact=alter1(contact, self.contact),
            delete_chat_photo=alter1(delete_chat_photo, self.delete_chat_photo),
            dice=alter1(dice, self.dice),
            document=alter1(document, self.document),
            edit_date=alter1(edit_date, self.edit_date),
            entities=alter1(entities, self.entities),
            external_reply=alter1(external_reply, self.external_reply),
            forum_topic_closed=alter1(forum_topic_closed, self.forum_topic_closed),
            forum_topic_created=alter1(forum_topic_created, self.forum_topic_created),
            forum_topic_edited=alter1(forum_topic_edited, self.forum_topic_edited),
            forum_topic_reopened=alter1(
                forum_topic_reopened, self.forum_topic_reopened
            ),
            forward_origin=alter1(forward_origin, self.forward_origin),
            from_=alter1(from_, self.from_),
            game=alter1(game, self.game),
            general_forum_topic_hidden=alter1(
                general_forum_topic_hidden, self.general_forum_topic_hidden
            ),
            general_forum_topic_unhidden=alter1(
                general_forum_topic_unhidden, self.general_forum_topic_unhidden
            ),
            giveaway=alter1(giveaway, self.giveaway),
            giveaway_completed=alter1(giveaway_completed, self.giveaway_completed),
            giveaway_created=alter1(giveaway_created, self.giveaway_created),
            giveaway_winners=alter1(giveaway_winners, self.giveaway_winners),
            group_chat_created=alter1(group_chat_created, self.group_chat_created),
            has_media_spoiler=alter1(has_media_spoiler, self.has_media_spoiler),
            has_protected_content=alter1(
                has_protected_content, self.has_protected_content
            ),
            invoice=alter1(invoice, self.invoice),
            is_automatic_forward=alter1(
                is_automatic_forward, self.is_automatic_forward
            ),
            is_topic_message=alter1(is_topic_message, self.is_topic_message),
            left_chat_member=alter1(left_chat_member, self.left_chat_member),
            link_preview_options=alter1(
                link_preview_options, self.link_preview_options
            ),
            location=alter1(location, self.location),
            media_group_id=alter1(media_group_id, self.media_group_id),
            message_auto_delete_timer_changed=alter1(
                message_auto_delete_timer_changed,
                self.message_auto_delete_timer_changed,
            ),
            message_thread_id=alter1(message_thread_id, self.message_thread_id),
            migrate_from_chat_id=alter1(
                migrate_from_chat_id, self.migrate_from_chat_id
            ),
            migrate_to_chat_id=alter1(migrate_to_chat_id, self.migrate_to_chat_id),
            new_chat_members=alter1(new_chat_members, self.new_chat_members),
            new_chat_photo=alter1(new_chat_photo, self.new_chat_photo),
            new_chat_title=alter1(new_chat_title, self.new_chat_title),
            passport_data=alter1(passport_data, self.passport_data),
            photo=alter1(photo, self.photo),
            pinned_message=alter1(pinned_message, self.pinned_message),
            poll=alter1(poll, self.poll),
            proximity_alert_triggered=alter1(
                proximity_alert_triggered, self.proximity_alert_triggered
            ),
            quote=alter1(quote, self.quote),
            reply_markup=alter1(reply_markup, self.reply_markup),
            reply_to_message=alter1(reply_to_message, self.reply_to_message),
            reply_to_story=alter1(reply_to_story, self.reply_to_story),
            sender_boost_count=alter1(sender_boost_count, self.sender_boost_count),
            sender_chat=alter1(sender_chat, self.sender_chat),
            sticker=alter1(sticker, self.sticker),
            story=alter1(story, self.story),
            successful_payment=alter1(successful_payment, self.successful_payment),
            supergroup_chat_created=alter1(
                supergroup_chat_created, self.supergroup_chat_created
            ),
            text=alter1(text, self.text),
            users_shared=alter1(users_shared, self.users_shared),
            venue=alter1(venue, self.venue),
            via_bot=alter1(via_bot, self.via_bot),
            video=alter1(video, self.video),
            video_chat_ended=alter1(video_chat_ended, self.video_chat_ended),
            video_chat_participants_invited=alter1(
                video_chat_participants_invited, self.video_chat_participants_invited
            ),
            video_chat_scheduled=alter1(
                video_chat_scheduled, self.video_chat_scheduled
            ),
            video_chat_started=alter1(video_chat_started, self.video_chat_started),
            video_note=alter1(video_note, self.video_note),
            voice=alter1(voice, self.voice),
            web_app_data=alter1(web_app_data, self.web_app_data),
            write_access_allowed=alter1(
                write_access_allowed, self.write_access_allowed
            ),
        )


MaybeInaccessibleMessage: TypeAlias = Message | InaccessibleMessage
""" This object describes a message that can be inaccessible to the bot. It can be one of
- Message
- InaccessibleMessage

Telegram documentation: https://core.telegram.org/bots/api#maybeinaccessiblemessage """
__all__ = ["InaccessibleMessage", "MaybeInaccessibleMessage", "Message"]
