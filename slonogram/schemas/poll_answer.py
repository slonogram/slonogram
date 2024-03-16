from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat, user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class PollAnswer:
    option_ids: list[int]
    """ 0-based identifiers of chosen answer options. May be empty if the vote was retracted. """
    poll_id: str
    """ Unique poll identifier """
    user: _user.User
    """ Optional. The user that changed the answer to the poll, if the voter isn't anonymous """
    voter_chat: _chat.Chat
    """ Optional. The chat that changed the answer to the poll, if the voter is anonymous """

    def alter(
        self,
        option_ids: Omittable[Alterer1[list[int]]] = OMIT,
        poll_id: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
        voter_chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
    ):
        return PollAnswer(
            option_ids=alter1(option_ids, self.option_ids),
            poll_id=alter1(poll_id, self.poll_id),
            user=alter1(user, self.user),
            voter_chat=alter1(voter_chat, self.voter_chat),
        )


__all__ = ["PollAnswer"]
