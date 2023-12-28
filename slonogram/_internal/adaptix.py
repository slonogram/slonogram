from typing import Any
from io import IOBase

from adaptix import Request, CannotProvide
from adaptix._internal.provider.request_filtering import RequestChecker, DirectMediator

from slonogram.utils.json import dump_json


class MatchFirstLayerOfFields(RequestChecker):
    def check_request(self, mediator: DirectMediator, request: Request[Any]) -> None:
        if len(mediator.request_stack) != 2:
            raise CannotProvide


def dump_field(field: Any) -> Any:
    if field is None or isinstance(field, str):
        return field
    elif isinstance(field, IOBase):
        return f"attach://{id(field)}"
    elif isinstance(field, bool):
        return "true" if field else "false"
    return dump_json(field)


__all__ = [
    "MatchFirstLayerOfFields",
    "dump_field",
]
