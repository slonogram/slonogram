from typing import Protocol, TypeVar

from slonogram.bot import Bot
from slonogram.dispatching.stash import Stash

M = TypeVar("M")


class AbstractContext(Protocol[M]):
    model: M
    rpc: Bot
    stash: Stash


__all__ = ["AbstractContext"]
