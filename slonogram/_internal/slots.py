import typing as t

from .one_of import OneOf

import dataclasses as dtc

from .omit import Omittable, OMIT
from .alter import Alter1, alter1

from ..schemas.message import Message
from ..schemas.inline_query import InlineQuery
from ..schemas.callback_query import CallbackQuery


@dtc.dataclass(slots=True)
class Slots:
    message: OneOf[Message] = OneOf(())
    edited_message: OneOf[Message] = OneOf(())

    inline_query: OneOf[InlineQuery] = OneOf(())
    callback_query: OneOf[CallbackQuery] = OneOf(())

    def alter(
        self,
        *,
        message: Omittable[Alter1[OneOf[Message]]] = OMIT,
        edited_message: Omittable[Alter1[OneOf[Message]]] = OMIT,
        inline_query: Omittable[Alter1[OneOf[InlineQuery]]] = OMIT,
        callback_query: Omittable[Alter1[OneOf[CallbackQuery]]] = OMIT,
    ) -> t.Self:
        return type(self)(
            message=alter1(self.message, message),
            edited_message=alter1(self.edited_message, edited_message),
            inline_query=alter1(self.inline_query, inline_query),
            callback_query=alter1(self.callback_query, callback_query),
        )
