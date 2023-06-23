import re

from abc import ABCMeta, abstractmethod
from typing import Any, Tuple, Set, List, TypeVar, Generic

from slonogram.dp.context import Context
from slonogram.handling.scratches.pad import ScratchPad

from ..schemas.chat import Message
from ..handling.scratches import Text

from .extended import ExtendedFilter

V = TypeVar("V", str, Tuple[str], Set[str], List[str])


class _TextFilter(ExtendedFilter[Any, Message], metaclass=ABCMeta):
    def __init__(
        self, case_sensitive: bool = False, _preserve_case: bool = False
    ) -> None:
        self.case_sensitive = case_sensitive
        self._preserve_case = _preserve_case

    @abstractmethod
    def _impl(self, text: str, pad: ScratchPad[Message]) -> bool:
        raise NotImplementedError

    async def __call__(self, ctx: Context[Any, Message]) -> bool:
        text = ctx.pad.get(Text)
        if text is None:
            return False
        if self.case_sensitive and not self._preserve_case:
            return self._impl(text.casefold(), ctx.pad)
        return self._impl(text, ctx.pad)


class Word(_TextFilter, Generic[V]):
    def __init__(self, variants: V, case_sensitive: bool = False) -> None:
        self.variants = _maybe_casefold(variants, case_sensitive)
        super().__init__(case_sensitive, True)

    def _impl(self, text: str, pad: ScratchPad[Message]) -> bool:
        word_end = text.find(" ")
        if word_end == -1:
            word = text
        else:
            word = text[:word_end]

        if self.case_sensitive:
            word = word.casefold()
        if word not in self.variants:
            return False

        if word_end != -1:
            pad.scratch(Text, text[word_end + 1 :])  # type: ignore
        else:
            pad.scratch(Text, "")  # type: ignore
        return True

    def __repr__(self) -> str:
        return f"(text:first_word in {self.variants})"


class Eq(_TextFilter, Generic[V]):
    def __init__(
        self,
        variants: V,
        case_sensitive: bool = False,
    ) -> None:
        self.variants = _maybe_casefold(variants, case_sensitive)
        super().__init__(case_sensitive)

    def _impl(self, text: str, _) -> bool:
        return text in self.variants

    def __repr__(self) -> str:
        casefolding = "" if self.case_sensitive else ".casefold()"
        return f"(text{casefolding} in {self.variants!r})"


class Prefix(_TextFilter):
    def __init__(self, pattern: str, case_sensitive: bool = False) -> None:
        flags = 0 if case_sensitive else re.IGNORECASE
        self.pattern = re.compile(pattern, flags)
        super().__init__(case_sensitive)

    def __repr__(self) -> str:
        ignorecase_sym = "" if self.case_sensitive else "i"
        return f"/^{self.pattern.pattern}/{ignorecase_sym}"

    def _impl(self, text: str, pad: ScratchPad[Message]) -> bool:
        match = self.pattern.match(text)
        if match is None:
            return False
        end = match.end()

        pad.scratch(Text, text[end:])  # type: ignore
        return True


def _maybe_casefold(
    c: V, sensitive: bool
) -> Tuple[str] | Set[str] | List[str]:
    if sensitive:
        return (c,) if isinstance(c, str) else c
    return _casefold_collection(c)


def _infix(t: V) -> str:
    if isinstance(t, str):
        return "=="
    return "in"


def _casefold_collection(c: V) -> Tuple[str] | Set[str] | List[str]:
    if isinstance(c, str):
        return (c.casefold(),)
    return type(c)(v.casefold() for v in c)  # type: ignore
