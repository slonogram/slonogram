from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

from .message_entity import MessageEntity
from .user import User


class PollType(str, Enum):
    regular = "regular"
    quiz = "quiz"


@dataclass
class PollOption:
    text: str
    voter_count: int


@dataclass
class PollAnswer:
    poll_id: str
    user: User

    option_ids: List[int]


@dataclass
class Poll:
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int

    is_closed: bool
    is_anonymous: bool

    type_: PollType
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_entities: Optional[List[MessageEntity]] = None

    open_period: Optional[int] = None
    close_date: Optional[int] = None
