from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default.
    Telegram docs: https://core.telegram.org/bots/api#maskposition"""

    point: str
    """ The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin". """
    scale: float
    """ Mask scaling coefficient. For example, 2.0 means double size. """
    x_shift: float
    """ Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position. """
    y_shift: float
    """ Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position. """

    def alter(
        self,
        point: Omittable[Alterer1[str]] = OMIT,
        scale: Omittable[Alterer1[float]] = OMIT,
        x_shift: Omittable[Alterer1[float]] = OMIT,
        y_shift: Omittable[Alterer1[float]] = OMIT,
    ):
        return MaskPosition(
            point=alter1(point, self.point),
            scale=alter1(scale, self.scale),
            x_shift=alter1(x_shift, self.x_shift),
            y_shift=alter1(y_shift, self.y_shift),
        )


__all__ = ["MaskPosition"]
