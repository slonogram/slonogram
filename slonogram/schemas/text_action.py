from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class Dice:
    emoji: str
    value: int


@dataclass(slots=True)
class Contact:
    phone_number: str
    first_name: str
    last_name: Optional[str] = None

    user_id: Optional[int] = None
    vcard: Optional[str] = None


__all__ = ["Dice", "Contact"]
