from typing import Optional

from ..extended_filter import ExtendedFilter
from slonogram.schemas.chat import Message


class TextContains(ExtendedFilter[Message]):
    def __init__(self, seq: str) -> None:
        self._seq = seq

    @property
    def seq(self) -> str:
        return self._seq

    def __call__(self, value: Message) -> Optional[Message]:
        if value.text is None:
            return None

        if self._seq in value.text:
            return value
        return None


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
