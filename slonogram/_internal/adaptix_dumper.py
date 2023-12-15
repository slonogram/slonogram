from adaptix import Request, CannotProvide
from adaptix._internal.provider.request_filtering import RequestChecker, DirectMediator


class MatchFirstLayerOfFields(RequestChecker):
    def check_request(self, mediator: DirectMediator, request: Request) -> None:
        if len(mediator.request_stack) != 2:
            raise CannotProvide
