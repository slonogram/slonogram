from slonogram.bot import Bot
from slonogram.extra.session.mock import MockSession

from .user import MOCK_USER

BOT_MOCK = Bot(MOCK_USER.copy_with(is_bot=True), MockSession())

__all__ = [
    "BOT_MOCK",
]
