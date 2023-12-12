from functools import reduce
from telegram_type_parser import Folder, fold_ex

from ..library.type_hint import TypeHint, Ref, List


class TypeFolder(Folder[TypeHint]):
    def boolean(self, preset: bool | None = None) -> TypeHint:
        if preset is not None:
            return Ref(str(preset))
        return Ref("bool")

    def string(self) -> TypeHint:
        return Ref("str")

    def integer(self) -> TypeHint:
        return Ref("int")

    def float(self) -> TypeHint:
        return Ref("float")

    def array_of(self, argument: TypeHint) -> TypeHint:
        return List(argument)

    def ref(self, tp: str) -> TypeHint:
        if tp == "InputFile":
            return Ref("BinaryIO")
        return Ref(tp)


FOLDER = TypeFolder()


def fold_type(tp: str) -> TypeHint:
    return fold_ex(tp, FOLDER)


def fold_types(tps: list[str]) -> TypeHint:
    if not tps:
        raise ValueError("Types is empty")
    elif len(tps) == 1:
        return fold_type(tps[0])

    return reduce(
        lambda lhs, rhs: lhs | rhs,
        map(fold_type, tps),
    )
