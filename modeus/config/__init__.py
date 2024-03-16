from os import PathLike
from dataclasses import dataclass
from typing import Generic, TypeVar, Any
from yaml import safe_load, safe_dump

from adaptix import Retort

T = TypeVar("T")


@dataclass(slots=True)
class RevisedConfig(Generic[T]):
    dirty: bool
    data: dict[str, T]

_RETORT = Retort()

def dump_revised(tp: Any, revised: RevisedConfig[T]) -> str:
    return safe_dump(
        _RETORT.dump(revised, RevisedConfig[tp]),
        None,
    )

def try_load_revised(inner: Any, path: PathLike | str) -> Any:
    with open(path) as fp:
        data = safe_load(fp)

    return _RETORT.load(data, RevisedConfig[inner])  # type: ignore


__all__ = ["RevisedConfig", "try_load_revised", "dump_revised"]
