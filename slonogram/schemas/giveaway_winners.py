"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import chat as _chat, user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class GiveawayWinners:
    """This object represents a message about the completion of a giveaway
    with public winners.  Telegram documentation:
    https://core.telegram.org/bots/api#giveawaywinners"""

    chat: _chat.Chat
    """The chat that created the giveaway"""
    giveaway_message_id: int
    """Identifier of the message with the giveaway in the chat"""
    winner_count: int
    """Total number of winners in the giveaway"""
    winners: tuple[_user.User, ...]
    """List of up to 100 winners of the giveaway"""
    winners_selection_date: int
    """Point in time (Unix timestamp) when winners of the giveaway were
    selected"""
    additional_chat_count: int | None = None
    """Optional. The number of other chats the user had to join in order to
    be eligible for the giveaway"""
    only_new_members: bool | None = None
    """Optional. True, if only users who had joined the chats after the
    giveaway started were eligible to win"""
    premium_subscription_month_count: int | None = None
    """Optional. The number of months the Telegram Premium subscription won
    from the giveaway will be active for"""
    prize_description: str | None = None
    """Optional. Description of additional giveaway prize"""
    unclaimed_prize_count: int | None = None
    """Optional. Number of undistributed prizes"""
    was_refunded: bool | None = None
    """Optional. True, if the giveaway was canceled because the payment for
    it was refunded"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        giveaway_message_id: Omittable[Alterer1[int]] = OMIT,
        winner_count: Omittable[Alterer1[int]] = OMIT,
        winners: Omittable[Alterer1[tuple[_user.User, ...]]] = OMIT,
        winners_selection_date: Omittable[Alterer1[int]] = OMIT,
        additional_chat_count: Omittable[Alterer1[int | None]] = OMIT,
        only_new_members: Omittable[Alterer1[bool | None]] = OMIT,
        premium_subscription_month_count: Omittable[Alterer1[int | None]] = OMIT,
        prize_description: Omittable[Alterer1[str | None]] = OMIT,
        unclaimed_prize_count: Omittable[Alterer1[int | None]] = OMIT,
        was_refunded: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> GiveawayWinners:
        return GiveawayWinners(
            chat=alter1(chat, self.chat),
            giveaway_message_id=alter1(giveaway_message_id, self.giveaway_message_id),
            winner_count=alter1(winner_count, self.winner_count),
            winners=alter1(winners, self.winners),
            winners_selection_date=alter1(
                winners_selection_date, self.winners_selection_date
            ),
            additional_chat_count=alter1(
                additional_chat_count, self.additional_chat_count
            ),
            only_new_members=alter1(only_new_members, self.only_new_members),
            premium_subscription_month_count=alter1(
                premium_subscription_month_count, self.premium_subscription_month_count
            ),
            prize_description=alter1(prize_description, self.prize_description),
            unclaimed_prize_count=alter1(
                unclaimed_prize_count, self.unclaimed_prize_count
            ),
            was_refunded=alter1(was_refunded, self.was_refunded),
        )


__all__ = ["GiveawayWinners"]
