from typing import Any
from io import IOBase

from adaptix import Request, CannotProvide
from adaptix._internal.provider.request_filtering import RequestChecker, DirectMediator

from slonogram.utils import dump_json


class MatchFirstLayerOfFields(RequestChecker):
    def check_request(self, mediator: DirectMediator, request: Request) -> None:
        if len(mediator.request_stack) != 2:
            raise CannotProvide


def dump_field(field: Any) -> Any:
    if field is None or isinstance(field, (IOBase, str)):
        return field
    elif isinstance(field, bool):
        return "true" if field else "false"
    return dump_json(field)
