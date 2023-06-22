from typing import Optional
from .scratch import attr_scratch, Scratch
from slonogram.schemas.chat import Message


Text: Scratch[Message, Optional[str]] = attr_scratch("text")

__all__ = ["Text"]
