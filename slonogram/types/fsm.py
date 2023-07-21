from typing import Protocol, Any, NewType, Optional
from enum import IntEnum, auto


ContextId = NewType("ContextId", int)


class FSMScope(IntEnum):
    USER = auto()
    CHAT = auto()


class FSMContext(Protocol):
    @property
    def scope(self) -> FSMScope:
        ...

    @property
    def id(self) -> ContextId:
        ...

    async def get(self, update_ttl: bool = False) -> Any:
        ...

    async def store(self, update_ttl: bool = True) -> Any:
        ...


class FSMStorage(Protocol):
    async def create_context(
        self,
        # black is a dumb fucker
        id_: ContextId,
        scope: FSMScope,
        ttl: Optional[int] = None,
    ) -> FSMContext:
        ...

    async def get(self, id: ContextId) -> FSMContext:
        ...

    async def drop_context(self, context: FSMContext) -> bool:
        ...


__all__ = ["FSMStorage", "FSMContext", "FSMScope", "ContextId"]
