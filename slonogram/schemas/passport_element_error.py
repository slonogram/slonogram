from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from typing import TypeAlias


@model
class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrordatafield"""

    data_hash: str
    """ Base64-encoded data hash """
    field_name: str
    """ Name of the data field which has the error """
    message: str
    """ Error message """
    source: str
    """ Error source, must be data """
    type: str
    """ The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address" """

    def alter(
        self,
        data_hash: Omittable[Alterer1[str]] = OMIT,
        field_name: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorDataField(
            data_hash=alter1(data_hash, self.data_hash),
            field_name=alter1(field_name, self.field_name),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorfile"""

    file_hash: str
    """ Base64-encoded file hash """
    message: str
    """ Error message """
    source: str
    """ Error source, must be file """
    type: str
    """ The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorFile(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorfiles"""

    file_hashes: list[str]
    """ List of base64-encoded file hashes """
    message: str
    """ Error message """
    source: str
    """ Error source, must be files """
    type: str
    """ The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hashes: Omittable[Alterer1[list[str]]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorFiles(
            file_hashes=alter1(file_hashes, self.file_hashes),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorfrontside"""

    file_hash: str
    """ Base64-encoded hash of the file with the front side of the document """
    message: str
    """ Error message """
    source: str
    """ Error source, must be front_side """
    type: str
    """ The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorFrontSide(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorreverseside"""

    file_hash: str
    """ Base64-encoded hash of the file with the reverse side of the document """
    message: str
    """ Error message """
    source: str
    """ Error source, must be reverse_side """
    type: str
    """ The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorReverseSide(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorselfie"""

    file_hash: str
    """ Base64-encoded hash of the file with the selfie """
    message: str
    """ Error message """
    source: str
    """ Error source, must be selfie """
    type: str
    """ The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorSelfie(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrortranslationfile"""

    file_hash: str
    """ Base64-encoded file hash """
    message: str
    """ Error message """
    source: str
    """ Error source, must be translation_file """
    type: str
    """ Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorTranslationFile(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrortranslationfiles"""

    file_hashes: list[str]
    """ List of base64-encoded file hashes """
    message: str
    """ Error message """
    source: str
    """ Error source, must be translation_files """
    type: str
    """ Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hashes: Omittable[Alterer1[list[str]]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorTranslationFiles(
            file_hashes=alter1(file_hashes, self.file_hashes),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@model
class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    Telegram docs: https://core.telegram.org/bots/api#passportelementerrorunspecified"""

    element_hash: str
    """ Base64-encoded element hash """
    message: str
    """ Error message """
    source: str
    """ Error source, must be unspecified """
    type: str
    """ Type of element of the user's Telegram Passport which has the issue """

    def alter(
        self,
        element_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportElementErrorUnspecified(
            element_hash=alter1(element_hash, self.element_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


PassportElementError: TypeAlias = (
    PassportElementErrorDataField
    | PassportElementErrorFrontSide
    | PassportElementErrorReverseSide
    | PassportElementErrorSelfie
    | PassportElementErrorFile
    | PassportElementErrorFiles
    | PassportElementErrorTranslationFile
    | PassportElementErrorTranslationFiles
    | PassportElementErrorUnspecified
)
__all__ = [
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "PassportElementError",
]
