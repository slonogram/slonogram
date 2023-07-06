import asyncio

from slonogram import Bot
from slonogram.dispatching import MessageFlags, Dispatcher, LocalSet

from slonogram.filtering.text import Word, Prefix
from slonogram.schemas import Message

TOKEN = open(".test_token").read()

set_ = LocalSet[None]()
prefixed = LocalSet(filter_=Prefix(r"(м[еэ]йда?|maid)\s*"))


@prefixed.on_message(
    MessageFlags.SENT | MessageFlags.EDITED,
    Word("test"),
)
async def test(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(
        message.chat.id, "Test!", reply_to=message.id
    )


async def main() -> None:
    async with Bot(TOKEN) as bot:
        dp = Dispatcher(None, bot)

        set_.include(prefixed)
        dp.set.include(set_)
        await dp.run_polling()


asyncio.run(main())
