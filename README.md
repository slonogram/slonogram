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

@marker.command()
async def start(ctx: Context[Message]) -> None:
    await ctx.reply("Hello world!")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("quickstart") # name is optional, so also can be created as `Dispatcher()`
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

- Asynchronous, supporting various runtimes. Under the hood, `slonogram` uses [anyio](https://anyio.readthedocs.io/en/stable/) to ensure compatibility with runtimes other than asyncio: [uvloop](https://github.com/MagicStack/uvloop), [trio](https://trio.readthedocs.io/en/stable/) or asyncio, of course
- Interactions with api are fully code-generated, so updating library to the upstream changes is pretty fast and straightforward
- Type-safe: we care about correctness and UX, so you get IDE-friendly interface and catching of some errors statically!
- Flexible dispatching: core of this library is the `Dispatcher` and it is: **fully immutable**, [hierarchical](examples/004_hierarchical_filters.py)
- Uses [adaptix](https://github.com/reagento/adaptix)! 😁

# This project is WIP

For ideas consider following the [trashcan](./trashcan/) directory. Feel free to spit your idea on the communities or in the issues.

## Communities

- 🇷🇺 (Russian-speaking group) [@slonogram_ru](https://t.me/slonogram_ru)


