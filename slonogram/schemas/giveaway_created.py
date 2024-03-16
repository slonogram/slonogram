from __future__ import annotations
from slonogram._internal.utils import model


@model
class GiveawayCreated:
    """This object represents a service message about the creation of a scheduled giveaway. Currently holds no information.
    Telegram docs: https://core.telegram.org/bots/api#giveawaycreated"""

    def alter(self) -> GiveawayCreated:
        return GiveawayCreated()


__all__ = ["GiveawayCreated"]
