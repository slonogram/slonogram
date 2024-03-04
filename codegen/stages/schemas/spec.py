from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class SchemaSpec:
    pass

__all__ = ["SchemaSpec"]
