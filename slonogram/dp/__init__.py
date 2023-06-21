from typing import (
    NoReturn,
    List,
    Optional,
    Generic,
    TypeVar,
    Any,
)
from functools import cached_property

from anyio import create_task_group
from anyio.abc import TaskGroup

from ..schemas.updates import UpdateType, Update
from ..bot import Bot
from .context import InterContextData, Context
from .local_set import LocalSet

D = TypeVar("D")


class Dispatcher(Generic[D]):
    """
    ### skip_pending:

    skips updates sent before the current time
    (time is retrieved through the `time.time`)
    """

    def __init__(
        self, data: D, bot: Bot, skip_pending: bool = False
    ) -> None:
        self.set: LocalSet = LocalSet("__dispatcher__")
        self.skip_pending = skip_pending
        self._bot = bot
        self._data = data

    @cached_property
    def _task_group(self) -> TaskGroup:
        return create_task_group()

    async def run_polling(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> NoReturn:
        if self.skip_pending:
            raise NotImplementedError

        bot = self._bot
        updates_call_group = bot.updates
        processor = self.set._process_update

        ctx: Context[D, Any] = Context(
            inter=InterContextData(self._data, bot), bot=bot, model=None
        )

        async with self._task_group as tg:
            while True:
                updates: List[Update] = await updates_call_group.get(
                    offset, limit, timeout, allowed_updates
                )
                if updates:
                    offset = updates[-1].id + 1

                for update in updates:
                    tg.start_soon(processor, ctx, update)
