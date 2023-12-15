from dataclasses import dataclass


class Schema:
    ...


class SchemaUnion(Schema):
    of: list[Schema]


class PlainSchema(Schema):
    ...
