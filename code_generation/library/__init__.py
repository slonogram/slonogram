from textwrap import indent as _indent


def indent(s: str) -> str:
    return _indent(s, "    ")


__all__ = ["indent"]
