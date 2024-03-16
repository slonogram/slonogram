from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class KeyboardButtonRequestUsers:
    max_quantity: int
    """ Optional. The maximum number of users to be selected; 1-10. Defaults to 1. """
    request_id: int
    """ Signed 32-bit identifier of the request that will be received back in the UsersShared object. Must be unique within the message """
    user_is_bot: bool
    """ Optional. Pass True to request bots, pass False to request regular users. If not specified, no additional restrictions are applied. """
    user_is_premium: bool
    """ Optional. Pass True to request premium users, pass False to request non-premium users. If not specified, no additional restrictions are applied. """

    def alter(
        self,
        request_id: Omittable[Alterer1[int]] = OMIT,
        max_quantity: Omittable[Alterer1[int]] = OMIT,
        user_is_bot: Omittable[Alterer1[bool]] = OMIT,
        user_is_premium: Omittable[Alterer1[bool]] = OMIT,
    ):
        return KeyboardButtonRequestUsers(
            request_id=alter1(request_id, self.request_id),
            max_quantity=alter1(max_quantity, self.max_quantity),
            user_is_bot=alter1(user_is_bot, self.user_is_bot),
            user_is_premium=alter1(user_is_premium, self.user_is_premium),
        )


__all__ = ["KeyboardButtonRequestUsers"]
