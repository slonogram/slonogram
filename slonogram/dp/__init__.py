from typing import List, Iterable, NoReturn

from ..bot import Bot
from .local_set import LocalSet


class Dispatcher:
    def __init__(self, bot: Bot) -> None:
        self.sets: List[LocalSet] = []
        self._bot = bot

    def include_set(self, set_: LocalSet) -> None:
        self.sets.append(set_)

    def include_sets(self, iterable: Iterable[LocalSet]) -> None:
        self.sets.extend(iterable)

    async def run_polling(self) -> NoReturn:
        while True:
            ...
