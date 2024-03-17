from __future__ import annotations
from slonogram.schemas import user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class GameHighScore:
    """This object represents one row of the high scores table for a game.

    Telegram documentation: https://core.telegram.org/bots/api#gamehighscore"""

    position: int
    """ Position in high score table for the game """
    score: int
    """ Score """
    user: _user.User
    """ User """

    def alter(
        self,
        position: Omittable[Alterer1[int]] = OMIT,
        score: Omittable[Alterer1[int]] = OMIT,
        user: Omittable[Alterer1[_user.User]] = OMIT,
    ) -> GameHighScore:
        return GameHighScore(
            position=alter1(position, self.position),
            score=alter1(score, self.score),
            user=alter1(user, self.user),
        )


__all__ = ["GameHighScore"]
