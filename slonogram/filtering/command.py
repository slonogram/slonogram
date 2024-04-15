from typing import Iterable

from .extended import ExtendedFilter

from ..types.context import Context
from ..schemas.maybe_inaccessible_message import Message

class Command(ExtendedFilter[Message]):
    __slots__ = ('variations', 'case_sensitive')

    def __init__(
        self,
        variations: Iterable[str] | str,
        case_sensitive: bool = False,
    ) -> None:
        if isinstance(variations, str):
            variations = (variations,)
        self.variations = tuple(
            var if case_sensitive else var.casefold()
            for var in variations
        )
        self.case_sensitive = case_sensitive

    def __repr__(self) -> str:
        return f"Command(variations={self.variations!r}, case_sensitive={self.case_sensitive})"

    def __call__(self, ctx: Context[Message]) -> bool:
        raise NotImplementedError

__all__ = ["Command"]


