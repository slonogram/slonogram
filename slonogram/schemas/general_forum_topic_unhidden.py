from __future__ import annotations
from slonogram._internal.utils import model


@model
class GeneralForumTopicUnhidden:
    def alter(self):
        return GeneralForumTopicUnhidden()


__all__ = ["GeneralForumTopicUnhidden"]
