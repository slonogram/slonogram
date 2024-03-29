"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass
from typing import TypeAlias


@dataclass(slots=True)
class ReactionTypeCustomEmoji:
    """The reaction is based on a custom emoji.  Telegram documentation:
    https://core.telegram.org/bots/api#reactiontypecustomemoji"""

    custom_emoji_id: str
    """Custom emoji identifier"""
    type: str
    """Type of the reaction, always "custom_emoji" """

    def alter(
        self,
        custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> ReactionTypeCustomEmoji:
        return ReactionTypeCustomEmoji(
            custom_emoji_id=alter1(custom_emoji_id, self.custom_emoji_id),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class ReactionTypeEmoji:
    """The reaction is based on an emoji.  Telegram documentation:
    https://core.telegram.org/bots/api#reactiontypeemoji"""

    emoji: str
    """Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰",
    "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊",
    "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆",
    "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻",
    "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪",
    "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀",
    "😡" """
    type: str
    """Type of the reaction, always "emoji" """

    def alter(
        self,
        emoji: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> ReactionTypeEmoji:
        return ReactionTypeEmoji(
            emoji=alter1(emoji, self.emoji),
            type=alter1(type, self.type),
        )


ReactionType: TypeAlias = ReactionTypeEmoji | ReactionTypeCustomEmoji
""" This object describes the type of a reaction. Currently, it can be one of
- ReactionTypeEmoji
- ReactionTypeCustomEmoji

Telegram documentation: https://core.telegram.org/bots/api#reactiontype """
__all__ = ["ReactionType", "ReactionTypeCustomEmoji", "ReactionTypeEmoji"]
