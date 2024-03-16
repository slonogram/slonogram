from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class LinkPreviewOptions:
    """Describes the options used for link preview generation.
    Telegram docs: https://core.telegram.org/bots/api#linkpreviewoptions"""

    is_disabled: bool
    """ Optional. True, if the link preview is disabled """
    prefer_large_media: bool
    """ Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview """
    prefer_small_media: bool
    """ Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview """
    show_above_text: bool
    """ Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text """
    url: str
    """ Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used """

    def alter(
        self,
        is_disabled: Omittable[Alterer1[bool]] = OMIT,
        prefer_large_media: Omittable[Alterer1[bool]] = OMIT,
        prefer_small_media: Omittable[Alterer1[bool]] = OMIT,
        show_above_text: Omittable[Alterer1[bool]] = OMIT,
        url: Omittable[Alterer1[str]] = OMIT,
    ) -> LinkPreviewOptions:
        return LinkPreviewOptions(
            is_disabled=alter1(is_disabled, self.is_disabled),
            prefer_large_media=alter1(prefer_large_media, self.prefer_large_media),
            prefer_small_media=alter1(prefer_small_media, self.prefer_small_media),
            show_above_text=alter1(show_above_text, self.show_above_text),
            url=alter1(url, self.url),
        )


__all__ = ["LinkPreviewOptions"]
