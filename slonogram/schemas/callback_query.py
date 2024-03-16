from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    user as _user,
    maybe_inaccessible_message as _maybe_inaccessible_message,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class CallbackQuery:
    chat_instance: str
    """ Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games. """
    data: str
    """ Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data. """
    from_: _user.User
    """ Sender """
    game_short_name: str
    """ Optional. Short name of a Game to be returned, serves as the unique identifier for the game """
    id: str
    """ Unique identifier for this query """
    inline_message_id: str
    """ Optional. Identifier of the message sent via the bot in inline mode, that originated the query. """
    message: _maybe_inaccessible_message.MaybeInaccessibleMessage
    """ Optional. Message sent by the bot with the callback button that originated the query """

    def alter(
        self,
        chat_instance: Omittable[Alterer1[str]] = OMIT,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        data: Omittable[Alterer1[str]] = OMIT,
        game_short_name: Omittable[Alterer1[str]] = OMIT,
        inline_message_id: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[
            Alterer1[_maybe_inaccessible_message.MaybeInaccessibleMessage]
        ] = OMIT,
    ):
        return CallbackQuery(
            chat_instance=alter1(chat_instance, self.chat_instance),
            from_=alter1(from_, self.from_),
            id=alter1(id, self.id),
            data=alter1(data, self.data),
            game_short_name=alter1(game_short_name, self.game_short_name),
            inline_message_id=alter1(inline_message_id, self.inline_message_id),
            message=alter1(message, self.message),
        )


__all__ = ["CallbackQuery"]
