from __future__ import annotations
from slonogram._internal.utils import model


@model
class ForumTopicClosed:
    def alter(self):
        return ForumTopicClosed()


__all__ = ["ForumTopicClosed"]
