# How `slonogram` works?

Let's move aside from complex event dispatching, middlewares, filters and so on. `slonogram`'s bare minimum is the following code:

```python
import asyncio

from slonogram import (
    Activation,
    Context,
    Bot,
    poll_for_updates,
)
from slonogram.schemas import Update

async def start(ctx: Context[Update]) -> Activation:
    upd = ctx.model
    if upd.message is not None and upd.message.text is not None:
        msg = upd.message
        text = msg.text
        if text == "/start":
            # TODO: code generation for methods
            await ctx.bot.session(
                "sendMessage",
                {"chat_id": str(msg.chat.id), "text": "Slon is awaken!"},
                {},
            )
            return Activation(start)
    return Activation.stalled()

async def main() -> None:
    async with Bot.from_env() as bot:
        await poll_for_updates(bot, start)

asyncio.run(main())
```

No more, no less (could be less a little). This is all you need, let's dive into details:
1. `Activation` - data structure that describes whether handler's code triggered or not, if triggered - we return `Activation(<handler>)`. Why is it needed? For many dispatching algorithms we usually need to know whether handler is appropriate or not, so, the handler will simply report it
2. `Context[Update]` - context of an event dispatching, contains information necessary for dispatching (model, `Update` in our case, `Bot` and `Stash`, what is `Stash` we'll discuss a little later)
3. `Bot` - telegram bot handle, `.from_env()` means that it will take token from the `TG_TOKEN` (customizable, can be specified via `variable` keyword argument) environment variable and create itself with default (`aiohttp`) session (we will return to that later).

It is surprisingly simple, all we need for dispatching (without counting necessary setup for creating bot instance) is just a function with signature `(Context[Update]) -> Awaitable[Activation]`.

## Dispatcher

But let's get more practical, code from the previous example is a bit tedious to write - it is primitive, handling code is imperative. We can do better

```python
import asyncio

from slonogram import (
    Dispatcher,
    Bot,
    Activation,
    Context
    poll_for_updates
)
from slonogram.schemas import Update, Message

async def start(ctx: Context[Message]) -> Activation:
    if ctx.model.text == "/start":
        print("Issued start")
        return Activation(start)
    return Activation.stalled()

async def help(ctx: Context[Message]) -> Activation:
    if ctx.model.text == "/help":
        print("Issued help")
        return Activation(help)
    return Activation.stalled()

def create_dispatcher() -> Dispatcher[Update]:
    return (
        Dispatcher()
            .interested(message=(start, help))
    )

async def main() -> None:
    async with Bot.from_env() as bot:
        dp = create_dispatcher()
        await poll_for_updates(bot, dp)

asyncio.run(main())
```

Wow, this is more declarative, but still... Something feels off, maybe this manual check for text equality? Let's jump into filters.

```python
import asyncio

from slonogram import (
    Dispatcher,
    Bot,
    Activation,
    Context
    poll_for_updates,
    Filter,
    activate,
)
from slonogram.schemas import Update, Message

def text_equal(text: str) -> Filter[Message]:
    def inner(ctx: Context[Message]) -> bool:
        return ctx.model.text == text
    return inner

@activate
async def start(ctx: Context[Message]) -> None:
    print("Issued start")

@activate
async def help(ctx: Context[Message]) -> None:
    print("Issued help")

def create_dispatcher() -> Dispatcher[Update]:
    return (
        Dispatcher()
            .interested(message=(
                start.filtered(text_equal("start")),
                help.filtered(text_equal("help"))
            ))
    )

async def main() -> None:
    async with Bot.from_env() as bot:
        dp = create_dispatcher()
        await poll_for_updates(bot, dp)

asyncio.run(main())
```

Much better, but what's an `activate` and `Filter`? In `slonogram`, your handlers is just a functions with signature `async (Context[M]) -> Activation`, but writing entirely in that style is tiresome, so, more enjoyable interface must be provided.

1. `activate` is a function that receives the `async (Context[M]) -> None` function and returns `async (Context[M]) -> Activation` function, by default it will always return `Activate(...)`, signaling that function code is triggered, additionally it wraps latter in the `Middlewared[M]` class, so that handler becomes easier to use by providing helpful methods like `.filtered(filter)`
2. `Filter[M]` is a type alias for predicate function: `(Context[M]) -> bool`, `.filtered(text_equal("start"))` equivalent to the following: `Filtered(self, text_equal("start"))`.

As you can see, filtering is also just a wrapper around handlers! `Middlewared` class needed just for more pleasant developer experience and is not necessary.

## More on filtering

Filters can be combined, like we previously did with the middlewares. There's `ExtendedFilter[M]` interface for that. To create `ExtendedFilter[M]` instance you need `Predicate` wrapper:

```python
from typing import Callable
from slonogram.filtering import ExtendedFilter, Predicate

def text_filter(filter: Callable[[str], bool]) -> ExtendedFilter[Message]:
    def inner(ctx: Context[Message]) -> bool:
        text = ctx.model.text
        if text is None:
            return False
        return filter(text)
    return Predicate(inner)

def startswith(text: str) -> Filter[Message]:
    def inner(supplied: str) -> bool:
        return supplied.startswith(text)
    return text_filter(inner)

def contains(text: str) -> Filter[Message]:
    def inner(supplied: str) -> bool:
        return text in supplied

    return text_filter(inner)

filter = startswith("/start") & contains("maid")
print(filter("/start maid"))  # True
print(filter("/start"))  # False

# `or` filters can be used
filter = startswith("/start") | contains("maid")
print(filter("/start")) # True
print(filter("hello maid!"))  # True
print(filter("Nevermind")) # False

# `xor` filter is also available
filter = startswith("/start") ^ contains("maid")
# it is identical (in terms of result, underlying implementation differs) to...
filter = (
    (startswith("/start") | contains("maid"))
    &
    ~(startswith("/start") & contains("maid"))
)
# negative filter is also available! As you can see.

print(filter("/start"))  # True
print(filter("maid")) # True
print(filter("/start maid"))  # False
```


