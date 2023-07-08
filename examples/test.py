import asyncio
from pprint import pprint
from io import StringIO

from slonogram import Bot
from slonogram.dispatching import MessageFlags, Dispatcher, LocalSet

from slonogram.filtering.text import Word, Prefix
from slonogram.schemas import Message, ParseMode

TOKEN = open(".test_token").read()

set_ = LocalSet[None]()
prefixed = LocalSet(filter_=Prefix(r"(м[еэ]йда?|maid)\s*"))


@prefixed.on_message(
    MessageFlags.SENT | MessageFlags.EDITED,
    Word("test"),
)
async def test(bot: Bot, message: Message) -> None:
    buffer = StringIO()
    pprint(message, stream=buffer)
    buffer.seek(0)
    text = buffer.read()

    await bot.chat.send_message(
        message.chat.id, f"```\n{text}\n```", parse_mode=ParseMode.MARKDOWN
    )


@prefixed.on_message.sent(Word("перешли"))
async def testo(bot: Bot, message: Message) -> None:
    await bot.chat.forward_message(5128231220, message.chat.id, message.id)


async def main() -> None:
    async with Bot(TOKEN) as bot:
        dp = Dispatcher(None, bot)

        set_.include(prefixed)
        dp.set.include(set_)
        await dp.run_polling()


asyncio.run(main())
