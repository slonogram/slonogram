from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import maybe_inaccessible_message as _maybe_inaccessible_message
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class GiveawayCompleted:
    """This object represents a service message about the completion of a giveaway without public winners.
    Telegram docs: https://core.telegram.org/bots/api#giveawaycompleted"""

    giveaway_message: _maybe_inaccessible_message.Message
    """ Optional. Message with the giveaway that was completed, if it wasn't deleted """
    unclaimed_prize_count: int
    """ Optional. Number of undistributed prizes """
    winner_count: int
    """ Number of winners in the giveaway """

    def alter(
        self,
        winner_count: Omittable[Alterer1[int]] = OMIT,
        giveaway_message: Omittable[
            Alterer1[_maybe_inaccessible_message.Message]
        ] = OMIT,
        unclaimed_prize_count: Omittable[Alterer1[int]] = OMIT,
    ):
        return GiveawayCompleted(
            winner_count=alter1(winner_count, self.winner_count),
            giveaway_message=alter1(giveaway_message, self.giveaway_message),
            unclaimed_prize_count=alter1(
                unclaimed_prize_count, self.unclaimed_prize_count
            ),
        )


__all__ = ["GiveawayCompleted"]
