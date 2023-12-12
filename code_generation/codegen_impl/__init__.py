from telegram_type_parser import fold_ex, StringFolder

INDENT = 4


class FixedStringFolder(StringFolder):
    def __init__(self, legacy_bindings: bool, prefix_typing: bool = True) -> None:
        super().__init__(legacy_bindings)
        self.refs: list[str] = []
        self.is_file = False
        self.prefix_typing = prefix_typing

    def ref(self, tp: str) -> str:
        if tp == "InputFile":
            self.is_file = True

            if self.prefix_typing:
                return "typing.BinaryIO"
            return "BinaryIO"

        self.refs.append(tp)
        return super().ref(tp)


def fold(tp: str) -> str:
    return fold_ex(tp, FixedStringFolder(False))
