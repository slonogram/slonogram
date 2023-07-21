from typing import Type, Optional, NoReturn
from ..types.fsm import FSMScope, FSMContext, ContextId, FSMStorage


class StubStorage:
    async def create_context(
        self,
        # black is a dumb fucker
        id_: ContextId,
        scope: FSMScope,
        ttl: Optional[int] = None,
    ) -> FSMContext:
        return _not_implemented()

    async def get(self, id: ContextId) -> FSMContext:
        return _not_implemented()

    async def drop_context(self, context: FSMContext) -> bool:
        return _not_implemented()


def _not_implemented() -> NoReturn:
    raise NotImplementedError("FSM storage is not set, tried calling stub")


_: Type[FSMStorage] = StubStorage

__all__ = ["StubStorage"]
