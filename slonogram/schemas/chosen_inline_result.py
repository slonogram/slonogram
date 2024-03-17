from __future__ import annotations
from slonogram.schemas import user as _user, location as _location
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.

    Telegram documentation: https://core.telegram.org/bots/api#choseninlineresult"""

    from_: _user.User
    """ The user that chose the result """
    query: str
    """ The query that was used to obtain the result """
    result_id: str
    """ The unique identifier for the result that was chosen """
    inline_message_id: str | None = None
    """ Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message. """
    location: _location.Location | None = None
    """ Optional. Sender location, only for bots that require user location """

    def alter(
        self,
        from_: Omittable[Alterer1[_user.User]] = OMIT,
        query: Omittable[Alterer1[str]] = OMIT,
        result_id: Omittable[Alterer1[str]] = OMIT,
        inline_message_id: Omittable[Alterer1[str | None]] = OMIT,
        location: Omittable[Alterer1[_location.Location | None]] = OMIT,
    ) -> ChosenInlineResult:
        return ChosenInlineResult(
            from_=alter1(from_, self.from_),
            query=alter1(query, self.query),
            result_id=alter1(result_id, self.result_id),
            inline_message_id=alter1(inline_message_id, self.inline_message_id),
            location=alter1(location, self.location),
        )


__all__ = ["ChosenInlineResult"]
