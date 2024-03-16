from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    Telegram docs: https://core.telegram.org/bots/api#forcereply"""

    force_reply: bool
    """ Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply' """
    input_field_placeholder: str
    """ Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters """
    selective: bool
    """ Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. """

    def alter(
        self,
        force_reply: Omittable[Alterer1[bool]] = OMIT,
        input_field_placeholder: Omittable[Alterer1[str]] = OMIT,
        selective: Omittable[Alterer1[bool]] = OMIT,
    ) -> ForceReply:
        return ForceReply(
            force_reply=alter1(force_reply, self.force_reply),
            input_field_placeholder=alter1(
                input_field_placeholder, self.input_field_placeholder
            ),
            selective=alter1(selective, self.selective),
        )


__all__ = ["ForceReply"]
