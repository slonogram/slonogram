from . import Ref
from .ref_sources import TYPING, BUILTINS, IO


# fmt: off

NONE      = Ref(BUILTINS, "None")
DICT      = Ref(BUILTINS, "dict")
LIST      = Ref(BUILTINS, "list")
STR       = Ref(BUILTINS, "str")
INT       = Ref(BUILTINS, "int")
FLOAT     = Ref(BUILTINS, "float")
TRUE      = Ref(BUILTINS, "True")
FALSE     = Ref(BUILTINS, "False")

ANY       = Ref(TYPING, "Any")

IO_BASE   = Ref(IO, "IOBase")

# fmt: on
