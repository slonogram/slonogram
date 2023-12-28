import asyncio

from typing import Callable, Coroutine, Any, ParamSpec
from os import environ

from slonogram.dispatching import Dispatcher
from slonogram.middlewares.backoff_retry import BackoffRetry
from slonogram.bot import Bot

from slonogram.session import add_middleware
from slonogram.executors.long_polling import poll_for_updates

P = ParamSpec("P")


def _sync(c: Callable[P, Coroutine[Any, Any, None]]) -> Callable[P, None]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> None:
        asyncio.run(c(*args, **kwargs))

    return inner


@_sync
async def run_dispatcher(dp: Dispatcher) -> None:
    async with Bot.from_aiohttp(environ["BOT_TOKEN"]) as bot:
        await bot.drop_pending_updates()
        await poll_for_updates(
            bot.alter(
                session=add_middleware(after=BackoffRetry()),
            ),
            dp,
        )
