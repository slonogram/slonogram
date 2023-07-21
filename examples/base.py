from typing import Optional, Any

from slonogram.bot import Bot
from slonogram.extra.aiohttp_session import Session

from slonogram.types.fsm import FSMStorage
from slonogram.dispatching import LocalSet, Dispatcher

TOKEN = open(".test_token").read()


async def run_bot(
    set_: LocalSet,
    data: Any = None,
    drop_pending: bool = True,
    fsm: Optional[FSMStorage] = None,
) -> None:
    async with Bot(Session(TOKEN)) as bot:
        dp = Dispatcher(bot, drop_pending, fsm)
        dp.data = data
        dp.set.include(set_)
        await dp.run_polling()
