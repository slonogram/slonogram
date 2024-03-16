from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat_boost as _chat_boost
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class UserChatBoosts:
    boosts: list[_chat_boost.ChatBoost]
    """ The list of boosts added to the chat by the user """

    def alter(self, boosts: Omittable[Alterer1[list[_chat_boost.ChatBoost]]] = OMIT):
        return UserChatBoosts(
            boosts=alter1(boosts, self.boosts),
        )


__all__ = ["UserChatBoosts"]
