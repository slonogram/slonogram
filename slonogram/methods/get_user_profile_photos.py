# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetUserProfilePhotos:
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""

    user_id: int
    """Unique identifier of the target user """
    offset: int | None = None
    """Sequential number of the first photo to be returned. By default, all photos are returned. """
    limit: int | None = None
    """Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100. """


__all__ = ["GetUserProfilePhotos"]
