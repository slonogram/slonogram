"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import chat as _chat, reaction_count as _reaction_count
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class MessageReactionCountUpdated:
    """This object represents reaction changes on a message with anonymous
    reactions.  Telegram documentation:
    https://core.telegram.org/bots/api#messagereactioncountupdated"""

    chat: _chat.Chat
    """The chat containing the message"""
    date: int
    """Date of the change in Unix time"""
    message_id: int
    """Unique message identifier inside the chat"""
    reactions: tuple[_reaction_count.ReactionCount, ...]
    """List of reactions that are present on the message"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        reactions: Omittable[
            Alterer1[tuple[_reaction_count.ReactionCount, ...]]
        ] = OMIT,
    ) -> MessageReactionCountUpdated:
        return MessageReactionCountUpdated(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            reactions=alter1(reactions, self.reactions),
        )


__all__ = ["MessageReactionCountUpdated"]
