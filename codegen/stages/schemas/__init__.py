from modeus.stage import Stage
from .spec import SchemaSpec


class SchemasStage(Stage[int, SchemaSpec]):
    def write(self, value: SchemaSpec) -> str:
        raise NotImplementedError
    
    def create_specification(self, args: int) -> SchemaSpec:
        raise NotImplementedError


__all__ = ["SchemasStage"]
