from __future__ import annotations
from slonogram.schemas import message_entity as _message_entity
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ReplyParameters:
    """Describes reply parameters for the message that is being sent.

    Telegram documentation: https://core.telegram.org/bots/api#replyparameters"""

    message_id: int
    """ Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified """
    allow_sending_without_reply: bool | None = None
    """ Optional. Pass True if the message should be sent even if the specified message to be replied to is not found; can be used only for replies in the same chat and forum topic. """
    chat_id: int | str | None = None
    """ Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername) """
    quote: str | None = None
    """ Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message. """
    quote_entities: tuple[_message_entity.MessageEntity, ...] | None = None
    """ Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode. """
    quote_parse_mode: str | None = None
    """ Optional. Mode for parsing entities in the quote. See formatting options for more details. """
    quote_position: int | None = None
    """ Optional. Position of the quote in the original message in UTF-16 code units """

    def alter(
        self,
        message_id: Omittable[Alterer1[int]] = OMIT,
        allow_sending_without_reply: Omittable[Alterer1[bool | None]] = OMIT,
        chat_id: Omittable[Alterer1[int | str | None]] = OMIT,
        quote: Omittable[Alterer1[str | None]] = OMIT,
        quote_entities: Omittable[
            Alterer1[tuple[_message_entity.MessageEntity, ...] | None]
        ] = OMIT,
        quote_parse_mode: Omittable[Alterer1[str | None]] = OMIT,
        quote_position: Omittable[Alterer1[int | None]] = OMIT,
    ) -> ReplyParameters:
        return ReplyParameters(
            message_id=alter1(message_id, self.message_id),
            allow_sending_without_reply=alter1(
                allow_sending_without_reply, self.allow_sending_without_reply
            ),
            chat_id=alter1(chat_id, self.chat_id),
            quote=alter1(quote, self.quote),
            quote_entities=alter1(quote_entities, self.quote_entities),
            quote_parse_mode=alter1(quote_parse_mode, self.quote_parse_mode),
            quote_position=alter1(quote_position, self.quote_position),
        )


__all__ = ["ReplyParameters"]
