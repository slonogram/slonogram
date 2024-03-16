from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Story:
    chat: _chat.Chat
    """ Chat that posted the story """
    id: int
    """ Unique identifier for the story in the chat """

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        id: Omittable[Alterer1[int]] = OMIT,
    ):
        return Story(
            chat=alter1(chat, self.chat),
            id=alter1(id, self.id),
        )


__all__ = ["Story"]
