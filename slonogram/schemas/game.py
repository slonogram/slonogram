from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    photo_size as _photo_size,
    message_entity as _message_entity,
    animation as _animation,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    Telegram docs: https://core.telegram.org/bots/api#game"""

    animation: _animation.Animation
    """ Optional. Animation that will be displayed in the game message in chats. Upload via BotFather """
    description: str
    """ Description of the game """
    photo: list[_photo_size.PhotoSize]
    """ Photo that will be displayed in the game message in chats. """
    text: str
    """ Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters. """
    text_entities: list[_message_entity.MessageEntity]
    """ Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc. """
    title: str
    """ Title of the game """

    def alter(
        self,
        description: Omittable[Alterer1[str]] = OMIT,
        photo: Omittable[Alterer1[list[_photo_size.PhotoSize]]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        animation: Omittable[Alterer1[_animation.Animation]] = OMIT,
        text: Omittable[Alterer1[str]] = OMIT,
        text_entities: Omittable[Alterer1[list[_message_entity.MessageEntity]]] = OMIT,
    ):
        return Game(
            description=alter1(description, self.description),
            photo=alter1(photo, self.photo),
            title=alter1(title, self.title),
            animation=alter1(animation, self.animation),
            text=alter1(text, self.text),
            text_entities=alter1(text_entities, self.text_entities),
        )


__all__ = ["Game"]
