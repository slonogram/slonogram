from ..bot import Bot
from ..schemas.updates import UpdateType, Update

from .local_set import LocalSet

from typing import List, Optional
from anyio import create_task_group


class Dispatcher:
    def __init__(self, bot: Bot) -> None:
        self._bot = bot
        self._sets: List[LocalSet] = []

    async def _processor(self, update: Update) -> None:
        for set_ in self._sets:
            if await set_.process_update(self._bot, update):
                break

    async def run_polling(
        self,
        limit: int = 100,
        timeout: int = 30,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> None:
        offset = None

        async with create_task_group() as task_group:
            while True:
                updates = await self._bot.updates.get_updates(
                    offset, limit, timeout, allowed_updates
                )
                if not updates:
                    continue

                last_update = updates[-1]
                offset = last_update.id + 1

                for update in updates:
                    task_group.start_soon(self._processor, update)

    def register_set(self, set_: LocalSet):
        self._sets.append(set_)


__all__ = ["Dispatcher"]
