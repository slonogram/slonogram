from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import message_entity as _message_entity
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ReplyParameters:
    """Describes reply parameters for the message that is being sent.
    Telegram docs: https://core.telegram.org/bots/api#replyparameters"""

    allow_sending_without_reply: bool
    """ Optional. Pass True if the message should be sent even if the specified message to be replied to is not found; can be used only for replies in the same chat and forum topic. """
    chat_id: int | str
    """ Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername) """
    message_id: int
    """ Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified """
    quote: str
    """ Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message. """
    quote_entities: list[_message_entity.MessageEntity]
    """ Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode. """
    quote_parse_mode: str
    """ Optional. Mode for parsing entities in the quote. See formatting options for more details. """
    quote_position: int
    """ Optional. Position of the quote in the original message in UTF-16 code units """

    def alter(
        self,
        message_id: Omittable[Alterer1[int]] = OMIT,
        allow_sending_without_reply: Omittable[Alterer1[bool]] = OMIT,
        chat_id: Omittable[Alterer1[int | str]] = OMIT,
        quote: Omittable[Alterer1[str]] = OMIT,
        quote_entities: Omittable[Alterer1[list[_message_entity.MessageEntity]]] = OMIT,
        quote_parse_mode: Omittable[Alterer1[str]] = OMIT,
        quote_position: Omittable[Alterer1[int]] = OMIT,
    ):
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
