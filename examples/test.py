from typing import Optional, cast
from re import compile as re_compile, IGNORECASE

import asyncio

from slonogram.bot import Bot

from slonogram.dp.context import Context
from slonogram.dp import Dispatcher
from slonogram.dp.local_set import LocalSet

from slonogram.filters import Just
from slonogram.handling.scratches.scratch import attr_scratch, Scratch
from slonogram.schemas.chat import Message

Text: Scratch[Message, Optional[str]] = attr_scratch("text")
local_set = LocalSet[None]("test")


def prefix(re: str) -> Just[None, Message]:
    pattern = re_compile(re, IGNORECASE)

    async def impl(ctx: Context[None, Message]) -> bool:
        text = ctx.pad.get(Text)
        if text is None:
            return False

        group = pattern.match(text)
        if group is None:
            return False
        end = group.end(0)

        ctx.pad.scratch(Text, cast(Optional[str], text[end:]))
        return True

    return Just(impl)


@local_set.on_message.sent(prefix(r"(м[еэ]йда?|maid)\s*"))
async def on_prefix(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Hello world")


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        dp.set.include(local_set)

        await dp.run_polling()


asyncio.run(main())
