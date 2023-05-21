from typing import Optional
from dataclasses import dataclass


@dataclass
class Dice:
    emoji: str
    value: int


@dataclass
class Contact:
    phone_number: str
    first_name: str
    last_name: Optional[str] = None

    user_id: Optional[int] = None
    vcard: Optional[str] = None
