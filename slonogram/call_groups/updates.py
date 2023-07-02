from typing import Optional, List, Awaitable

from ..schemas import UpdateType, Update
from .group import CallsGroup, UseRetort


class UpdatesCallGroup(CallsGroup):
    def get(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> Awaitable[List[Update]]:
        return self._call(
            List[Update],
            "getUpdates",
            {},
            (
                ("offset", offset),
                ("limit", limit),
                ("timeout", timeout),
                UseRetort("allowed_updates", allowed_updates),
            ),
        )
