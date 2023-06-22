from typing import Optional
from ..schemas.chat import Message
from ..protocols.patch_id import AttrPatchId


class Text(AttrPatchId[Message, Optional[str]]):
    attr = "text"
