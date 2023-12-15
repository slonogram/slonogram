from functools import reduce
from typing import Iterable
from abc import ABCMeta, abstractmethod

from .type_hint import TypeRefs


class Statement(metaclass=ABCMeta):
    def __repr__(self) -> str:
        return self.generate()

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError

    def collect_refs(self) -> TypeRefs:
        return TypeRefs()

def collect_from_all_stmts(stmts: Iterable[Statement]) -> TypeRefs:
    return reduce(
        lambda lhs, rhs: lhs | rhs,
        map(lambda x: x.collect_refs(), stmts),
        TypeRefs(),
    )
