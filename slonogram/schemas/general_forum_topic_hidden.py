from __future__ import annotations
from slonogram._internal.utils import model


@model
class GeneralForumTopicHidden:
    def alter(self):
        return GeneralForumTopicHidden()


__all__ = ["GeneralForumTopicHidden"]
