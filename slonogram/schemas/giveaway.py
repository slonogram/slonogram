from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Giveaway:
    """This object represents a message about a scheduled giveaway.
    Telegram docs: https://core.telegram.org/bots/api#giveaway"""

    chats: list[_chat.Chat]
    """ The list of chats which the user must join to participate in the giveaway """
    country_codes: list[str]
    """ Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways. """
    has_public_winners: bool
    """ Optional. True, if the list of giveaway winners will be visible to everyone """
    only_new_members: bool
    """ Optional. True, if only users who join the chats after the giveaway started should be eligible to win """
    premium_subscription_month_count: int
    """ Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for """
    prize_description: str
    """ Optional. Description of additional giveaway prize """
    winner_count: int
    """ The number of users which are supposed to be selected as winners of the giveaway """
    winners_selection_date: int
    """ Point in time (Unix timestamp) when winners of the giveaway will be selected """

    def alter(
        self,
        chats: Omittable[Alterer1[list[_chat.Chat]]] = OMIT,
        winner_count: Omittable[Alterer1[int]] = OMIT,
        winners_selection_date: Omittable[Alterer1[int]] = OMIT,
        country_codes: Omittable[Alterer1[list[str]]] = OMIT,
        has_public_winners: Omittable[Alterer1[bool]] = OMIT,
        only_new_members: Omittable[Alterer1[bool]] = OMIT,
        premium_subscription_month_count: Omittable[Alterer1[int]] = OMIT,
        prize_description: Omittable[Alterer1[str]] = OMIT,
    ) -> Giveaway:
        return Giveaway(
            chats=alter1(chats, self.chats),
            winner_count=alter1(winner_count, self.winner_count),
            winners_selection_date=alter1(
                winners_selection_date, self.winners_selection_date
            ),
            country_codes=alter1(country_codes, self.country_codes),
            has_public_winners=alter1(has_public_winners, self.has_public_winners),
            only_new_members=alter1(only_new_members, self.only_new_members),
            premium_subscription_month_count=alter1(
                premium_subscription_month_count, self.premium_subscription_month_count
            ),
            prize_description=alter1(prize_description, self.prize_description),
        )


__all__ = ["Giveaway"]
