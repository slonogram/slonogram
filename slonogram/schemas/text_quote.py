"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import message_entity as _message_entity
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class TextQuote:
    """This object contains information about the quoted part of a message
    that is replied to by the given message.  Telegram documentation:
    https://core.telegram.org/bots/api#textquote"""

    position: int
    """Approximate quote position in the original message in UTF-16 code
    units as specified by the sender"""
    text: str
    """Text of the quoted part of a message that is replied to by the given
    message"""
    entities: tuple[_message_entity.MessageEntity, ...] | None = None
    """Optional. Special entities that appear in the quote. Currently, only
    bold, italic, underline, strikethrough, spoiler, and custom_emoji
    entities are kept in quotes."""
    is_manual: bool | None = None
    """Optional. True, if the quote was chosen manually by the message
    sender. Otherwise, the quote was added automatically by the server."""

    def alter(
        self,
        position: Omittable[Alterer1[int]] = OMIT,
        text: Omittable[Alterer1[str]] = OMIT,
        entities: Omittable[
            Alterer1[tuple[_message_entity.MessageEntity, ...] | None]
        ] = OMIT,
        is_manual: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> TextQuote:
        return TextQuote(
            position=alter1(position, self.position),
            text=alter1(text, self.text),
            entities=alter1(entities, self.entities),
            is_manual=alter1(is_manual, self.is_manual),
        )


__all__ = ["TextQuote"]
