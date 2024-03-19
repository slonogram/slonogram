from typing import Iterable, Any

from slonogram.handling.handler import Handler
from slonogram.types.interest import Interest
from slonogram.abstract.interested import Interested

def collect_interests(handlers: Iterable[Handler[Any]]) -> set[Interest]:
    interests = set()
    for handler in handlers:
        if isinstance(handler, Interested):
            interests.update(handler.collect_interests())

    return interests

