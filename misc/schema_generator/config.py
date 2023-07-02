from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Enums:
    types: Dict[str, List[str | List[str]]]
    override: Dict[str, str]


@dataclass
class Config:
    enums: Enums
    renames: Dict[str, str]
