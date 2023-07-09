import asyncio

from dataclasses import dataclass
from typing import Annotated

from slonogram.di import Container, Injector, Dependency, FromPad
from slonogram.handling.scratches import Text

from slonogram.schemas import Message
from slonogram.filtering.text import Word
from slonogram.bot import Bot
from slonogram.dispatching import Dispatcher, LocalSet


@dataclass(slots=True)
class Master:
    username: str


set_ = LocalSet[None]()
container = Container()
container[Master] = Master(username="@nerodono")
inject = Injector(container)


@set_.on_message.sent(Word(["скажи", "say"]))
@inject
async def say(
    bot: Bot, message: Message, rest: Annotated[str, FromPad(Text)]
) -> None:
    await bot.chat.send_message(message.chat.id, rest)


@set_.on_message.sent(Word("di"))
@inject
async def test(
    bot: Bot,
    message: Message,
    master: Annotated[Master, Dependency],
    rest: Annotated[str, FromPad(Text)],
) -> None:
    print(321)
    await bot.chat.send_message(
        message.chat.id,
        f"text = {message.text}, rest = {rest}, master = {master!r}",
    )


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        dp.set.include(set_)

        await dp.run_polling()


asyncio.run(main())
