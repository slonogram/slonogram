from code_generation.library.type_hint import TypeRefs
from ..library.statement import Statement
from ..library.dataclass import Dataclass


class ExtendedDataclass(Statement):
    def __init__(self, dtc: Dataclass) -> None:
        self.dtc = dtc

    def generate(self) -> str:
        return self.dtc.generate()

    def collect_refs(self) -> TypeRefs:
        return self.dtc.collect_refs()
