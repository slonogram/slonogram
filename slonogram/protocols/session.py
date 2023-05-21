from typing import Dict, Type, TypeVar
from typing import Protocol

from ..schemas.result import Result

T = TypeVar("T")


class Session(Protocol):
    async def raw_method(
        self, ty: Type[T], method_name: str, args: Dict
    ) -> Result[T]:
        ...

    async def finalize(self) -> None:
        ...
