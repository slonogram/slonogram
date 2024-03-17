from __future__ import annotations
from slonogram.schemas import (
    chat as _chat,
    reaction_type as _reaction_type,
    user as _user,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class MessageReactionUpdated:
    """This object represents a change of a reaction on a message performed by a user.

    Telegram documentation: https://core.telegram.org/bots/api#messagereactionupdated"""

    chat: _chat.Chat
    """ The chat containing the message the user reacted to """
    date: int
    """ Date of the change in Unix time """
    message_id: int
    """ Unique identifier of the message inside the chat """
    new_reaction: tuple[_reaction_type.ReactionType, ...]
    """ New list of reaction types that have been set by the user """
    old_reaction: tuple[_reaction_type.ReactionType, ...]
    """ Previous list of reaction types that were set by the user """
    actor_chat: _chat.Chat | None = None
    """ Optional. The chat on behalf of which the reaction was changed, if the user is anonymous """
    user: _user.User | None = None
    """ Optional. The user that changed the reaction, if the user isn't anonymous """

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        date: Omittable[Alterer1[int]] = OMIT,
        message_id: Omittable[Alterer1[int]] = OMIT,
        new_reaction: Omittable[
            Alterer1[tuple[_reaction_type.ReactionType, ...]]
        ] = OMIT,
        old_reaction: Omittable[
            Alterer1[tuple[_reaction_type.ReactionType, ...]]
        ] = OMIT,
        actor_chat: Omittable[Alterer1[_chat.Chat | None]] = OMIT,
        user: Omittable[Alterer1[_user.User | None]] = OMIT,
    ) -> MessageReactionUpdated:
        return MessageReactionUpdated(
            chat=alter1(chat, self.chat),
            date=alter1(date, self.date),
            message_id=alter1(message_id, self.message_id),
            new_reaction=alter1(new_reaction, self.new_reaction),
            old_reaction=alter1(old_reaction, self.old_reaction),
            actor_chat=alter1(actor_chat, self.actor_chat),
            user=alter1(user, self.user),
        )


__all__ = ["MessageReactionUpdated"]
