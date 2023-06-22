import asyncio

from re import compile as re_compile, IGNORECASE

from slonogram.dp.patches import Text
from slonogram.dp.context import Context
from slonogram.dp import Dispatcher
from slonogram.dp.local_set import LocalSet

from slonogram.filters.extended import Just

from slonogram.schemas.chat import Message
from slonogram.bot import Bot
from slonogram.schemas.updates import UpdateType

local_set = LocalSet[None]("test")


def prefix(re: str) -> Just[None, Message]:
    pattern = re_compile(re, IGNORECASE)

    async def impl(ctx: Context[None, Message]) -> bool:
        text = ctx.patched(Text)
        if text is None:
            return False

        group = pattern.match(text)
        if group is None:
            return False
        end = group.end(0)

        ctx.patch(Text, text[end:])
        return True

    return Just(impl)


async def send_patched(ctx: Context[None, Message]) -> bool:
    text = ctx.patched(Text)
    if text is None:
        return False
    await ctx.inter.bot.chat.send_message(
        ctx.model.chat.id, f"patched text: {text}"
    )
    return True


@local_set.on_message.sent(prefix(r"(м[еэ]йда?|maid)\s*") & send_patched)
async def print_message(bot: Bot, message: Message) -> None:
    pass


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        dp.set.include(local_set)

        await dp.run_polling(
            allowed_updates=[UpdateType.message, UpdateType.edited_message]
        )


asyncio.run(main())
