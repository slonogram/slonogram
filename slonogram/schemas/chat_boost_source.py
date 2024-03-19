"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass
from typing import TypeAlias


@dataclass(slots=True)
class ChatBoostSourceGiftCode:
    """The boost was obtained by the creation of Telegram Premium gift codes
    to boost a chat. Each such code boosts the chat 4 times for the
    duration of the corresponding Telegram Premium subscription.  Telegram
    documentation:
    https://core.telegram.org/bots/api#chatboostsourcegiftcode"""

    source: str
    """Source of the boost, always "gift_code" """
    user: _user.User
    """User for which the gift code was created"""

    def alter(
        self,
        source: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ) -> ChatBoostSourceGiftCode:
        return ChatBoostSourceGiftCode(
            source=alter1(source, self.source),
            user=alter1(user, self.user),
        )


@dataclass(slots=True)
class ChatBoostSourceGiveaway:
    """The boost was obtained by the creation of a Telegram Premium giveaway.
    This boosts the chat 4 times for the duration of the corresponding
    Telegram Premium subscription.  Telegram documentation:
    https://core.telegram.org/bots/api#chatboostsourcegiveaway"""

    giveaway_message_id: int
    """Identifier of a message in the chat with the giveaway; the message
    could have been deleted already. May be 0 if the message isn't sent
    yet."""
    source: str
    """Source of the boost, always "giveaway" """
    is_unclaimed: bool | None = None
    """Optional. True, if the giveaway was completed, but there was no user
    to win the prize"""
    user: _user.User | None = None
    """Optional. User that won the prize in the giveaway if any"""

    def alter(
        self,
        giveaway_message_id: Omittable[Alterer1[int]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        is_unclaimed: Omittable[Alterer1[bool | None]] = OMIT,
        user: Omittable[Alterer1[_user.User | None]] = OMIT,
    ) -> ChatBoostSourceGiveaway:
        return ChatBoostSourceGiveaway(
            giveaway_message_id=alter1(giveaway_message_id, self.giveaway_message_id),
            source=alter1(source, self.source),
            is_unclaimed=alter1(is_unclaimed, self.is_unclaimed),
            user=alter1(user, self.user),
        )


@dataclass(slots=True)
class ChatBoostSourcePremium:
    """The boost was obtained by subscribing to Telegram Premium or by
    gifting a Telegram Premium subscription to another user.  Telegram
    documentation:
    https://core.telegram.org/bots/api#chatboostsourcepremium"""

    source: str
    """Source of the boost, always "premium" """
    user: _user.User
    """User that boosted the chat"""

    def alter(
        self,
        source: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ) -> ChatBoostSourcePremium:
        return ChatBoostSourcePremium(
            source=alter1(source, self.source),
            user=alter1(user, self.user),
        )


ChatBoostSource: TypeAlias = (
    ChatBoostSourcePremium | ChatBoostSourceGiftCode | ChatBoostSourceGiveaway
)
""" This object describes the source of a chat boost. It can be one of
- ChatBoostSourcePremium
- ChatBoostSourceGiftCode
- ChatBoostSourceGiveaway

Telegram documentation: https://core.telegram.org/bots/api#chatboostsource """
__all__ = [
    "ChatBoostSource",
    "ChatBoostSourceGiftCode",
    "ChatBoostSourceGiveaway",
    "ChatBoostSourcePremium",
]
