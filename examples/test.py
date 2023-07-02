import asyncio

from slonogram.bot import Bot

from slonogram.filters.text import Prefix, Eq, Word
from slonogram.filters.command import Command

from slonogram.dispatching import Dispatcher
from slonogram.dispatching import LocalSet

from slonogram.schemas.chat import Message

bare = LocalSet[None]()
prefixed_set = LocalSet[None](
    "prefixed", filter_=Prefix(r"(м[еэ]йда?|maid)\s*")
)
set_ = LocalSet[None]()


@bare.on_message.sent(Command("start"))
async def on_start(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "start")


@set_.on_message.sent(Word("скажи") & Word({"сыр", "рыр"}))
async def on_prefix(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "кхе")


@set_.on_message.edited(Eq("сыр"))
async def on_edited(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Сыр")


@set_.on_message.sent(Eq("ладность"))
async def on_ladno(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Прохладность")


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        prefixed_set.include(set_)

        dp.set.include(bare)
        dp.set.include(prefixed_set)

        await dp.run_polling()


asyncio.run(main())
