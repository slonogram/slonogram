from __future__ import annotations
from slonogram.schemas import (
    photo_size as _photo_size,
    animation as _animation,
    message_entity as _message_entity,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Telegram documentation: https://core.telegram.org/bots/api#game"""

    description: str
    """ Description of the game """
    photo: tuple[_photo_size.PhotoSize, ...]
    """ Photo that will be displayed in the game message in chats. """
    title: str
    """ Title of the game """
    animation: _animation.Animation | None = None
    """ Optional. Animation that will be displayed in the game message in chats. Upload via BotFather """
    text: str | None = None
    """ Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters. """
    text_entities: tuple[_message_entity.MessageEntity, ...] | None = None
    """ Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc. """

    def alter(
        self,
        description: Omittable[Alterer1[str]] = OMIT,
        photo: Omittable[Alterer1[tuple[_photo_size.PhotoSize, ...]]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        animation: Omittable[Alterer1[_animation.Animation | None]] = OMIT,
        text: Omittable[Alterer1[str | None]] = OMIT,
        text_entities: Omittable[
            Alterer1[tuple[_message_entity.MessageEntity, ...] | None]
        ] = OMIT,
    ) -> Game:
        return Game(
            description=alter1(description, self.description),
            photo=alter1(photo, self.photo),
            title=alter1(title, self.title),
            animation=alter1(animation, self.animation),
            text=alter1(text, self.text),
            text_entities=alter1(text_entities, self.text_entities),
        )


__all__ = ["Game"]
