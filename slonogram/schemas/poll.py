from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    poll_option as _poll_option,
    message_entity as _message_entity,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Poll:
    """This object contains information about a poll.
    Telegram docs: https://core.telegram.org/bots/api#poll"""

    allows_multiple_answers: bool
    """ True, if the poll allows multiple answers """
    close_date: int
    """ Optional. Point in time (Unix timestamp) when the poll will be automatically closed """
    correct_option_id: int
    """ Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot. """
    explanation: str
    """ Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters """
    explanation_entities: list[_message_entity.MessageEntity]
    """ Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation """
    id: str
    """ Unique poll identifier """
    is_anonymous: bool
    """ True, if the poll is anonymous """
    is_closed: bool
    """ True, if the poll is closed """
    open_period: int
    """ Optional. Amount of time in seconds the poll will be active after creation """
    options: list[_poll_option.PollOption]
    """ List of poll options """
    question: str
    """ Poll question, 1-300 characters """
    total_voter_count: int
    """ Total number of users that voted in the poll """
    type: str
    """ Poll type, currently can be "regular" or "quiz" """

    def alter(
        self,
        allows_multiple_answers: Omittable[Alterer1[bool]] = OMIT,
        id: Omittable[Alterer1[str]] = OMIT,
        is_anonymous: Omittable[Alterer1[bool]] = OMIT,
        is_closed: Omittable[Alterer1[bool]] = OMIT,
        options: Omittable[Alterer1[list[_poll_option.PollOption]]] = OMIT,
        question: Omittable[Alterer1[str]] = OMIT,
        total_voter_count: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        close_date: Omittable[Alterer1[int]] = OMIT,
        correct_option_id: Omittable[Alterer1[int]] = OMIT,
        explanation: Omittable[Alterer1[str]] = OMIT,
        explanation_entities: Omittable[
            Alterer1[list[_message_entity.MessageEntity]]
        ] = OMIT,
        open_period: Omittable[Alterer1[int]] = OMIT,
    ) -> Poll:
        return Poll(
            allows_multiple_answers=alter1(
                allows_multiple_answers, self.allows_multiple_answers
            ),
            id=alter1(id, self.id),
            is_anonymous=alter1(is_anonymous, self.is_anonymous),
            is_closed=alter1(is_closed, self.is_closed),
            options=alter1(options, self.options),
            question=alter1(question, self.question),
            total_voter_count=alter1(total_voter_count, self.total_voter_count),
            type=alter1(type, self.type),
            close_date=alter1(close_date, self.close_date),
            correct_option_id=alter1(correct_option_id, self.correct_option_id),
            explanation=alter1(explanation, self.explanation),
            explanation_entities=alter1(
                explanation_entities, self.explanation_entities
            ),
            open_period=alter1(open_period, self.open_period),
        )


__all__ = ["Poll"]
