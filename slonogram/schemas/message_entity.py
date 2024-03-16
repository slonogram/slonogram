from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class MessageEntity:
    custom_emoji_id: str
    """ Optional. For "custom_emoji" only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker """
    language: str
    """ Optional. For "pre" only, the programming language of the entity text """
    length: int
    """ Length of the entity in UTF-16 code units """
    offset: int
    """ Offset in UTF-16 code units to the start of the entity """
    type: str
    """ Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "blockquote" (block quotation), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames), "custom_emoji" (for inline custom emoji stickers) """
    url: str
    """ Optional. For "text_link" only, URL that will be opened after user taps on the text """
    user: _user.User
    """ Optional. For "text_mention" only, the mentioned user """

    def alter(
        self,
        length: Omittable[Alterer1[int]] = OMIT,
        offset: Omittable[Alterer1[int]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
        language: Omittable[Alterer1[str]] = OMIT,
        url: Omittable[Alterer1[str]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return MessageEntity(
            length=alter1(length, self.length),
            offset=alter1(offset, self.offset),
            type=alter1(type, self.type),
            custom_emoji_id=alter1(custom_emoji_id, self.custom_emoji_id),
            language=alter1(language, self.language),
            url=alter1(url, self.url),
            user=alter1(user, self.user),
        )


__all__ = ["MessageEntity"]
