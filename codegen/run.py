from typing import Iterable, Any
from modeus.stage import Stage

from .stages.schemas import SchemasStage

STAGES: Iterable[Stage[Any, Any]] = [
    SchemasStage()
]

__all__ = ["STAGES"]
