from __future__ import annotations
from slonogram._internal.utils import model


@model
class ForumTopicReopened:
    def alter(self):
        return ForumTopicReopened()


__all__ = ["ForumTopicReopened"]
