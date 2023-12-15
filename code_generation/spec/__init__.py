from dataclasses import dataclass

from .method import Method
from .model import SpecModel


@dataclass
class Spec:
    version: str
    release_date: str
    changelog: str

    methods: dict[str, Method]
    models: dict[str, SpecModel]
