# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 08:56:56.806984
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SetGameScore:
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""

    user_id: int
    """User identifier """
    score: int
    """New score, must be non-negative """
    force: bool | None = None
    """Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters """
    disable_edit_message: bool | None = None
    """Pass True if the game message should not be automatically edited to include the current scoreboard """
    chat_id: int | None = None
    """Required if inline_message_id is not specified. Unique identifier for the target chat """
    message_id: int | None = None
    """Required if inline_message_id is not specified. Identifier of the sent message """
    inline_message_id: str | None = None
    """Required if chat_id and message_id are not specified. Identifier of the inline message """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetGameScore"]
