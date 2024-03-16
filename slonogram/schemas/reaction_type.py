from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class ReactionTypeCustomEmoji:
    custom_emoji_id: str
    """ Custom emoji identifier """
    type: str
    """ Type of the reaction, always "custom_emoji" """

    def alter(
        self,
        custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return ReactionTypeCustomEmoji(
            custom_emoji_id=alter1(custom_emoji_id, self.custom_emoji_id),
            type=alter1(type, self.type),
        )


@model
class ReactionTypeEmoji:
    emoji: str
    """ Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡" """
    type: str
    """ Type of the reaction, always "emoji" """

    def alter(
        self,
        emoji: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return ReactionTypeEmoji(
            emoji=alter1(emoji, self.emoji),
            type=alter1(type, self.type),
        )


ReactionType: TypeAlias = ReactionTypeEmoji | ReactionTypeCustomEmoji
__all__ = ["ReactionTypeCustomEmoji", "ReactionTypeEmoji", "ReactionType"]
