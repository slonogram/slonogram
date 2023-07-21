from dataclasses import dataclass
from typing import Sequence, Optional
from keyword import kwlist

TP_MAPPINGS = {
    "String": "str",
    "Integer": "int",
    "Boolean": "bool",
    "Float": "float",
}


@dataclass(slots=True)
class ParsedType:
    result: str
    from_schema: bool
    arg: Optional[str] = None


def wrap_list(tp: str) -> str:
    return f"List[{tp}]"


def escape_hard_keywords(name: str) -> str:
    if name in kwlist:
        return name + "_"
    return name


def prefix_schema(r: ParsedType) -> str:
    if r.from_schema:
        if r.arg is None:
            return f"schemas.{r.result}"
        return f"List[schemas.{r.arg}]"
    return r.result


def parse_multiple_types(
    telegram_tps: Sequence[str], prefix: bool = False
) -> str:
    match telegram_tps:
        case [tp]:
            return parse_type(tp, prefix)
        case anything:
            return " | ".join(
                prefix_schema(parse_type_ex(tp))
                if prefix
                else parse_type(tp)
                for tp in anything
            )


def parse_type(telegram_tp: str, prefix: bool = False) -> str:
    if not prefix:
        return parse_type_ex(telegram_tp).result
    return prefix_schema(parse_type_ex(telegram_tp))


def parse_type_ex(telegram_tp: str) -> ParsedType:
    tp = telegram_tp.strip()
    if tp in TP_MAPPINGS:
        return ParsedType(TP_MAPPINGS[tp], False)

    if (wo_prefix := tp.removeprefix("Array of ")) != tp:
        inside = parse_type_ex(wo_prefix)
        return ParsedType(
            wrap_list(inside.result), inside.from_schema, inside.result
        )
    return ParsedType(tp, True)
