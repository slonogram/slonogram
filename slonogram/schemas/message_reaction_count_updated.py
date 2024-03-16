from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat, reaction_count as _reaction_count
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class MessageReactionCountUpdated:
    """This object represents reaction changes on a message with anonymous reactions.
    Telegram docs: https://core.telegram.org/bots/api#messagereactioncountupdated"""

    chat: _chat.Chat
    """ The chat containing the message """
    date: int
    """ Date of the change in Unix time """
    message_id: int
    """ Unique message identifier inside the chat """
    reactions: list[_reaction_count.ReactionCount]
    """ List of reactions that are present on the message """

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        reactions: Omittable[Alterer1[list[_reaction_count.ReactionCount]]] = OMIT,
    ) -> MessageReactionCountUpdated:
        return MessageReactionCountUpdated(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            reactions=alter1(reactions, self.reactions),
        )


__all__ = ["MessageReactionCountUpdated"]
