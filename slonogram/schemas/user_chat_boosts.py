from __future__ import annotations
from slonogram.schemas import chat_boost as _chat_boost
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class UserChatBoosts:
    """This object represents a list of boosts added to a chat by a user.

    Telegram documentation: https://core.telegram.org/bots/api#userchatboosts"""

    boosts: tuple[_chat_boost.ChatBoost, ...]
    """ The list of boosts added to the chat by the user """

    def alter(
        self, boosts: Omittable[Alterer1[tuple[_chat_boost.ChatBoost, ...]]] = OMIT
    ) -> UserChatBoosts:
        return UserChatBoosts(
            boosts=alter1(boosts, self.boosts),
        )


__all__ = ["UserChatBoosts"]
