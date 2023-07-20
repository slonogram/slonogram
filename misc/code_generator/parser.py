from typing import Sequence
from keyword import kwlist

TP_MAPPINGS = {
    "String": "str",
    "Integer": "int",
    "Boolean": "bool",
    "Float": "float",
}


def escape_hard_keywords(name: str) -> str:
    if name in kwlist:
        return name + "_"
    return name


def parse_multiple_types(telegram_tps: Sequence[str]) -> str:
    match telegram_tps:
        case [tp]:
            return parse_type(tp)
        case anything:
            return " | ".join(parse_type(tp) for tp in anything)


def parse_type(telegram_tp: str) -> str:
    tp = telegram_tp.strip()
    if tp in TP_MAPPINGS:
        return TP_MAPPINGS[tp]

    if (wo_prefix := tp.removeprefix("Array of ")) != tp:
        inside = parse_type(wo_prefix)
        return f"List[{inside}]"
    return tp
