from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatpermissions"""

    can_add_web_page_previews: bool | None = None
    """ Optional. True, if the user is allowed to add web page previews to their messages """
    can_change_info: bool | None = None
    """ Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups """
    can_invite_users: bool | None = None
    """ Optional. True, if the user is allowed to invite new users to the chat """
    can_manage_topics: bool | None = None
    """ Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages """
    can_pin_messages: bool | None = None
    """ Optional. True, if the user is allowed to pin messages. Ignored in public supergroups """
    can_send_audios: bool | None = None
    """ Optional. True, if the user is allowed to send audios """
    can_send_documents: bool | None = None
    """ Optional. True, if the user is allowed to send documents """
    can_send_messages: bool | None = None
    """ Optional. True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues """
    can_send_other_messages: bool | None = None
    """ Optional. True, if the user is allowed to send animations, games, stickers and use inline bots """
    can_send_photos: bool | None = None
    """ Optional. True, if the user is allowed to send photos """
    can_send_polls: bool | None = None
    """ Optional. True, if the user is allowed to send polls """
    can_send_video_notes: bool | None = None
    """ Optional. True, if the user is allowed to send video notes """
    can_send_videos: bool | None = None
    """ Optional. True, if the user is allowed to send videos """
    can_send_voice_notes: bool | None = None
    """ Optional. True, if the user is allowed to send voice notes """

    def alter(
        self,
        can_add_web_page_previews: Omittable[Alterer1[bool | None]] = OMIT,
        can_change_info: Omittable[Alterer1[bool | None]] = OMIT,
        can_invite_users: Omittable[Alterer1[bool | None]] = OMIT,
        can_manage_topics: Omittable[Alterer1[bool | None]] = OMIT,
        can_pin_messages: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_audios: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_documents: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_messages: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_other_messages: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_photos: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_polls: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_video_notes: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_videos: Omittable[Alterer1[bool | None]] = OMIT,
        can_send_voice_notes: Omittable[Alterer1[bool | None]] = OMIT,
    ) -> ChatPermissions:
        return ChatPermissions(
            can_add_web_page_previews=alter1(
                can_add_web_page_previews, self.can_add_web_page_previews
            ),
            can_change_info=alter1(can_change_info, self.can_change_info),
            can_invite_users=alter1(can_invite_users, self.can_invite_users),
            can_manage_topics=alter1(can_manage_topics, self.can_manage_topics),
            can_pin_messages=alter1(can_pin_messages, self.can_pin_messages),
            can_send_audios=alter1(can_send_audios, self.can_send_audios),
            can_send_documents=alter1(can_send_documents, self.can_send_documents),
            can_send_messages=alter1(can_send_messages, self.can_send_messages),
            can_send_other_messages=alter1(
                can_send_other_messages, self.can_send_other_messages
            ),
            can_send_photos=alter1(can_send_photos, self.can_send_photos),
            can_send_polls=alter1(can_send_polls, self.can_send_polls),
            can_send_video_notes=alter1(
                can_send_video_notes, self.can_send_video_notes
            ),
            can_send_videos=alter1(can_send_videos, self.can_send_videos),
            can_send_voice_notes=alter1(
                can_send_voice_notes, self.can_send_voice_notes
            ),
        )


__all__ = ["ChatPermissions"]
