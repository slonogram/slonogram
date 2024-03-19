"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass
from typing import TypeAlias


@dataclass(slots=True)
class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value changes.
    Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrordatafield"""

    data_hash: str
    """Base64-encoded data hash"""
    field_name: str
    """Name of the data field which has the error"""
    message: str
    """Error message"""
    source: str
    """Error source, must be data"""
    type: str
    """The section of the user's Telegram Passport which has the error, one
    of "personal_details", "passport", "driver_license", "identity_card",
    "internal_passport", "address" """

    def alter(
        self,
        data_hash: Omittable[Alterer1[str]] = OMIT,
        field_name: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorDataField:
        return PassportElementErrorDataField(
            data_hash=alter1(data_hash, self.data_hash),
            field_name=alter1(field_name, self.field_name),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered
    resolved when the file with the document scan changes.  Telegram
    documentation:
    https://core.telegram.org/bots/api#passportelementerrorfile"""

    file_hash: str
    """Base64-encoded file hash"""
    message: str
    """Error message"""
    source: str
    """Error source, must be file"""
    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorFile:
        return PassportElementErrorFile(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.
    Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrorfiles"""

    file_hashes: tuple[str, ...]
    """List of base64-encoded file hashes"""
    message: str
    """Error message"""
    source: str
    """Error source, must be files"""
    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hashes: Omittable[Alterer1[tuple[str, ...]]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorFiles:
        return PassportElementErrorFiles(
            file_hashes=alter1(file_hashes, self.file_hashes),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the document
    changes.  Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrorfrontside"""

    file_hash: str
    """Base64-encoded hash of the file with the front side of the document"""
    message: str
    """Error message"""
    source: str
    """Error source, must be front_side"""
    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of "passport", "driver_license", "identity_card", "internal_passport" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorFrontSide:
        return PassportElementErrorFrontSide(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the document
    changes.  Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrorreverseside"""

    file_hash: str
    """Base64-encoded hash of the file with the reverse side of the document"""
    message: str
    """Error message"""
    source: str
    """Error source, must be reverse_side"""
    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of "driver_license", "identity_card" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorReverseSide:
        return PassportElementErrorReverseSide(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.  Telegram
    documentation:
    https://core.telegram.org/bots/api#passportelementerrorselfie"""

    file_hash: str
    """Base64-encoded hash of the file with the selfie"""
    message: str
    """Error message"""
    source: str
    """Error source, must be selfie"""
    type: str
    """The section of the user's Telegram Passport which has the issue, one
    of "passport", "driver_license", "identity_card", "internal_passport" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorSelfie:
        return PassportElementErrorSelfie(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the
    translation of a document. The error is considered resolved when the
    file changes.  Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrortranslationfile"""

    file_hash: str
    """Base64-encoded file hash"""
    message: str
    """Error message"""
    source: str
    """Error source, must be translation_file"""
    type: str
    """Type of element of the user's Telegram Passport which has the issue,
    one of "passport", "driver_license", "identity_card",
    "internal_passport", "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorTranslationFile:
        return PassportElementErrorTranslationFile(
            file_hash=alter1(file_hash, self.file_hash),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document translation
    change.  Telegram documentation: https://core.telegram.org/bots/api#pa
    ssportelementerrortranslationfiles"""

    file_hashes: tuple[str, ...]
    """List of base64-encoded file hashes"""
    message: str
    """Error message"""
    source: str
    """Error source, must be translation_files"""
    type: str
    """Type of element of the user's Telegram Passport which has the issue,
    one of "passport", "driver_license", "identity_card",
    "internal_passport", "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration", "temporary_registration" """

    def alter(
        self,
        file_hashes: Omittable[Alterer1[tuple[str, ...]]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorTranslationFiles:
        return PassportElementErrorTranslationFiles(
            file_hashes=alter1(file_hashes, self.file_hashes),
            message=alter1(message, self.message),
            source=alter1(source, self.source),
            type=alter1(type, self.type),
        )


@dataclass(slots=True)
class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.  Telegram documentation:
    https://core.telegram.org/bots/api#passportelementerrorunspecified"""

    element_hash: str
    """Base64-encoded element hash"""
    message: str
    """Error message"""
    source: str
    """Error source, must be unspecified"""
    type: str
    """Type of element of the user's Telegram Passport which has the issue"""

    def alter(
        self,
        element_hash: Omittable[Alterer1[str]] = OMIT,
        message: Omittable[Alterer1[str]] = OMIT,
        source: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
    ) -> PassportElementErrorUnspecified:
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
""" This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:
- PassportElementErrorDataField
- PassportElementErrorFrontSide
- PassportElementErrorReverseSide
- PassportElementErrorSelfie
- PassportElementErrorFile
- PassportElementErrorFiles
- PassportElementErrorTranslationFile
- PassportElementErrorTranslationFiles
- PassportElementErrorUnspecified

Telegram documentation: https://core.telegram.org/bots/api#passportelementerror """
__all__ = [
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
]
