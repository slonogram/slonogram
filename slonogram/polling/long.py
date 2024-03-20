from typing import Iterable

from ..schemas.update import Update
from ..bot import Bot

from ..types.interest import Interest
from ..abstract.interested import Interested
from ..handling.handler import Handler

async def poll_for_updates(
    bot: Bot,
    handler: Handler[Update],
    offset: int | None = None,
    limit: int | None = None,
    timeout: int | None = None,
    interests: Iterable[Interest] | None = None,
) -> None:
    _interests: set[Interest] | None
    if isinstance(interests, set):
        _interests = interests
    elif interests is not None:
        _interests = set(interests)
    elif isinstance(handler, Interested):
        _interests = handler.collect_interests()
    else:
        _interests = None

    raise NotImplementedError()

__all__ = [
    "poll_for_updates",
]
