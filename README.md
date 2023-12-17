# slonogram

An experimental telegram bot-framework

# Quickstart

```py
import asyncio

from slonogram import (
    HandlerMarker,
    Dispatcher,
    Ic,
    Bot,
    Context,
)
from slonogram.schemas import Message
from slonogram.executors.long_polling import poll_for_updates

TOKEN = "<your token>"
marker = HandlerMarker()

@marker.command("start")
async def start(ctx: Context[Message]) -> None:
    await ctx.reply("Hello world!")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("quickstart")
            .on(Ic.message, start)
    )
    # fmt: on


async def main() -> None:
    async with Bot.from_aiohttp(TOKEN) as bot:
        await poll_for_updates(bot, create_dispatcher())

asyncio.run(main())
```

`HandlerMarker` is optional, you can also write in the following manner:

```py
from slonogram.filtering import Command
# ...

async def start(ctx: Context[Message]) -> None:
    await ctx.reply("Hello world!")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("quickstart")
            .on(Ic.message, start, filter=Command("start"))
    )
    # fmt: on

# ...
```

Disabling `black` formatter on the dispatcher creation is needed because it usually messes up the style inside it. For more examples follow the [examples/](examples/) directory

# Features

- Interactions with api are fully code-generated, so updating library to the upstream changes it pretty straightforward
- Type-safe: we care about correctness and UX, so you get IDE-friendly interface and catching of some errors statically!
- Flexible dispatching: core of this library is the `Dispatcher` and it is: **fully immutable**, [hierarchical](examples/004_hierarchical_filters.py)
- Uses [adaptix](https://github.com/reagento/adaptix)! 😁

# This project is WIP

For ideas consider following the [trashcan](./tashcan/) directory. Feel free to spit your idea on the communities or in the issues.

## Communities

- 🇷🇺 (Russian-speaking group) [@slonogram_ru](https://t.me/slonogram_ru)


