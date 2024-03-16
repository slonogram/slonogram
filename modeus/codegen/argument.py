def arg(name: str, tp: str | None = None, default: str | None = None) -> str:
    if tp is None:
        return name
    
    out = f'{name}: {tp}'
    if default is not None:
        out += ' = ' + default
    
    return out

__all__ = ["arg"]
