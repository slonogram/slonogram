import asyncio

from typing import Callable, Coroutine, Any, ParamSpec
from os import environ

from slonogram.extra.session.aiohttp import create_session_factory
from slonogram.dispatching import Dispatcher
from slonogram.bot import Bot

from slonogram.executors.long_polling import poll_for_updates

P = ParamSpec("P")


def _sync(c: Callable[P, Coroutine[Any, Any, None]]) -> Callable[P, None]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> None:
        asyncio.run(c(*args, **kwargs))

    return inner


@_sync
async def run_dispatcher(dp: Dispatcher) -> None:
    async with create_session_factory(environ["BOT_TOKEN"]) as factory:
        bot = await Bot.from_session(factory)

        await poll_for_updates(bot, dp)
