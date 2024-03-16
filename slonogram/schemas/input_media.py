from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    input_file as _input_file,
    message_entity as _message_entity,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    Telegram docs: https://core.telegram.org/bots/api#inputmediaanimation"""

    caption: str
    """ Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    duration: int
    """ Optional. Animation duration in seconds """
    has_spoiler: bool
    """ Optional. Pass True if the animation needs to be covered with a spoiler animation """
    height: int
    """ Optional. Animation height """
    media: str
    """ File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    parse_mode: str
    """ Optional. Mode for parsing entities in the animation caption. See formatting options for more details. """
    thumbnail: _input_file.InputFile | str
    """ Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    type: str
    """ Type of the result, must be animation """
    width: int
    """ Optional. Animation width """

    def alter(
        self,
        media: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        duration: Omittable[Alterer1[int]] = OMIT,
        has_spoiler: Omittable[Alterer1[bool]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_input_file.InputFile | str]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
    ) -> InputMediaAnimation:
        return InputMediaAnimation(
            media=alter1(media, self.media),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            duration=alter1(duration, self.duration),
            has_spoiler=alter1(has_spoiler, self.has_spoiler),
            height=alter1(height, self.height),
            parse_mode=alter1(parse_mode, self.parse_mode),
            thumbnail=alter1(thumbnail, self.thumbnail),
            width=alter1(width, self.width),
        )


@model
class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent.
    Telegram docs: https://core.telegram.org/bots/api#inputmediaaudio"""

    caption: str
    """ Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    duration: int
    """ Optional. Duration of the audio in seconds """
    media: str
    """ File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    parse_mode: str
    """ Optional. Mode for parsing entities in the audio caption. See formatting options for more details. """
    performer: str
    """ Optional. Performer of the audio """
    thumbnail: _input_file.InputFile | str
    """ Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    title: str
    """ Optional. Title of the audio """
    type: str
    """ Type of the result, must be audio """

    def alter(
        self,
        media: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        duration: Omittable[Alterer1[int]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        performer: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_input_file.InputFile | str]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> InputMediaAudio:
        return InputMediaAudio(
            media=alter1(media, self.media),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            duration=alter1(duration, self.duration),
            parse_mode=alter1(parse_mode, self.parse_mode),
            performer=alter1(performer, self.performer),
            thumbnail=alter1(thumbnail, self.thumbnail),
            title=alter1(title, self.title),
        )


@model
class InputMediaDocument:
    """Represents a general file to be sent.
    Telegram docs: https://core.telegram.org/bots/api#inputmediadocument"""

    caption: str
    """ Optional. Caption of the document to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    disable_content_type_detection: bool
    """ Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album. """
    media: str
    """ File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    parse_mode: str
    """ Optional. Mode for parsing entities in the document caption. See formatting options for more details. """
    thumbnail: _input_file.InputFile | str
    """ Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    type: str
    """ Type of the result, must be document """

    def alter(
        self,
        media: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        disable_content_type_detection: Omittable[Alterer1[bool]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_input_file.InputFile | str]] = OMIT,
    ) -> InputMediaDocument:
        return InputMediaDocument(
            media=alter1(media, self.media),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            disable_content_type_detection=alter1(
                disable_content_type_detection, self.disable_content_type_detection
            ),
            parse_mode=alter1(parse_mode, self.parse_mode),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


@model
class InputMediaPhoto:
    """Represents a photo to be sent.
    Telegram docs: https://core.telegram.org/bots/api#inputmediaphoto"""

    caption: str
    """ Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    has_spoiler: bool
    """ Optional. Pass True if the photo needs to be covered with a spoiler animation """
    media: str
    """ File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    parse_mode: str
    """ Optional. Mode for parsing entities in the photo caption. See formatting options for more details. """
    type: str
    """ Type of the result, must be photo """

    def alter(
        self,
        media: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        has_spoiler: Omittable[Alterer1[bool]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
    ) -> InputMediaPhoto:
        return InputMediaPhoto(
            media=alter1(media, self.media),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            has_spoiler=alter1(has_spoiler, self.has_spoiler),
            parse_mode=alter1(parse_mode, self.parse_mode),
        )


@model
class InputMediaVideo:
    """Represents a video to be sent.
    Telegram docs: https://core.telegram.org/bots/api#inputmediavideo"""

    caption: str
    """ Optional. Caption of the video to be sent, 0-1024 characters after entities parsing """
    caption_entities: list[_message_entity.MessageEntity]
    """ Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode """
    duration: int
    """ Optional. Video duration in seconds """
    has_spoiler: bool
    """ Optional. Pass True if the video needs to be covered with a spoiler animation """
    height: int
    """ Optional. Video height """
    media: str
    """ File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    parse_mode: str
    """ Optional. Mode for parsing entities in the video caption. See formatting options for more details. """
    supports_streaming: bool
    """ Optional. Pass True if the uploaded video is suitable for streaming """
    thumbnail: _input_file.InputFile | str
    """ Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    type: str
    """ Type of the result, must be video """
    width: int
    """ Optional. Video width """

    def alter(
        self,
        media: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        caption: Omittable[Alterer1[str]] = OMIT,
        caption_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        duration: Omittable[Alterer1[int]] = OMIT,
        has_spoiler: Omittable[Alterer1[bool]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        parse_mode: Omittable[Alterer1[str]] = OMIT,
        supports_streaming: Omittable[Alterer1[bool]] = OMIT,
        thumbnail: Omittable[Alterer1[_input_file.InputFile | str]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
    ) -> InputMediaVideo:
        return InputMediaVideo(
            media=alter1(media, self.media),
            type=alter1(type, self.type),
            caption=alter1(caption, self.caption),
            caption_entities=alter1(caption_entities, self.caption_entities),
            duration=alter1(duration, self.duration),
            has_spoiler=alter1(has_spoiler, self.has_spoiler),
            height=alter1(height, self.height),
            parse_mode=alter1(parse_mode, self.parse_mode),
            supports_streaming=alter1(supports_streaming, self.supports_streaming),
            thumbnail=alter1(thumbnail, self.thumbnail),
            width=alter1(width, self.width),
        )


InputMedia: TypeAlias = (
    InputMediaAnimation
    | InputMediaDocument
    | InputMediaAudio
    | InputMediaPhoto
    | InputMediaVideo
)
__all__ = [
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMedia",
]
