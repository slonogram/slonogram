from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import message_entity as _message_entity
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class TextQuote:
    """This object contains information about the quoted part of a message that is replied to by the given message.
    Telegram docs: https://core.telegram.org/bots/api#textquote"""

    entities: list[_message_entity.MessageEntity]
    """ Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes. """
    is_manual: bool
    """ Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server. """
    position: int
    """ Approximate quote position in the original message in UTF-16 code units as specified by the sender """
    text: str
    """ Text of the quoted part of a message that is replied to by the given message """

    def alter(
        self,
        position: Omittable[Alterer1[int]] = OMIT,
        text: Omittable[Alterer1[str]] = OMIT,
        entities: Omittable[Alterer1[list[_message_entity.MessageEntity]]] = OMIT,
        is_manual: Omittable[Alterer1[bool]] = OMIT,
    ):
        return TextQuote(
            position=alter1(position, self.position),
            text=alter1(text, self.text),
            entities=alter1(entities, self.entities),
            is_manual=alter1(is_manual, self.is_manual),
        )


__all__ = ["TextQuote"]
