from typing import Optional

from ..types.scratch import attr_scratch, Scratch
from ..schemas import Message


Text: Scratch[Message, Optional[str]] = attr_scratch("text")

__all__ = ["Text"]
