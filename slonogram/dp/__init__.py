from typing import Iterable, NoReturn

from ..bot import Bot
from .local_set import LocalSet


class Dispatcher:
    """
    ### skip_pending:

    skips updates sent before the current time
    (time is retrieved through the `time.time`)
    """

    def __init__(self, bot: Bot, skip_pending: bool = False) -> None:
        self._set: LocalSet = LocalSet("__dispatcher__")
        self.skip_pending = skip_pending
        self._bot = bot

    def include_set(self, set_: LocalSet) -> None:
        self._set.include_set(set_)

    def include_sets(self, iterable: Iterable[LocalSet]) -> None:
        self._set.include_sets(iterable)

    async def run_polling(self) -> NoReturn:
        while True:
            ...
