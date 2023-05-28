from slonogram.schemas.chat import Message
from ..extended_filter import ExtendedFilter

from typing import List, Optional
from re import compile as compile_regex, Pattern

TG_COMMAND_REGEX = compile_regex(r"\/([\w\-_\d]+)(@[\w_]+)?")


class Command(ExtendedFilter[Message]):
    def __init__(
        self,
        single_or_more: List[str] | str,
        regex: Pattern = TG_COMMAND_REGEX,
    ) -> None:
        self._single_or_more = single_or_more
        self._regex = regex

    def __repr__(self) -> str:
        if isinstance(self._single_or_more, list):
            obj = self._single_or_more
        else:
            obj = [self._single_or_more]

        return f"<command variations={obj!r}>"

    def _match_single(self, text: str) -> Optional[int]:
        pass

    def __call__(self, message: Message) -> Message:
        raise NotImplementedError("TODO")


__all__ = ["Command"]
