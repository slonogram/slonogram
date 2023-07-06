from typing import Protocol, Any
from enum import IntEnum, auto


class ContextScope(IntEnum):
    CHAT = auto()
    USER = auto()


class FSMContext(Protocol):
    async def set_state(self, state: Any) -> None:
        ...

    async def get_state(self) -> Any:
        ...

    @property
    def scope(self) -> ContextScope:
        ...


class FSMStorage(Protocol):
    async def get_context(
        self, scope: ContextScope, key: Any
    ) -> FSMContext:
        ...

    async def create_context(
        self, scope: ContextScope = ContextScope.CHAT
    ) -> FSMContext:
        ...

    async def destroy_context(self, ctx: FSMContext) -> None:
        ...
