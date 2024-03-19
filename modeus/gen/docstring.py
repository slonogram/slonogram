from textwrap import wrap

_QUOT = '"""'
_FQUOTE = 'f"""'

def create_docstring(s: str, wrap_width: int | None = 70) -> str:
    use_start = _QUOT
    if wrap_width is not None:
        s = '\n'.join(wrap(s, width=wrap_width))

    if s.startswith('"'):
        s = " " + s
    if s.endswith('"'):
        s += " "

    if _QUOT in s:
        s = s.replace(_QUOT, '\\"""')

    return use_start + s + _QUOT

__all__ = ["create_docstring"]
