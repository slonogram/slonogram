from anyio import create_task_group

from ..dispatching.dispatcher import Dispatcher
from ..bot import Bot

from ..types.interest import Interest


async def poll_for_updates(
    bot: Bot,
    dispatcher: Dispatcher,
    *,
    offset: int | None = None,
    limit: int | None = None,
    timeout: int = 25,
    allowed_updates: set[Interest] | None = None,
) -> None:
    interests = dispatcher.collect_interests()
    if allowed_updates is not None:
        if interests.intersection(allowed_updates) != interests:
            diff = interests.difference(allowed_updates)
            raise ValueError(
                f"Provided `Dispatcher` instance doesn't handle the following updates: {diff!r}"
            )
        interests = allowed_updates

    allowed = [str(n) for n in interests]
    feed_fn = dispatcher.feed_single

    async with create_task_group() as tg:
        while True:
            updates = await bot.get_updates(
                offset=offset,
                limit=limit,
                timeout=timeout,
                allowed_updates=allowed,
            )
            if not updates:
                continue

            for update in updates:
                tg.start_soon(feed_fn, update, bot)
            offset = updates[-1].update_id + 1


__all__ = ["poll_for_updates"]
