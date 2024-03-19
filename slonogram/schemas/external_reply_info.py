"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import (
    message_origin as _message_origin,
    animation as _animation,
    audio as _audio,
    chat as _chat,
    contact as _contact,
    dice as _dice,
    document as _document,
    game as _game,
    giveaway as _giveaway,
    giveaway_winners as _giveaway_winners,
    invoice as _invoice,
    link_preview_options as _link_preview_options,
    location as _location,
    photo_size as _photo_size,
    poll as _poll,
    sticker as _sticker,
    story as _story,
    venue as _venue,
    video as _video,
    video_note as _video_note,
    voice as _voice,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ExternalReplyInfo:
    """This object contains information about a message that is being replied
    to, which may come from another chat or forum topic.  Telegram
    documentation: https://core.telegram.org/bots/api#externalreplyinfo"""

    origin: _message_origin.MessageOrigin
    """Origin of the message replied to by the given message"""
    animation: _animation.Animation | None = None
    """Optional. Message is an animation, information about the animation"""
    audio: _audio.Audio | None = None
    """Optional. Message is an audio file, information about the file"""
    chat: _chat.Chat | None = None
    """Optional. Chat the original message belongs to. Available only if the
    chat is a supergroup or a channel."""
    contact: _contact.Contact | None = None
    """Optional. Message is a shared contact, information about the contact"""
    dice: _dice.Dice | None = None
    """Optional. Message is a dice with random value"""
    document: _document.Document | None = None
    """Optional. Message is a general file, information about the file"""
    game: _game.Game | None = None
    """Optional. Message is a game, information about the game. More about
    games: https://core.telegram.org/bots/api#games"""
    giveaway: _giveaway.Giveaway | None = None
    """Optional. Message is a scheduled giveaway, information about the
    giveaway"""
    giveaway_winners: _giveaway_winners.GiveawayWinners | None = None
    """Optional. A giveaway with public winners was completed"""
    has_media_spoiler: bool | None = None
    """Optional. True, if the message media is covered by a spoiler animation"""
    invoice: _invoice.Invoice | None = None
    """Optional. Message is an invoice for a payment, information about the
    invoice. More about payments:
    https://core.telegram.org/bots/api#payments"""
    link_preview_options: _link_preview_options.LinkPreviewOptions | None = None
    """Optional. Options used for link preview generation for the original
    message, if it is a text message"""
    location: _location.Location | None = None
    """Optional. Message is a shared location, information about the location"""
    message_id: int | None = None
    """Optional. Unique message identifier inside the original chat.
    Available only if the original chat is a supergroup or a channel."""
    photo: tuple[_photo_size.PhotoSize, ...] | None = None
    """Optional. Message is a photo, available sizes of the photo"""
    poll: _poll.Poll | None = None
    """Optional. Message is a native poll, information about the poll"""
    sticker: _sticker.Sticker | None = None
    """Optional. Message is a sticker, information about the sticker"""
    story: _story.Story | None = None
    """Optional. Message is a forwarded story"""
    venue: _venue.Venue | None = None
    """Optional. Message is a venue, information about the venue"""
    video: _video.Video | None = None
    """Optional. Message is a video, information about the video"""
    video_note: _video_note.VideoNote | None = None
    """Optional. Message is a video note, information about the video message"""
    voice: _voice.Voice | None = None
    """Optional. Message is a voice message, information about the file"""

    def alter(
        self,
        origin: Omittable[Alterer1[_message_origin.MessageOrigin]] = OMIT,
        animation: Omittable[Alterer1[_animation.Animation | None]] = OMIT,
        audio: Omittable[Alterer1[_audio.Audio | None]] = OMIT,
        chat: Omittable[Alterer1[_chat.Chat | None]] = OMIT,
        contact: Omittable[Alterer1[_contact.Contact | None]] = OMIT,
        dice: Omittable[Alterer1[_dice.Dice | None]] = OMIT,
        document: Omittable[Alterer1[_document.Document | None]] = OMIT,
        game: Omittable[Alterer1[_game.Game | None]] = OMIT,
        giveaway: Omittable[Alterer1[_giveaway.Giveaway | None]] = OMIT,
        giveaway_winners: Omittable[
            Alterer1[_giveaway_winners.GiveawayWinners | None]
        ] = OMIT,
        has_media_spoiler: Omittable[Alterer1[bool | None]] = OMIT,
        invoice: Omittable[Alterer1[_invoice.Invoice | None]] = OMIT,
        link_preview_options: Omittable[
            Alterer1[_link_preview_options.LinkPreviewOptions | None]
        ] = OMIT,
        location: Omittable[Alterer1[_location.Location | None]] = OMIT,
        message_id: Omittable[Alterer1[int | None]] = OMIT,
        photo: Omittable[Alterer1[tuple[_photo_size.PhotoSize, ...] | None]] = OMIT,
        poll: Omittable[Alterer1[_poll.Poll | None]] = OMIT,
        sticker: Omittable[Alterer1[_sticker.Sticker | None]] = OMIT,
        story: Omittable[Alterer1[_story.Story | None]] = OMIT,
        venue: Omittable[Alterer1[_venue.Venue | None]] = OMIT,
        video: Omittable[Alterer1[_video.Video | None]] = OMIT,
        video_note: Omittable[Alterer1[_video_note.VideoNote | None]] = OMIT,
        voice: Omittable[Alterer1[_voice.Voice | None]] = OMIT,
    ) -> ExternalReplyInfo:
        return ExternalReplyInfo(
            origin=alter1(origin, self.origin),
            animation=alter1(animation, self.animation),
            audio=alter1(audio, self.audio),
            chat=alter1(chat, self.chat),
            contact=alter1(contact, self.contact),
            dice=alter1(dice, self.dice),
            document=alter1(document, self.document),
            game=alter1(game, self.game),
            giveaway=alter1(giveaway, self.giveaway),
            giveaway_winners=alter1(giveaway_winners, self.giveaway_winners),
            has_media_spoiler=alter1(has_media_spoiler, self.has_media_spoiler),
            invoice=alter1(invoice, self.invoice),
            link_preview_options=alter1(
                link_preview_options, self.link_preview_options
            ),
            location=alter1(location, self.location),
            message_id=alter1(message_id, self.message_id),
            photo=alter1(photo, self.photo),
            poll=alter1(poll, self.poll),
            sticker=alter1(sticker, self.sticker),
            story=alter1(story, self.story),
            venue=alter1(venue, self.venue),
            video=alter1(video, self.video),
            video_note=alter1(video_note, self.video_note),
            voice=alter1(voice, self.voice),
        )


__all__ = ["ExternalReplyInfo"]
