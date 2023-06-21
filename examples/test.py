from typing import Any
from slonogram.dp.local_set import LocalSet
from slonogram.bot import Bot

set_ = LocalSet[Any]("test")


@set_.on_message.sent()
async def only_bot(bot: Bot) -> None:
    pass
