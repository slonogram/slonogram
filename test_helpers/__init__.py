from slonogram.bot import Bot
from slonogram.extra.session.mock import MockSession

from .user import MOCK_USER

BOT_MOCK = Bot(MockSession, MOCK_USER.copy_with(is_bot=True))

__all__ = [
    "BOT_MOCK",
]
