from typing import Iterable
from functools import reduce
from telegram_type_parser import Folder, fold_ex

from ..library.type_hint.ref_sources import BUILTINS, SCHEMAS, IO
from ..library.type_hint import Ref, TypeHint


class TypeFolder(Folder[TypeHint]):
    def boolean(self, preset: bool | None = None) -> TypeHint:
        if preset is not None:
            return Ref(BUILTINS, str(preset))
        return Ref(BUILTINS, "bool")

    def integer(self) -> TypeHint:
        return Ref(BUILTINS, "int")

    def float(self) -> TypeHint:
        return Ref(BUILTINS, "float")

    def array_of(self, argument: TypeHint) -> TypeHint:
        return Ref(BUILTINS, "list")[argument]

    def string(self) -> TypeHint:
        return Ref(BUILTINS, "str")

    def ref(self, tp: str) -> TypeHint:
        if tp == "InputFile":
            return Ref(IO, "IOBase")

        return Ref(SCHEMAS, tp)


TYPE_FOLDER = TypeFolder()


def fold_type(tp: str) -> TypeHint:
    return fold_ex(tp, TYPE_FOLDER)


def fold_types(tps: Iterable[str]) -> TypeHint:
    return reduce(
        lambda lhs, rhs: lhs | rhs,
        map(fold_type, tps),
    )
