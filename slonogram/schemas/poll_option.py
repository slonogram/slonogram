from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class PollOption:
    """This object contains information about one answer option in a poll.
    Telegram docs: https://core.telegram.org/bots/api#polloption"""

    text: str
    """ Option text, 1-100 characters """
    voter_count: int
    """ Number of users that voted for this option """

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        voter_count: Omittable[Alterer1[int]] = OMIT,
    ) -> PollOption:
        return PollOption(
            text=alter1(text, self.text),
            voter_count=alter1(voter_count, self.voter_count),
        )


__all__ = ["PollOption"]
