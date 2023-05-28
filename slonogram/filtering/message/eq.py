from typing import Optional

from ..extended_filter import ExtendedFilter
from slonogram.schemas.chat import Message


class TextEq(ExtendedFilter[Message]):
    def __init__(self, to: str) -> None:
        self._to = to

    @property
    def to(self) -> str:
        return self._to

    def __call__(self, value: Message) -> Optional[Message]:
        if value.text == self._to:
            return value
        return None
