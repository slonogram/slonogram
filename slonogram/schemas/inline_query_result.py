from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    input_message_content as _input_message_content,
    message_entity as _message_entity,
    inline_keyboard_markup as _inline_keyboard_markup,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class InlineQueryResultArticle:
    """Represents a link to an article or web page.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultarticle"""

    description: str
    """ Optional. Short description of the result """
    hide_url: bool
    """ Optional. Pass True if you don't want the URL to be shown in the message """
    id: str
    """ Unique identifier for this result, 1-64 Bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Content of the message to be sent """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_height: int
    """ Optional. Thumbnail height """
    thumbnail_url: str
    """ Optional. Url of the thumbnail for the result """
    thumbnail_width: int
    """ Optional. Thumbnail width """
    title: str
    """ Title of the result """
    type: str
    """ Type of the result, must be article """
    url: str
    """ Optional. URL of the result """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        hide_url: Omittable[Alterer1[bool]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_height: Omittable[Alterer1[int]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_width: Omittable[Alterer1[int]] = OMIT,
        url: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultArticle:
        return InlineQueryResultArticle(
            id=alter1(id, self.id),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            description=alter1(description, self.description),
            hide_url=alter1(hide_url, self.hide_url),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_height=alter1(thumbnail_height, self.thumbnail_height),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            thumbnail_width=alter1(thumbnail_width, self.thumbnail_width),
            url=alter1(url, self.url),
        )


@model
class InlineQueryResultAudio:
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultaudio"""

    audio_duration: int
    """ Optional. Audio duration in seconds """
    audio_url: str
    """ A valid URL for the audio file """
    caption: str
    """ Optional. Caption, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the audio """
    parse_mode: str
    """ Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    performer: str
    """ Optional. Performer """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Title """
    type: str
    """ Type of the result, must be audio """

    def alter(
        self,
        audio_url: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        audio_duration: Omittable[Alterer1[int]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        performer: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultAudio:
        return InlineQueryResultAudio(
            audio_url=alter1(audio_url, self.audio_url),
            id=alter1(id, self.id),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            audio_duration=alter1(audio_duration, self.audio_duration),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            performer=alter1(performer, self.performer),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultCachedAudio:
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedaudio"""

    audio_file_id: str
    """ A valid file identifier for the audio file """
    caption: str
    """ Optional. Caption, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the audio """
    parse_mode: str
    """ Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    type: str
    """ Type of the result, must be audio """

    def alter(
        self,
        audio_file_id: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultCachedAudio:
        return InlineQueryResultCachedAudio(
            audio_file_id=alter1(audio_file_id, self.audio_file_id),
            id=alter1(id, self.id),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultCachedDocument:
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcacheddocument"""

    caption: str
    """ Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    document_file_id: str
    """ A valid file identifier for the file """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the file """
    parse_mode: str
    """ Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Title for the result """
    type: str
    """ Type of the result, must be document """

    def alter(
        self,
        document_file_id: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultCachedDocument:
        return InlineQueryResultCachedDocument(
            document_file_id=alter1(document_file_id, self.document_file_id),
            id=alter1(id, self.id),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultCachedGif:
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedgif"""

    caption: str
    """ Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    gif_file_id: str
    """ A valid file identifier for the GIF file """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the GIF animation """
    parse_mode: str
    """ Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be gif """

    def alter(
        self,
        gif_file_id: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultCachedGif:
        return InlineQueryResultCachedGif(
            gif_file_id=alter1(gif_file_id, self.gif_file_id),
            id=alter1(id, self.id),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultCachedMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif"""

    caption: str
    """ Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the video animation """
    mpeg4_file_id: str
    """ A valid file identifier for the MPEG4 file """
    parse_mode: str
    """ Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be mpeg4_gif """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        mpeg4_file_id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultCachedMpeg4Gif:
        return InlineQueryResultCachedMpeg4Gif(
            id=alter1(id, self.id),
            mpeg4_file_id=alter1(mpeg4_file_id, self.mpeg4_file_id),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultCachedPhoto:
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedphoto"""

    caption: str
    """ Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the photo """
    parse_mode: str
    """ Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    photo_file_id: str
    """ A valid file identifier of the photo """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be photo """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        photo_file_id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultCachedPhoto:
        return InlineQueryResultCachedPhoto(
            id=alter1(id, self.id),
            photo_file_id=alter1(photo_file_id, self.photo_file_id),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker"""

    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the sticker """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    sticker_file_id: str
    """ A valid file identifier of the sticker """
    type: str
    """ Type of the result, must be sticker """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        sticker_file_id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultCachedSticker:
        return InlineQueryResultCachedSticker(
            id=alter1(id, self.id),
            sticker_file_id=alter1(sticker_file_id, self.sticker_file_id),
            type=alter1(type, self.type),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultCachedVideo:
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedvideo"""

    caption: str
    """ Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the video """
    parse_mode: str
    """ Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Title for the result """
    type: str
    """ Type of the result, must be video """
    video_file_id: str
    """ A valid file identifier for the video file """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        video_file_id: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultCachedVideo:
        return InlineQueryResultCachedVideo(
            id=alter1(id, self.id),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            video_file_id=alter1(video_file_id, self.video_file_id),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultCachedVoice:
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcachedvoice"""

    caption: str
    """ Optional. Caption, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the voice message """
    parse_mode: str
    """ Optional. Mode for parsing entities in the voice message caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Voice message title """
    type: str
    """ Type of the result, must be voice """
    voice_file_id: str
    """ A valid file identifier for the voice message """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        voice_file_id: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultCachedVoice:
        return InlineQueryResultCachedVoice(
            id=alter1(id, self.id),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            voice_file_id=alter1(voice_file_id, self.voice_file_id),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultcontact"""

    first_name: str
    """ Contact's first name """
    id: str
    """ Unique identifier for this result, 1-64 Bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the contact """
    last_name: str
    """ Optional. Contact's last name """
    phone_number: str
    """ Contact's phone number """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_height: int
    """ Optional. Thumbnail height """
    thumbnail_url: str
    """ Optional. Url of the thumbnail for the result """
    thumbnail_width: int
    """ Optional. Thumbnail width """
    type: str
    """ Type of the result, must be contact """
    vcard: str
    """ Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes """

    def alter(
        self,
        first_name: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        phone_number: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        last_name: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_height: Omittable[Alterer1[int]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_width: Omittable[Alterer1[int]] = OMIT,
        vcard: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultContact:
        return InlineQueryResultContact(
            first_name=alter1(first_name, self.first_name),
            id=alter1(id, self.id),
            phone_number=alter1(phone_number, self.phone_number),
            type=alter1(type, self.type),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            last_name=alter1(last_name, self.last_name),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_height=alter1(thumbnail_height, self.thumbnail_height),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            thumbnail_width=alter1(thumbnail_width, self.thumbnail_width),
            vcard=alter1(vcard, self.vcard),
        )


@model
class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultdocument"""

    caption: str
    """ Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    document_url: str
    """ A valid URL for the file """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the file """
    mime_type: str
    """ MIME type of the content of the file, either "application/pdf" or "application/zip" """
    parse_mode: str
    """ Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_height: int
    """ Optional. Thumbnail height """
    thumbnail_url: str
    """ Optional. URL of the thumbnail (JPEG only) for the file """
    thumbnail_width: int
    """ Optional. Thumbnail width """
    title: str
    """ Title for the result """
    type: str
    """ Type of the result, must be document """

    def alter(
        self,
        document_url: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        mime_type: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_height: Omittable[Alterer1[int]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_width: Omittable[Alterer1[int]] = OMIT,
    ) -> InlineQueryResultDocument:
        return InlineQueryResultDocument(
            document_url=alter1(document_url, self.document_url),
            id=alter1(id, self.id),
            mime_type=alter1(mime_type, self.mime_type),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_height=alter1(thumbnail_height, self.thumbnail_height),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            thumbnail_width=alter1(thumbnail_width, self.thumbnail_width),
        )


@model
class InlineQueryResultGame:
    """Represents a Game.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultgame"""

    game_short_name: str
    """ Short name of the game """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    type: str
    """ Type of the result, must be game """

    def alter(
        self,
        game_short_name: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
    ) -> InlineQueryResultGame:
        return InlineQueryResultGame(
            game_short_name=alter1(game_short_name, self.game_short_name),
            id=alter1(id, self.id),
            type=alter1(type, self.type),
            reply_markup=alter1(reply_markup, self.reply_markup),
        )


@model
class InlineQueryResultGif:
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultgif"""

    caption: str
    """ Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    gif_duration: int
    """ Optional. Duration of the GIF in seconds """
    gif_height: int
    """ Optional. Height of the GIF """
    gif_url: str
    """ A valid URL for the GIF file. File size must not exceed 1MB """
    gif_width: int
    """ Optional. Width of the GIF """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the GIF animation """
    parse_mode: str
    """ Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_mime_type: str
    """ Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg" """
    thumbnail_url: str
    """ URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be gif """

    def alter(
        self,
        gif_url: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        gif_duration: Omittable[Alterer1[int]] = OMIT,
        gif_height: Omittable[Alterer1[int]] = OMIT,
        gif_width: Omittable[Alterer1[int]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_mime_type: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultGif:
        return InlineQueryResultGif(
            gif_url=alter1(gif_url, self.gif_url),
            id=alter1(id, self.id),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            gif_duration=alter1(gif_duration, self.gif_duration),
            gif_height=alter1(gif_height, self.gif_height),
            gif_width=alter1(gif_width, self.gif_width),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_mime_type=alter1(thumbnail_mime_type, self.thumbnail_mime_type),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultlocation"""

    heading: int
    """ Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. """
    horizontal_accuracy: float
    """ Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    id: str
    """ Unique identifier for this result, 1-64 Bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the location """
    latitude: float
    """ Location latitude in degrees """
    live_period: int
    """ Optional. Period in seconds for which the location can be updated, should be between 60 and 86400. """
    longitude: float
    """ Location longitude in degrees """
    proximity_alert_radius: int
    """ Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_height: int
    """ Optional. Thumbnail height """
    thumbnail_url: str
    """ Optional. Url of the thumbnail for the result """
    thumbnail_width: int
    """ Optional. Thumbnail width """
    title: str
    """ Location title """
    type: str
    """ Type of the result, must be location """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        heading: Omittable[Alterer1[int]] = OMIT,
        horizontal_accuracy: Omittable[Alterer1[float]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        live_period: Omittable[Alterer1[int]] = OMIT,
        proximity_alert_radius: Omittable[Alterer1[int]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_height: Omittable[Alterer1[int]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_width: Omittable[Alterer1[int]] = OMIT,
    ) -> InlineQueryResultLocation:
        return InlineQueryResultLocation(
            id=alter1(id, self.id),
            latitude=alter1(latitude, self.latitude),
            longitude=alter1(longitude, self.longitude),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            heading=alter1(heading, self.heading),
            horizontal_accuracy=alter1(horizontal_accuracy, self.horizontal_accuracy),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            live_period=alter1(live_period, self.live_period),
            proximity_alert_radius=alter1(
                proximity_alert_radius, self.proximity_alert_radius
            ),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_height=alter1(thumbnail_height, self.thumbnail_height),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            thumbnail_width=alter1(thumbnail_width, self.thumbnail_width),
        )


@model
class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif"""

    caption: str
    """ Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the video animation """
    mpeg4_duration: int
    """ Optional. Video duration in seconds """
    mpeg4_height: int
    """ Optional. Video height """
    mpeg4_url: str
    """ A valid URL for the MPEG4 file. File size must not exceed 1MB """
    mpeg4_width: int
    """ Optional. Video width """
    parse_mode: str
    """ Optional. Mode for parsing entities in the caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_mime_type: str
    """ Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg" """
    thumbnail_url: str
    """ URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be mpeg4_gif """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        mpeg4_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        mpeg4_duration: Omittable[Alterer1[int]] = OMIT,
        mpeg4_height: Omittable[Alterer1[int]] = OMIT,
        mpeg4_width: Omittable[Alterer1[int]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_mime_type: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultMpeg4Gif:
        return InlineQueryResultMpeg4Gif(
            id=alter1(id, self.id),
            mpeg4_url=alter1(mpeg4_url, self.mpeg4_url),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            mpeg4_duration=alter1(mpeg4_duration, self.mpeg4_duration),
            mpeg4_height=alter1(mpeg4_height, self.mpeg4_height),
            mpeg4_width=alter1(mpeg4_width, self.mpeg4_width),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_mime_type=alter1(thumbnail_mime_type, self.thumbnail_mime_type),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultphoto"""

    caption: str
    """ Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the photo """
    parse_mode: str
    """ Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    photo_height: int
    """ Optional. Height of the photo """
    photo_url: str
    """ A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB """
    photo_width: int
    """ Optional. Width of the photo """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_url: str
    """ URL of the thumbnail for the photo """
    title: str
    """ Optional. Title for the result """
    type: str
    """ Type of the result, must be photo """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        photo_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        photo_height: Omittable[Alterer1[int]] = OMIT,
        photo_width: Omittable[Alterer1[int]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InlineQueryResultPhoto:
        return InlineQueryResultPhoto(
            id=alter1(id, self.id),
            photo_url=alter1(photo_url, self.photo_url),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            photo_height=alter1(photo_height, self.photo_height),
            photo_width=alter1(photo_width, self.photo_width),
            reply_markup=alter1(reply_markup, self.reply_markup),
            title=alter1(title, self.title),
        )


@model
class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultvenue"""

    address: str
    """ Address of the venue """
    foursquare_id: str
    """ Optional. Foursquare identifier of the venue if known """
    foursquare_type: str
    """ Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str
    """ Optional. Google Places identifier of the venue """
    google_place_type: str
    """ Optional. Google Places type of the venue. (See supported types.) """
    id: str
    """ Unique identifier for this result, 1-64 Bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the venue """
    latitude: float
    """ Latitude of the venue location in degrees """
    longitude: float
    """ Longitude of the venue location in degrees """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_height: int
    """ Optional. Thumbnail height """
    thumbnail_url: str
    """ Optional. Url of the thumbnail for the result """
    thumbnail_width: int
    """ Optional. Thumbnail width """
    title: str
    """ Title of the venue """
    type: str
    """ Type of the result, must be venue """

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        foursquare_id: Omittable[Alterer1[str]] = OMIT,
        foursquare_type: Omittable[Alterer1[str]] = OMIT,
        google_place_id: Omittable[Alterer1[str]] = OMIT,
        google_place_type: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        thumbnail_height: Omittable[Alterer1[int]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        thumbnail_width: Omittable[Alterer1[int]] = OMIT,
    ) -> InlineQueryResultVenue:
        return InlineQueryResultVenue(
            address=alter1(address, self.address),
            id=alter1(id, self.id),
            latitude=alter1(latitude, self.latitude),
            longitude=alter1(longitude, self.longitude),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            foursquare_id=alter1(foursquare_id, self.foursquare_id),
            foursquare_type=alter1(foursquare_type, self.foursquare_type),
            google_place_id=alter1(google_place_id, self.google_place_id),
            google_place_type=alter1(google_place_type, self.google_place_type),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            reply_markup=alter1(reply_markup, self.reply_markup),
            thumbnail_height=alter1(thumbnail_height, self.thumbnail_height),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            thumbnail_width=alter1(thumbnail_width, self.thumbnail_width),
        )


@model
class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultvideo"""

    caption: str
    """ Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    description: str
    """ Optional. Short description of the result """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video). """
    mime_type: str
    """ MIME type of the content of the video URL, "text/html" or "video/mp4" """
    parse_mode: str
    """ Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    thumbnail_url: str
    """ URL of the thumbnail (JPEG only) for the video """
    title: str
    """ Title for the result """
    type: str
    """ Type of the result, must be video """
    video_duration: int
    """ Optional. Video duration in seconds """
    video_height: int
    """ Optional. Video height """
    video_url: str
    """ A valid URL for the embedded video player or video file """
    video_width: int
    """ Optional. Video width """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        mime_type: Omittable[Alterer1[str]] = OMIT,
        thumbnail_url: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        video_url: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        video_duration: Omittable[Alterer1[int]] = OMIT,
        video_height: Omittable[Alterer1[int]] = OMIT,
        video_width: Omittable[Alterer1[int]] = OMIT,
    ) -> InlineQueryResultVideo:
        return InlineQueryResultVideo(
            id=alter1(id, self.id),
            mime_type=alter1(mime_type, self.mime_type),
            thumbnail_url=alter1(thumbnail_url, self.thumbnail_url),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            video_url=alter1(video_url, self.video_url),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            description=alter1(description, self.description),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            video_duration=alter1(video_duration, self.video_duration),
            video_height=alter1(video_height, self.video_height),
            video_width=alter1(video_width, self.video_width),
        )


@model
class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultvoice"""

    caption: str
    """ Optional. Caption, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    id: str
    """ Unique identifier for this result, 1-64 bytes """
    input_message_content: _input_message_content.InputMessageContent
    """ Optional. Content of the message to be sent instead of the voice recording """
    parse_mode: str
    """ Optional. Mode for parsing entities in the voice message caption. See formatting options for more details. """
    reply_markup: _inline_keyboard_markup.InlineKeyboardMarkup
    """ Optional. Inline keyboard attached to the message """
    title: str
    """ Recording title """
    type: str
    """ Type of the result, must be voice """
    voice_duration: int
    """ Optional. Recording duration in seconds """
    voice_url: str
    """ A valid URL for the voice recording """

    def alter(
        self,
        id: Omittable[Alterer1[str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        voice_url: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        input_message_content: Omittable[
            Alterer1[_input_message_content.InputMessageContent]
        ] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        reply_markup: Omittable[
            Alterer1[_inline_keyboard_markup.InlineKeyboardMarkup]
        ] = OMIT,
        voice_duration: Omittable[Alterer1[int]] = OMIT,
    ) -> InlineQueryResultVoice:
        return InlineQueryResultVoice(
            id=alter1(id, self.id),
            title=alter1(title, self.title),
            type=alter1(type, self.type),
            voice_url=alter1(voice_url, self.voice_url),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            input_message_content=alter1(
                input_message_content, self.input_message_content
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            reply_markup=alter1(reply_markup, self.reply_markup),
            voice_duration=alter1(voice_duration, self.voice_duration),
        )


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
__all__ = [
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultContact",
    "InlineQueryResultDocument",
    "InlineQueryResultGame",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "InlineQueryResult",
]
