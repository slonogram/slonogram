from typing import Awaitable

from .group import CallsGroup
from ..schemas.user import User


class UserCallGroup(CallsGroup):
    def get_me(self) -> Awaitable[User]:
        return self._call(User, "getMe", {})
