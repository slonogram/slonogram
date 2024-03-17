from __future__ import annotations
from slonogram.schemas import user as _user, chat as _chat
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll.

    Telegram documentation: https://core.telegram.org/bots/api#pollanswer"""

    option_ids: tuple[int, ...]
    """ 0-based identifiers of chosen answer options. May be empty if the vote was retracted. """
    poll_id: str
    """ Unique poll identifier """
    user: _user.User | None = None
    """ Optional. The user that changed the answer to the poll, if the voter isn't anonymous """
    voter_chat: _chat.Chat | None = None
    """ Optional. The chat that changed the answer to the poll, if the voter is anonymous """

    def alter(
        self,
        option_ids: Omittable[Alterer1[tuple[int, ...]]] = OMIT,
        poll_id: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User | None]] = OMIT,
        voter_chat: Omittable[Alterer1[_chat.Chat | None]] = OMIT,
    ) -> PollAnswer:
        return PollAnswer(
            option_ids=alter1(option_ids, self.option_ids),
            poll_id=alter1(poll_id, self.poll_id),
            user=alter1(user, self.user),
            voter_chat=alter1(voter_chat, self.voter_chat),
        )


__all__ = ["PollAnswer"]
