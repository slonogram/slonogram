def extract_from_utf16(
    text: str,
    offset: int,
    length: int,
) -> str:
    return text.encode("utf-16-le")[offset << 1 : (offset + length) << 1].decode(
        "utf-16-le"
    )


__all__ = ["extract_from_utf16"]
