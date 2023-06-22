from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class PatchId(Generic[T, R], metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def read(cls, from_: T) -> R:
        """
        Get original value of the field
        """
        _ = from_
        raise NotImplementedError


class AttrPatchId(PatchId[T, R]):
    attr: str

    @classmethod
    def read(cls, from_: T) -> R:
        return getattr(from_, cls.attr)
