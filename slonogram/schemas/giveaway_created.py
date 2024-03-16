from __future__ import annotations
from slonogram._internal.utils import model


@model
class GiveawayCreated:
    def alter(self):
        return GiveawayCreated()


__all__ = ["GiveawayCreated"]
