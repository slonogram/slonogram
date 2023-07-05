import asyncio

from slonogram import Bot, Dispatcher, LocalSet

TOKEN = open("./test_token").read()
set_ = LocalSet[None]()


@set_.on_message.sent()
async def test(bot: Bot) -> None:
    print("Hello")


async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher(None, bot)

    dp.set.include(set_)


asyncio.run(main())
