# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetGameHighScores:
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects."""

    user_id: int
    """Target user id """
    chat_id: int | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the sent message """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """


__all__ = ["GetGameHighScores"]