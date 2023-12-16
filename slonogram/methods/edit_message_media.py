# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 17:59:35.955291
from dataclasses import dataclass
from slonogram.schemas import InputMedia, InlineKeyboardMarkup
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditMessageMedia:
    """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""

    media: InputMedia
    """A JSON-serialized object for a new media content of the message """
    chat_id: int | str | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the message to edit """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """
    reply_markup: InlineKeyboardMarkup | None = None
    """A JSON-serialized object for a new inline keyboard. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        collect_attachs_from(self.media, dest)


__all__ = ["EditMessageMedia"]
