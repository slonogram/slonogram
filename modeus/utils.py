def to_snake_case(value: str) -> str:
    out = ""
    if value[0].isupper():
        out += value[0].lower()
        value = value[1:]

    for char in value:
        if char.isupper():
            out += '_' + char.lower()
        else:
            out += char

    return out


__all__ = [
    "to_snake_case",
]

