from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import reaction_type as _reaction_type
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ReactionCount:
    """Represents a reaction added to a message along with the number of times it was added.
    Telegram docs: https://core.telegram.org/bots/api#reactioncount"""

    total_count: int
    """ Number of times the reaction was added """
    type: _reaction_type.ReactionType
    """ Type of the reaction """

    def alter(
        self,
        total_count: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[_reaction_type.ReactionType]] = OMIT,
    ) -> ReactionCount:
        return ReactionCount(
            total_count=alter1(total_count, self.total_count),
            type=alter1(type, self.type),
        )


__all__ = ["ReactionCount"]
