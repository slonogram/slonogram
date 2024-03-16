from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    giveaway as _giveaway,
    contact as _contact,
    location as _location,
    chat as _chat,
    invoice as _invoice,
    voice as _voice,
    giveaway_winners as _giveaway_winners,
    sticker as _sticker,
    audio as _audio,
    video as _video,
    animation as _animation,
    document as _document,
    venue as _venue,
    poll as _poll,
    dice as _dice,
    story as _story,
    message_origin as _message_origin,
    game as _game,
    link_preview_options as _link_preview_options,
    photo_size as _photo_size,
    video_note as _video_note,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ExternalReplyInfo:
    animation: _animation.Animation
    """ Optional. Message is an animation, information about the animation """
    audio: _audio.Audio
    """ Optional. Message is an audio file, information about the file """
    chat: _chat.Chat
    """ Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel. """
    contact: _contact.Contact
    """ Optional. Message is a shared contact, information about the contact """
    dice: _dice.Dice
    """ Optional. Message is a dice with random value """
    document: _document.Document
    """ Optional. Message is a general file, information about the file """
    game: _game.Game
    """ Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games """
    giveaway: _giveaway.Giveaway
    """ Optional. Message is a scheduled giveaway, information about the giveaway """
    giveaway_winners: _giveaway_winners.GiveawayWinners
    """ Optional. A giveaway with public winners was completed """
    has_media_spoiler: bool
    """ Optional. True, if the message media is covered by a spoiler animation """
    invoice: _invoice.Invoice
    """ Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments """
    link_preview_options: _link_preview_options.LinkPreviewOptions
    """ Optional. Options used for link preview generation for the original message, if it is a text message """
    location: _location.Location
    """ Optional. Message is a shared location, information about the location """
    message_id: int
    """ Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel. """
    origin: _message_origin.MessageOrigin
    """ Origin of the message replied to by the given message """
    photo: list[_photo_size.PhotoSize]
    """ Optional. Message is a photo, available sizes of the photo """
    poll: _poll.Poll
    """ Optional. Message is a native poll, information about the poll """
    sticker: _sticker.Sticker
    """ Optional. Message is a sticker, information about the sticker """
    story: _story.Story
    """ Optional. Message is a forwarded story """
    venue: _venue.Venue
    """ Optional. Message is a venue, information about the venue """
    video: _video.Video
    """ Optional. Message is a video, information about the video """
    video_note: _video_note.VideoNote
    """ Optional. Message is a video note, information about the video message """
    voice: _voice.Voice
    """ Optional. Message is a voice message, information about the file """

    def alter(
        self,
        origin: Omittable[Alterer1[_message_origin.MessageOrigin]] = OMIT,
        animation: Omittable[Alterer1[_animation.Animation]] = OMIT,
        audio: Omittable[Alterer1[_audio.Audio]] = OMIT,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        contact: Omittable[Alterer1[_contact.Contact]] = OMIT,
        dice: Omittable[Alterer1[_dice.Dice]] = OMIT,
        document: Omittable[Alterer1[_document.Document]] = OMIT,
        game: Omittable[Alterer1[_game.Game]] = OMIT,
        giveaway: Omittable[Alterer1[_giveaway.Giveaway]] = OMIT,
        giveaway_winners: Omittable[Alterer1[_giveaway_winners.GiveawayWinners]] = OMIT,
        has_media_spoiler: Omittable[Alterer1[bool]] = OMIT,
        invoice: Omittable[Alterer1[_invoice.Invoice]] = OMIT,
        link_preview_options: Omittable[
            Alterer1[_link_preview_options.LinkPreviewOptions]
        ] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        photo: Omittable[Alterer1[list[_photo_size.PhotoSize]]] = OMIT,
        poll: Omittable[Alterer1[_poll.Poll]] = OMIT,
        sticker: Omittable[Alterer1[_sticker.Sticker]] = OMIT,
        story: Omittable[Alterer1[_story.Story]] = OMIT,
        venue: Omittable[Alterer1[_venue.Venue]] = OMIT,
        video: Omittable[Alterer1[_video.Video]] = OMIT,
        video_note: Omittable[Alterer1[_video_note.VideoNote]] = OMIT,
        voice: Omittable[Alterer1[_voice.Voice]] = OMIT,
    ):
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
